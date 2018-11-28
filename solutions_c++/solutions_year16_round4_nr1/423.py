#include <iostream>
#include <cstdio>

using namespace std;

void Work()
{
    int n, m;
    scanf("%d%d", &n, &m);
    double a[300];
    for (int i = 0; i < n; i++) scanf("%lf", &a[i]);
    sort(a, a + n);
    
    double b[300];
    int cnt = 0;
    for (int i = 0, j = n - 1, k = 0; k < m / 2; i++, j--, k++)
    {
        b[++cnt] = a[i];
        b[++cnt] = a[j];
    }
    //for (int i = 1; i <= m; i++) printf("%.5f ", b[i]); printf("\n");
    //cnt = m;
    
    double f[300][300];
    memset(f, 0, sizeof(f));
    f[0][0] = 1.0;
    for (int i = 1; i <= m; i++)
        for (int j = 0; j <= i; j++)
        {
            f[i][j] = f[i - 1][j] * (1.0 - b[i]);
            if (j) f[i][j] += f[i - 1][j - 1] * b[i];
            //printf("f[%d][%d] = %.10f\n", i, j, f[i][j]);
        }
    printf("%.10f\n", f[m][m / 2]);
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