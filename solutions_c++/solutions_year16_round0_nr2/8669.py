/*******************************************************************************
	> File Name: b.cpp
	> Author: sillyplus 
	> Mail: oi_boy@sina.cn 
	> Created Time: Sun Apr 10 02:14:58 2016
*******************************************************************************/

#include <bits/stdc++.h>

using namespace std;

int main(int argc, char* argv[]) {
    int t, tt = 0;
    cin >> t;
    while (t--) {
        tt++;
        int n, ans;
        string s;
        string st = "";
        cin >> s;
        n = s.length();
        for (int i = 0; i < n; ++i) {
            if (s[i] != st[st.size()-1]) {
                st += s[i];
            }
        }
        int stn = st.size();
        if (stn % 2) {
            ans = st[0] == '+' ? stn-1 : stn;
        } else {
            ans = st[0] == '+' ? stn : stn-1;
        }
        printf("Case #%d: %d\n", tt, ans);
    }
    return 0;
}
