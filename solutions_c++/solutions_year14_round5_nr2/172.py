#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

#define MAX 128
#define MAXN 1024

using namespace std;

int h[MAX], g[MAX], a[MAX], b[MAX], c[MAX];
int dp[MAX][MAXN];

int solve(int n) {
    int i, j, ret = 0;

    memset(dp, -1, sizeof(dp));
    dp[0][1] = 0;
    for (i = 1; i <= n; ++i) {
        for (j = 0; j < MAXN; ++j) {
            if (j - b[i] + a[i] >= 0 && j - b[i] + a[i] < MAXN && ~dp[i - 1][j - b[i] + a[i]]) {
                dp[i][j] = max(dp[i][j], dp[i - 1][j - b[i] + a[i]] + g[i]);
            }
            if (j - c[i] >= 0 && j - c[i] < MAXN && ~dp[i - 1][j - c[i]]) {
                dp[i][j] = max(dp[i][j], dp[i - 1][j - c[i]]);
            }

            //printf("i = %d, j = %d, dp = %d\n", i, j, dp[i][j]);
            //getchar();
        }
    }
    for (i = 0; i < MAXN; ++i) ret = max(ret, dp[n][i]);

    return ret;
}

int main() {
    int t, ct = 0, n, p, q, i, ans;

    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    scanf("%d", &t);
    while (t--) {
        scanf("%d%d%d", &p, &q, &n);
        for (i = 1; i <= n; ++i) {
            scanf("%d%d", &h[i], &g[i]);
            if (!(h[i] % q)) {
                a[i] = (q + p - 1) / p;
                b[i] = h[i] / q - 1;
            } else {
                a[i] = (h[i] % q + p - 1) / p;
                b[i] = h[i] / q;
            }
            c[i] = (h[i] + q - 1) / q;
        }
        ans = solve(n);

        printf("Case #%d: %d\n", ++ct, ans);
    }

    return 0;
}
