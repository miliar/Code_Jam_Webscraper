#include <cstdio>
#include <cstring>

double p[20], a[20];
double f[20][20];

double DP(int k) {
   // for (int i = 0; i < k; i++) printf("%lf ", a[i]); puts("");
    memset(f, 0, sizeof(f));
    f[0][0] = 1.0;
    for (int i = 1; i <= k; i++)
        for (int j = 0; j <= k / 2; j++) {
            f[i][j] = f[i - 1][j] * (1.0 - a[i - 1]);
            if (j > 0) f[i][j] += f[i - 1][j - 1] * a[i - 1];
            //printf("f[%d][%d] = %f\n", i, j, f[i][j]);
        }
    return f[k][k / 2];
}

int main() {
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        int n, k;
        scanf("%d%d", &n, &k);
        for (int i = 0; i < n; i++)
            scanf("%lf", &p[i]);
        double ans = 0;
        for (int st = 0; st < (1 << n); st++) {
            int t = 0;
            for (int i = 0; i < n; i++)
                if ((st >> i) & 1) a[t++] = p[i];
            if (t != k) continue;
            double cur = DP(k);
            if (cur > ans) ans = cur;
        }
        printf("Case #%d: %.8lf\n", cas, ans);
    }
    return 0;
}
