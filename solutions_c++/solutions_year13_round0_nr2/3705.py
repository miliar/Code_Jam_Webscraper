#include <cstdio>
#include <iostream>
#include <cstring>
#include <vector>
#include <cmath>
using namespace std;

#define N 101
int g[N][N];
int n, m;
bool used[N][N];

bool ok1(int x, int y)
{
    for (int i = 0; i < m; i++)
        if (!used[x][i] && g[x][i] != g[x][y])
            return false;
    return true;
}

bool ok2(int x, int y)
{
    for (int i = 0; i < n; i++)
        if (!used[i][y] && g[i][y] != g[x][y])
            return false;
    return true;
}

bool clear1(int x, int y)
{
    for (int i = 0; i < m; i++)
        used[x][i] = true;
}

bool clear2(int x, int y)
{
    for (int i = 0; i < n; i++)
        used[i][y] = true;
}

bool check()
{
    memset(used, false, sizeof (used));
    while (1)
    {
        int Min = 1000000, x, y;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                if (!used[i][j] && g[i][j] < Min)
                {
                    Min = g[i][j];
                    x = i;
                    y = j;
                }
        if (Min == 1000000)return true;
        if (ok1(x, y))
            clear1(x, y);
        else if (ok2(x, y))
            clear2(x, y);
        else return false;
    }
}

int main()
{
    freopen("D:\\data.in","r",stdin);
    freopen("D:\\data.out","w",stdout);
    int cas, t = 0;
    scanf("%d", &cas);
    while (cas--)
    {
        scanf("%d %d", &n, &m);
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                scanf("%d", &g[i][j]);
        printf("Case #%d: ", ++t);
        if (check())
            printf("YES\n");
        else
            printf("NO\n");
    }
    return 0;
}