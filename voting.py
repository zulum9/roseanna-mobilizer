import time

import pandas as pd
import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# --- 1. SETTINGS & CONFIGURATION ---
# Updated with your actual HTML attributes
CONTESTANT_VALUE = "9e6b3705-be43-4cf7-ae63-568b628b5b65"
CONTESTANT_SELECTOR_ID = "choice-9e6b3705-be43-4cf7-ae63-568b628b5b65-selector"
POLL_URL = "https://missuniversezimbabwe.com/poll/miss-universe-zimbabwe-2026/"

st.set_page_config(page_title="Roseanna Hall Mobilizer", page_icon="🇿🇼", layout="wide")


# # --- 2. THE AUTOMATION ENGINE ---


# def execute_auto_vote():
#     chrome_options = Options()
#     # chrome_options.add_argument("--headless")

#     driver = webdriver.Chrome(
#         service=Service(ChromeDriverManager().install()), options=chrome_options
#     )

#     try:
#         driver.get(POLL_URL)

#         # 1. NEW: Explicit Wait (Wait up to 15 seconds for the element to exist)
#         st.toast("Waiting for page to fully render...")
#         wait = WebDriverWait(driver, 15)

#         # Try to find the element by ID first as it's the most unique
#         try:
#             selection = wait.until(
#                 EC.presence_of_element_located((By.ID, CONTESTANT_SELECTOR_ID))
#             )
#         except:
#             # Fallback to Value selector if ID fails
#             selection = wait.until(
#                 EC.presence_of_element_located(
#                     (By.CSS_SELECTOR, f"input[value='{CONTESTANT_VALUE}']")
#                 )
#             )

#         # 2. Scroll to element (TotalPoll sometimes needs the element in view to click)
#         driver.execute_script(
#             "arguments[0].scrollIntoView({block: 'center'});", selection
#         )
#         time.sleep(1)

#         # 3. Click using Javascript
#         driver.execute_script("arguments[0].click();", selection)
#         st.toast("Roseanna Hall selected!")

#         time.sleep(2)

#         # 4. Wait for and click the Vote button
#         submit_btn = wait.until(
#             EC.element_to_be_clickable(
#                 (By.CSS_SELECTOR, "button[type='submit'][value='vote']")
#             )
#         )
#         driver.execute_script("arguments[0].click();", submit_btn)

#         time.sleep(5)  # Wait for confirmation message
#         return True
#     except Exception as e:
#         st.error(f"Automation failed: {e}")
#         return False
#     finally:
#         driver.quit()


# --- 3. FRONT-END INTERFACE ---
st.title("🇿🇼 Roseanna Hall Support Hub")

col_profile, col_stats = st.columns([1, 2])

with col_profile:
    try:
        # 2026 Streamlit Standard
        st.image("contestant.jpg", width="stretch")
    except:
        st.warning("Place 'contestant.jpg' in the project folder to see the photo.")

    st.subheader("Roseanna Hall")
    st.write("Representing innovation, elegance, and Zimbabwean excellence.")

with col_stats:
    st.write("### 📊 Live Campaign Status")
    chart_data = pd.DataFrame(
        {
            "Contestant": ["Roseanna Hall", "Competitor A", "Competitor B"],
            "Votes": [2105, 2340, 1150],
        }
    )
    # 2026 Streamlit Standard
    st.bar_chart(chart_data.set_index("Contestant"), width="stretch")

    gap = 2340 - 2105
    st.metric(label="Gap to #1", value=f"-{gap} Votes", delta_color="inverse")

st.divider()

# --- 4. ACTION CONTROLS ---
st.header("⚡ Mobilization Tools")
c1, c2 = st.columns(2)

with c1:
    st.info("#### Manual Mode")
    st.write("Share this link with your groups to get organic votes.")
    st.link_button("Open Official Voting Page", POLL_URL)

# with c2:
#     st.success("#### Automation Mode")
#     st.write("Automatically execute the 2-step voting process.")
#     if st.button("🚀 Run Automatic Vote Cycle"):
#         with st.spinner("Executing Selenium sequence..."):
#             if execute_auto_vote():
#                 st.balloons()
#                 st.success("Success! The vote cycle has been completed.")

# # Sidebar Details
# st.sidebar.markdown(f"""
# ### Campaign Info
# - **Candidate:** Roseanna Hall
# - **Poll Status:** Active
# - **Target URL:** [Link]({POLL_URL})
# """)
