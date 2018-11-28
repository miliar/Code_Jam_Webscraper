#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
using namespace std;

int T, N, K, cas = 0;
double p[205], pp[205];
double dp[205][205];

double solve(int n) {
    dp[0][0] = 1.0;
    for (int i = 1; i <= n; ++i) {
        for (int j = 0; j <= i; ++j) {
            dp[i][j] = 0.0;
            dp[i][j] += dp[i - 1][j] * (1 - pp[i]);
            if (j) dp[i][j] += dp[i - 1][j - 1] * pp[i];
        }
    }
    return dp[n][n >> 1];
}

int main()
{
    freopen("b.in", "r", stdin);
    freopen("b_out.txt", "w", stdout);
    scanf("%d", &T);
    while (T--) {
        scanf("%d%d", &N, &K);
        for (int i = 1; i <= N; ++i) scanf("%lf", p + i);
        double ans = 0;
        for (int msk = 0; msk < (1 << N); ++msk) {
            int n = 0;
            for (int i = 0; i < N; ++i) if (msk >> i & 1) {
                pp[++n] = p[i + 1];
            }
            if (n == K) ans = max(ans, solve(n));
        }
        printf("Case #%d: %.10lf\n", ++cas, ans);
    }
    return 0;
}
