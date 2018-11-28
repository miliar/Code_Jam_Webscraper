#include <cstdio>
const int MAXN = 100, MAXM = 100;
int n, m, a[MAXN][MAXM];
bool possible()
{
    int i, p, j, b[MAXN][MAXM];
    for(i = 0; i < n; i++)
    {
        p = a[i][0];
        for(j = 1; j < m; j++)
            if(p < a[i][j])
                p = a[i][j];
        for(j = 0; j < m; j++)
            b[i][j] = p;
    }
    for(i = 0; i < m; i++)
    {
        p = a[0][i];
        for(j = 1; j < n; j++)
            if(p < a[j][i])
                p = a[j][i];
        for(j = 0; j < n; j++)
            if(b[j][i] > p)
                b[j][i] = p;
    }
    for(i = 0; i < n; i++)
        for(j = 0; j < m; j++)
            if(a[i][j] != b[i][j])
                return false;
    return true;
}
int main()
{
    int t, i, j, k;
    FILE *fin = fopen("Lawnmower.in", "r"), *fout = fopen("Lawnmower.out", "w");
    fscanf(fin, "%d", &t);
    for(i = 1; i <= t; i++)
    {
        fscanf(fin, "%d%d", &n, &m);
        for(j = 0; j < n; j++)
            for(k = 0; k < m; k++)
                fscanf(fin, "%d", &a[j][k]);
        if(possible())
            fprintf(fout, "Case #%d: YES\n", i);
        else
            fprintf(fout, "Case #%d: NO\n", i);
    }
    return 0;
}
