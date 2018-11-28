#include <iostream>
#include <cstdio>

using namespace std;

void Work()
{
    int n, m;
    scanf("%d%d", &n, &m);
    double a[300];
    for (int i = 1; i <= n; i++) scanf("%lf", &a[i]);
    sort(a + 1, a + n + 1);
    
    double b[300];
    double f[300][300];
    double ans = 0.0;
    for (int _ = 0; _ <= m; _++)
    {
        int cnt = 0;
        for (int i = 1; i <= _; i++) b[++cnt] = a[i];
        for (int i = n - (m - _) + 1; i <= n; i++) b[++cnt] = a[i];
        //printf("cnt = %d\n", cnt);
        //for (int i = 1; i <= cnt; i++) printf("%.3f ", b[i]); printf("\n");
        
        memset(f, 0, sizeof(f));
        f[0][0] = 1.0;
        for (int i = 1; i <= m; i++)
            for (int j = 0; j <= i; j++)
            {
                f[i][j] = f[i - 1][j] * (1.0 - b[i]);
                if (j) f[i][j] += f[i - 1][j - 1] * b[i];
                //printf("f[%d][%d] = %.10f\n", i, j, f[i][j]);
            }
        //printf("ans = %.9f\n", f[m][m / 2]);
        if (f[m][m / 2] > ans) ans = f[m][m / 2];
    }
    
    printf("%.10f\n", ans);
}

int main()
{
    freopen("123.in", "r", stdin);
    freopen("123.out", "w", stdout);
    int T;
    scanf("%d", &T);
    //printf("T = %d\n", T);
    for (int i = 1; i <= T; i++)
    {
        printf("Case #%d: ", i);
        Work();
    }
    return 0;
}