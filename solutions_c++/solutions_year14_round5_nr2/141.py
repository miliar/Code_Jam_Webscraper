#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int n, p, q, h[128], g[128];
int dp[128][1280];

int solve() {
    memset(dp, -1, sizeof(dp));
    dp[0][0] = 0;
    dp[0][1] = 0;
    rep (i, n) rep (r, 1280) if (dp[i][r] >= 0) {
        int k = 0;
        for (; k * q < h[i]; k++) {
            int e = h[i] - k*q;
            int x = (e + p - 1) / p;
            if (r + k >= x) {
                dp[i+1][r+k-x] = max(dp[i+1][r+k-x], dp[i][r] + g[i]);
            }
        }
        dp[i+1][r+k] = max(dp[i+1][r+k], dp[i][r]);
    }
    int ans = 0;
    rep (i, 1280) ans = max(ans, dp[n][i]);
    return ans;
}

int main() {
    int T;
    scanf("%d", &T);
    rep (_q, T) {
        scanf("%d%d%d", &p, &q, &n);
        rep (i, n) scanf("%d%d", h+i, g+i);
        printf("Case #%d: %d\n", _q+1, solve());
    }
    return 0;
}
