#include <bits/stdc++.h>

using namespace std;

float a[20], b[20];
double f[20][20][20], res;
int n, k;

void ktr()
{
    for(int i=0; i<=k; i++)
    {
        for(int j=0; j<=k/2; j++)
        {
            for(int c=0; c<=k/2; c++)
                f[i][j][c] = 0;
        }
    }
    f[0][0][0] = 1;
    for(int i=1; i<=k; i++)
    {
        for(int j=0; j<=k/2; j++)
        {
            for(int c=0; c<=k/2; c++)
            {
                if (j>0)
                    f[i][j][c] += (f[i-1][j-1][c]*b[i]);
                if (c>0)
                    f[i][j][c] += (f[i-1][j][c-1]*(1.0 - b[i]));
            }
        }
    }
    res = max(res, f[k][k/2][k/2]);
}

void duyet(int rem, int vt)
{
    if (rem == 0)
    {
        ktr();
        return;
    }
    for(int j=vt; j<=n; j++)
    {
        b[rem] = a[j];
        duyet(rem-1, j+1);
    }
}

int main()
{
    freopen("bs.in", "r", stdin);
    freopen("testBs.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int t=1; t<=T; t++)
    {
        printf("Case #%d: ", t);
        scanf("%d%d", &n, &k);
        for(int i=1; i<=n; i++)
            scanf("%f", &a[i]);
        res = 0;
        duyet(k, 1);
        printf("%.9f\n", res);
    }
    return 0;
}
