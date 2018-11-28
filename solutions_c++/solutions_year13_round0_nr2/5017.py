#include <cstdio>

int grass[11][11];
int t, cas = 1;
int m, n;

bool check(int x, int y)
{
    bool ret = true;
    for (int i = 0; i < m; i ++)
        if (grass[i][y] == 2)
        {
            ret = false;
            break;
        }
    if (ret) return true;
    ret = true;
    for (int j = 0; j < n; j ++)
        if (grass[x][j] == 2)
        {
            ret = false;
            break;
        }
    return ret;
}

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    scanf("%d", &t);
    while (t --)
    {
        scanf("%d %d", &m, &n);
        for (int i = 0; i < m; i ++)
            for (int j = 0; j < n; j ++)
                scanf("%d", &grass[i][j]);
        bool flag = true;
        for (int i = 0; i < m && flag; i ++)
            for (int j = 0; j < n && flag; j ++)
                if (grass[i][j] == 1 && !check(i, j ))
                {
                    flag = false;
                }
        printf("Case #%d: ", cas ++);
        if (flag)
            printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
/*
3
3 3
2 1 2
1 1 1
2 1 2
5 5
2 2 2 2 2
2 1 1 1 2
2 1 2 1 2
2 1 1 1 2
2 2 2 2 2
1 3
1 2 1
*/
