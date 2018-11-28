#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <ctype.h>
#include <limits.h>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <stack>
#include <set>
#include <bitset>
#define CLR(a) memset(a, 0, sizeof(a))
#define REP(i, a, b) for(int i = a;i < b;i++)
#define REP_D(i, a, b) for(int i = a;i <= b;i++)

typedef long long ll;

using namespace std;

const int maxn = 1e2 +10;
int dx[10] = {-1, 0, 1, 0}, dy[10] = {0, 1, 0, -1};
char a[maxn][maxn];
int dir[maxn][maxn];
int vis[maxn][maxn][10];
int ans[maxn][maxn][10];
int n, m;
int anss;
int flag;

int dfs_for(int x, int y, int direct)
{
    if(x < 1 || x > n || y < 1 || y > m)
        return 0;
    if(vis[x][y][direct])
    {
        return ans[x][y][direct];
    }
    vis[x][y][direct] = 1;
    if(a[x][y] == '.')
    {
        ans[x][y][direct] = dfs_for(x + dx[direct], y+dy[direct],direct);
        return ans[x][y][direct];
    }
    else
    {
        return 1;
    }
}

int dfs(int x, int y, int direct)
{
    if(dfs_for(x + dx[direct],y+dy[direct],direct))
    {
        return 1;
    }
    anss++;
    for(int i = 0; i <= 3; i++)
    {
        if(i != dir[x][y])
        {
            if(dfs_for(x + dx[i],y+dy[i],i))
            {
                return 1;
            }
        }
    }
    return 0;

//    if(x < 1 || x > n || y < 1 || y > m)
//        return 0;
//    if(vis[x][y][direct])
//    {
//        return ans[x][y][direct];
//    }
//    vis[x][y][direct] = 1;
//    if(a[x][y] == '.')
//    {
//        ans[x][y][direct] = dfs_for(x + dx[direct], y+dy[direct],direct);
//        return ans[x][y][direct];
//    }
//    int res = 0;
//    if(dfs_for(x + dx[dir[x][y]],y+dy[dir[x][y]],dir[x][y]))
//    {
//        res = 1;
//    }
//    else
//    {
//        anss++;
//        for(int i = 0; i <= 3; i++)
//        {
//            if(i != dir[x][y])
//            {
//                if(dfs_for(x + dx[i],y+dy[i],i))
//                {
//                    res = 1;
//                    break;
//                }
//            }
//        }
//    }
//    ans[x][y][direct] = res;
//    if(res == 0)
//        flag = 0;
//    return res;
}

int solve()
{
    CLR(vis);
    anss = 0;
    flag = 1;
    for(int i = 1; i <= n; i++)
    {
        for(int j = 1; j <= m; j++)
        {
            if(a[i][j]=='.')
            {
                ;
            }
            else
            {
                if(dfs(i, j, dir[i][j]) == 0)
                {
                    flag = 0;
                    return -1;
                }
            }
        }
    }
    return anss;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("1111lllnewAout.txt", "w", stdout);
    int ncase;
    scanf("%d", &ncase);
    REP_D(_, 1, ncase)
    {
        printf("Case #%d: ", _);
        scanf("%d%d", &n, &m);
        REP_D(i, 1, n)
        {
            scanf("%s", a[i] + 1);
        }
        REP_D(i, 1, n)
        {
            REP_D(j, 1, m)
            {
                int x = i, y = j;
                if(a[i][j] == '^')
                {
                    dir[x][y] = 0;
                }
                else if(a[i][j] == '>')
                {
                    dir[x][y] = 1;
                }
                else if(a[i][j] == 'v')
                {
                    dir[x][y] = 2;
                }
                else if(a[i][j] == '<')
                {
                    dir[x][y] = 3;
                }
            }
        }
        int t = solve();
        if(t == -1)
        {
            printf("IMPOSSIBLE\n");
        }
        else
        {
            printf("%d\n", t);
        }
    }
    return 0;
}
