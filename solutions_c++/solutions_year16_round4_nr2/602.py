#include <cstdio>
#include <algorithm>

using namespace std;

const int Maxn = 201;

double p[Maxn], f[Maxn][Maxn], a[Maxn];

double dp(double *p, int n)
{
    for (int i = 0; i <= n; ++i)
        for (int j = 0; j <= n; ++j)
            f[i][j] = 0.0;
    f[0][0] = 1.0;
    for (int i = 1; i <= n; ++i)
    {
        f[i][0] = f[i - 1][0] * (1 - p[i]);
        for (int j = 1; j <= i; ++j)
            f[i][j] = f[i - 1][j - 1] * p[i] + f[i - 1][j] * (1 - p[i]);
    }
    return f[n][n >> 1];
}

int main()
{
    int T, n, k;
    scanf("%d", &T);
    for (int tt = 1; tt <= T; ++tt)
    {
        scanf("%d%d", &n, &k);
        for (int i = 0; i < n; ++i)
            scanf("%lf", p + i);
        sort(p, p + n);
        double ans = 0.0;
        for (int i = 0; i <= k; ++i)
        {
            for (int j = 1; j <= i; ++j)
                a[j] = p[j - 1];
            for (int j = i + 1; j <= k; ++j)
                a[j] = p[n - k + j - 1];
            ans = max(ans, dp(a, k));
        }
        printf("Case #%d: %.7f\n", tt, ans);
    }
    return 0;
}
