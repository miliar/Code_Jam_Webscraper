#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

const int N = 222;
int n, k;
double p[N], t[N];
double dp[N][N];

double calc(int l1, int r1, int l2, int r2) {
    int tot = 0;
    for (int i = l1; i <= r1; i++) t[++tot] = p[i];
    for (int i = l2; i <= r2; i++) t[++tot] = p[i];
    memset (dp, 0, sizeof dp);
    dp[0][0] = 1;
    for (int i = 0; i < tot; i++) {
        for (int j = 0; j <= tot; j++) {
            if (dp[i][j]) {
                dp[i + 1][j + 1] += dp[i][j] * t[i + 1];
                dp[i + 1][j] += dp[i][j] * (1 - t[i + 1]);
            }
        }
    }
    return dp[tot][tot / 2];
}

int main() {
    int T, Case = 1;
    scanf("%d", &T);
    while (T--) {
        scanf("%d%d", &n, &k);
        double res = 0;
        int ri;
        for (int i= 1; i<= n; i++) {
            scanf("%lf", &p[i]);
        }
        sort (p + 1, p + 1 + n);
        double ans = 0.0;
        for (int i = 0; i <= k; i++) {
            ans = max(ans, calc(1, i, n - (k - i) + 1, n));
        }
        printf("Case #%d: %.20f\n", Case++, ans);
    }
    return 0;
}
