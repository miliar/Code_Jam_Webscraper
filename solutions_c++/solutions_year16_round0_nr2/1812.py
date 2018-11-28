#include <bits/stdc++.h>

using namespace std;

const int MAXN = 100;
int dp[MAXN][2];

int main() {
    freopen("inp.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin >> t;
    for (int c = 1; c <= t; c++) {
        string s;
        cin >> s;
        int n = s.length();
        dp[0][0] = (s[0] == '+');
        dp[0][1] = (s[0] == '-');
        for (int i = 1; i < n; i++) {
            if (s[i] == '-') {
                dp[i][0] = dp[i - 1][0];
                dp[i][1] = dp[i - 1][0] + 1;
            } else {
                dp[i][0] = dp[i - 1][1] + 1;
                dp[i][1] = dp[i - 1][1];
            }
        }
        cout << "Case #" << c << ": " << dp[n - 1][1] << endl;
    }
}
        
