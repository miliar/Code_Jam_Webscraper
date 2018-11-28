#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int n, m;
int g[111][111];
bool OK(int a, int b)
{
    int i, j, pr = 0, pc = 0;
    for(i = a + 1; i < n; i ++)
        if(g[i][b] > g[a][b]) {pr = 1; break;}
    for(i = a - 1; i >= 0; i --)
        if(g[i][b] > g[a][b]) {pr = 1; break;}
    for(j = b + 1; j < m; j ++)
        if(g[a][j] > g[a][b]) {pc = 1; break;}
    for(j = b - 1; j >= 0; j --)
        if(g[a][j] > g[a][b]) {pc = 1; break;}
    return !pr || !pc;
}

bool Judge()
{
    int i, j;
    for(i = 0; i < n; i ++)
        for(j = 0; j < m; j ++)
            if(!OK(i, j)) return false;
    return true;
}
int main()
{
    int t, i, j, ca;
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    for(scanf("%d", &t), ca = 1; ca <= t; ca ++)
    {
        scanf("%d%d", &n, &m);
        for(i = 0; i < n; i ++)
            for(j = 0; j < m; j ++)
                scanf("%d", &g[i][j]);
        printf("Case #%d: ", ca);
        printf(Judge() ? "YES\n" : "NO\n");
    }
    return 0;
}
