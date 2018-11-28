#include <iostream>
#include <algorithm>
using namespace std;
int main() {
    int T;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ++ca) {
        int n, k;
        double pp[300], p[300];
        scanf("%d%d", &n, &k);
        for (int i = 0; i < n; ++i) {
            scanf("%lf", &pp[i]);
        }
        sort(pp, pp+n);
        double ans = 0;
        for (int i = 0; i <= k; ++i) {
            int l = 0;
            for (int j = 0; j < i; ++j) {
                p[l++] = pp[j];
            }
            for (int j = n - k + i - 1; j < n; ++j) {
                p[l++] = pp[j];
            }
            double dp[300][300];
            memset(dp, 0, sizeof(dp));
            dp[0][0] = 1-p[0];
            dp[0][1] = p[0];
            for (int j = 1; j < l; ++j) {
                for (int k = 0; k <= j; ++k) {
                    dp[j][k] += dp[i-1][k] * (1-p[j]);
                    if (k) {
                        dp[j][k] += dp[i-1][k-1]*p[j];
                    }
                }
            }
            ans = max(ans, dp[l-1][(l+1)/2-1]);
        }
        printf("Case #%d: %.10f\n", ca, ans);
    }
    return 0;
}
