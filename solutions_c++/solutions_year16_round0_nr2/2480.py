// in the name of ogd

#include <bits/stdc++.h>
#define sz(x) ((int)x.size())
using namespace std;

int32_t main() {
    int tt; cin >> tt;
    for (int t = 1; t <= tt; t++) {
        string s; cin >> s;
        vector<bool> v;
        v.push_back(s[0] == '+');
        for (int i = 1; i < sz(s); i++) {
            int bul = (s[i] == '+');
            if (bul != v.back())
                v.push_back(bul);
        }
        int dp[2][111] = {};
        dp[0][0] = (s[0] == '+');
        dp[1][0] = (s[0] == '-');
        for (int i = 1; i < sz(v); i++) {
            int bul = v[i];
            if (bul) {
                dp[0][i] = dp[1][i-1] + 1;
                dp[1][i] = dp[1][i-1];
            }
            else {
                dp[0][i] = dp[0][i-1];
                dp[1][i] = dp[0][i-1] + 1;
            }
        }
        cout << "Case #" << t << ": " << dp[1][sz(v)-1] << endl;
    }
}