#include <iostream>
#include <algorithm>
#include <string>
#include <cstdio>

using namespace std;

int a[200][200];
int n, m;

void init()
{
    scanf("%d %d", &n, &m);
    for (int i=1; i<=n; i++)
        for (int j=1; j<=m; j++)
            scanf("%d", &a[i][j]);
}

bool work()
{
    for (int i=1; i<=n; i++)
        for (int j=1; j<=m; j++)
        {
            bool cut_row = true;
            for (int k=1; k<=m; k++)
                if (a[i][k] > a[i][j])
                {
                    cut_row = false;
                    break;
                }
            bool cut_col = true;
            for (int k=1; k<=n; k++)
                if (a[k][j] > a[i][j])
                {
                    cut_col = false;
                    break;
                }
            if (!cut_row && !cut_col)
                return false;
        }
    return true;
}

int main()
{
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int tim=1; tim<=T; tim++)
    {
        init();
        bool res = work();
        if (res)
            printf("Case #%d: %s\n", tim, "YES");
        else
            printf("Case #%d: %s\n", tim, "NO");
    }
    return 0;
}
