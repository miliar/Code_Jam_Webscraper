#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

int n, k;
long double pr[440];
long double dp[210][456];

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        scanf("%d %d", &n, &k);
        for (int i = 0; i < n; ++i) {
            long double x;
            scanf("%Lf", &x);
            pr[i] = x;
        }
        sort(pr, pr + n);
        for (int i = 0; i < n; ++i) {
            pr[i + n] = pr[i];
        }
        long double ans = 0;
        for (int s = 0; s < n; ++s) {
            memset(dp, 0, sizeof(dp));
            dp[0][220] = 1;
            for (int i = s; i < s + k; ++i) {
                for (int j = 1; j < 450; ++j) {
                    dp[i - s + 1][j] = pr[i] * dp[i - s][j - 1] +
                            (1. - pr[i]) * dp[i - s][j + 1];
                }
            }
            ans = max(ans, dp[k][220]);
        }
        printf("Case #%d: %.10Lf\n", t, (long double) ans);
    }
    return 0;
}
