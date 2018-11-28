#include <bits/stdc++.h>

using namespace std;

int main () {
    ios::sync_with_stdio(false);

    vector <vector <int>> dp(1024, vector <int> (1024, 0));

    for (int i = 1; i < 1024; ++i) {
        dp[i][0] = 1024;
        for (int j = 1; j < 1024; j++) {
            dp[i][j] = dp[i - 1][j - 1];
            for (int k = 1; k < i; k++) {
                dp[i][j] = min(dp[i][j], dp[k][j] + dp[i - k][j] + 1);
            }
            // if (i <= 5 && j <= 5) {
            //     cout << ">> " << i << ' ' << j << ' ' << dp[i][j] << endl;
            //     //     cout << ' ' << dp[i - 1][j - 1] << ' ' << (i / 2) << "+" << (i % 2) <<  "=" << k << ' ' << dp[k][j] << endl;
            // }
        }
    }

    int t;
    cin >> t;
    for (int cs = 0; cs < t; ++cs) {
        int n;
        cin >> n;

        vector <int> a(n);
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
        }

        int ans = 1024;
        for (int d = 1; d < 1024; d++) {
            int sp = 0;
            for (int c : a) {
                sp += dp[c][d];
            }
            ans = min (ans, sp + d);
            // if (d < 6) cout << ">>> " << d << ' ' << sp << endl;
        }

        cout << "Case #" << cs + 1 << ": " << ans << endl;
    }

    return 0;
}







