#include <bits/stdc++.h>
using namespace std;

const int N = 1000000;
long long a[N];
long long s[N + 1];
int dp[101][10005][2];

inline void solve(int test) {
    int p, q, n;
    cin >> p >> q >> n;
    int h[n];
    int g[n];
    for (int i = 0; i < n; ++i) {
        cin >> h[i] >> g[i];
    }


    memset(dp, 255, sizeof(dp));
    dp[0][0][0] = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j <= 10 * n; ++j)
        {
            if (dp[i][j][0] >= 0) {
                int o = (h[i] + q - 1) / q;
                dp[i + 1][j + o][0] = max(dp[i + 1][j + o][0], dp[i][j][0]);

                for (int qw = 0; qw <= min(j, 10); ++qw) {
                    int tmp = h[i] - qw * p;
                    if (tmp <= 0) {
                        dp[i + 1][j - qw][1] = max(dp[i + 1][j - qw][1], dp[i][j][0] + g[i]);
                        break;
                    }
                    for (int k = 0; k < 10; ++k) {
                        tmp -= k * (p + q);
                        if (tmp <= 0) {
                            break;
                        }
                        int o = (tmp - 1) / q;
                        int w = tmp % q;
                        if (w == 0) w += q;
                        if (w <= p) {
                            dp[i + 1][j - qw + o][1] = max(dp[i + 1][j - qw + o][1], dp[i][j][0] + g[i]);
                        }
                        tmp += k * (p + q);
                    }
                }
            }
            if (dp[i][j][1] >= 0) {
                int o = (h[i] - 1) / q;
                dp[i + 1][j + o][0] = max(dp[i + 1][j + o][0], dp[i][j][1]);

                for (int qw = 0; qw <= min(j, 10); ++qw) {
                    int tmp = h[i] - qw * p;
                    if (tmp <= 0) {
                        dp[i + 1][j - qw][1] = max(dp[i + 1][j - qw][1], dp[i][j][1] + g[i]);
                        break;
                    }
                    tmp -= q;
                    for (int k = 0; k < 10; ++k) {
                        tmp -= k * (p + q);
                        if (tmp <= 0) {
                            break;
                        }
                        int o = (tmp - 1) / q;
                        int w = tmp % q;
                        if (w == 0) w += q;
                        if (w <= p) {
                            dp[i + 1][j - qw + o][1] = max(dp[i + 1][j - qw + o][1], dp[i][j][1] + g[i]);
                        }
                        tmp += k * (p + q);
                    }
                }
            }
        }
    }
    int ans = 0;
    for (int j = 0; j <= 10 * n; ++j) {
        ans = max(ans, dp[n][j][0]);
        ans = max(ans, dp[n][j][1]);
    }
    cout << "Case #" << test << ": ";
    cout << ans << endl;
}

int main() {
    freopen("B.in", "r", stdin);
    freopen("out", "w", stdout);
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        solve(i + 1);
    }
    return 0;
}
