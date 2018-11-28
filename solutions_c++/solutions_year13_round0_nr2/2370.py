#include <stdio.h>

const int maxn = 110;

int mat[maxn][maxn];
int n, m;

int main()
{
    int T, i, j, k;
    freopen("B-large.in", "r", stdin);
    //freopen("B-small-attempt0.in", "r", stdin);
    freopen("bout.txt", "w", stdout);
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++)
    {
        scanf("%d%d", &n, &m);
        for (i=1; i<=n; i++)
            for (j=1; j<=m; j++)
                scanf("%d", &mat[i][j]);
        bool ans = true;
        for (i=1; i<=n; i++) {
            for (j=1; j<=m; j++)
            {
                bool col = true, row = true;
                for (k=1; k<=n; k++)
                    if (mat[k][j] > mat[i][j]) col = false;
                for (k=1; k<=m; k++)
                    if (mat[i][k] > mat[i][j]) row = false;
                ans = col || row;
                if (!ans) break;
            }
            if (!ans) break;
        }
        if (ans) printf("Case #%d: YES\n", cas);
        else printf("Case #%d: NO\n", cas);
    }
    return 0;
}
/*
3
5 5
2 2 2 2 2
2 1 1 1 2
2 1 2 1 2
2 1 1 1 2
2 2 2 2 2

*/
