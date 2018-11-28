#include <bits/stdc++.h>
using namespace std;

double dp[210][210];
double p[210];
int r[210];

void ck(double &x, double y) {
    x += y;
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        int n, K;
        scanf("%d%d", &n, &K);
        for (int i = 0; i < n; i++) {
            scanf("%lf", &p[i]);
        }
        sort(p, p + n);
        double res = 0.0;
        for (int l = 0; l <= K; l++) {
            int rr = K - l, cnt = 0;
            for (int i = 0; i < l; i++) {
                r[cnt++] = i;
            }
            for (int j = n - 1; j >= n - rr; j--) {
                r[cnt++] = j;
            }
            assert(cnt == K);
            memset(dp, 0, sizeof(dp));
            dp[0][0] = 1.0;
            for (int i = 0; i < K; i++) {
                for (int j = 0; j <= K / 2 && j <= i; j++) {
                    ck(dp[i + 1][j + 1], dp[i][j] * p[r[i]]);
                    ck(dp[i + 1][j], dp[i][j] * (1.0 - p[r[i]]));
                }
            }
            res = max(res, dp[K][K / 2]);
        }
        printf("Case #%d: %.20f\n", cas, res);
        fprintf(stderr, "Case #%d: %.20f\n", cas, res);
    }
    return 0;
}