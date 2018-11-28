#include <bits/stdc++.h>

using namespace std;
int r,c;
char s[110][110];
int dp[110][110][10];

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t;
    cin >> t;
    for(int cas = 1; cas <= t ; cas ++) { 
        cin >> r >> c;
        for(int i = 0 ; i < r ; i++) {
            cin >> s[i];
        }
        int res = 0;
        memset(dp, 0, sizeof(dp));
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (s[i][j] != '.') {
                    dp[i][j][0] = 1;
                    break;
                }
            }
        }
        for (int i = 0; i < r; i++) {
            for (int j = c-1; j >= 0; j--) {
                if (s[i][j] != '.') {
                    dp[i][j][1] = 1;
                    break;
                }
            }
        }
        for (int j = 0; j < c; j++) {
            for (int i = 0 ; i < r; i++) {
                if (s[i][j] != '.') {
                    dp[i][j][2] = 1;
                    break;
                }
            }
        }
        for (int j = 0; j < c; j++) {
            for (int i = r-1; i >= 0; i--) {
                if (s[i][j] != '.') {
                    dp[i][j][3] = 1;
                    break;
                }
            }
        }

        bool flag = true;
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (dp[i][j][0] && dp[i][j][1] && dp[i][j][2] && dp[i][j][3]) {
                    flag = false;
                    break;
                }
                if (dp[i][j][0] && s[i][j] == '<') res++;
                if (dp[i][j][1] && s[i][j] == '>') res++;
                if (dp[i][j][2] && s[i][j] == '^') res++;
                if (dp[i][j][3] && s[i][j] == 'v') res++;
            }
            if (!flag) break;
        }

        if (!flag) cout << "Case #" << cas << ": IMPOSSIBLE" << endl;
        else cout << "Case #" << cas << ": " << res << endl;
    }
    return 0;
}
