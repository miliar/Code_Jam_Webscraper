#include <cstdio>
#include <cstring>
#include <algorithm>

int dp[101][3000];

int h[100], g[100];

void update(int &a, const int &b) {
    a = std :: max(a, b);
}

int main() {
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++ cas) {
        int n, P, Q;
        scanf("%d%d%d", &P, &Q, &n);
        for (int i = 0; i < n; ++ i)
            scanf("%d%d", &h[i], &g[i]);
        memset(dp, -1, sizeof(dp));
        dp[0][1] = 0;
        for (int i = 0; i < n; ++ i)
            for (int j = 0; j < 3000; ++ j)
                if (dp[i][j] != -1) {
                    int numq = (h[i] + Q - 1) / Q;
                    int nump = (h[i] - (numq - 1) * Q + P - 1) / P;
                    update(dp[i + 1][j + numq], dp[i][j]);
                    if (j + numq - 1 - nump >= 0)
                        update(dp[i + 1][j + numq - 1 - nump], dp[i][j] + g[i]);
                }
        int ans = 0;
        for (int i = 0; i < 3000; ++ i) {
            ans = std :: max(ans, dp[n][i]);
        }
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
