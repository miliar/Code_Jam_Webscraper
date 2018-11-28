#include <iostream>
#include <cstring>
#include <algorithm>
#include <cstdio>
#include <queue>
#include <vector>
#include <cctype>
#include <string>

#define FOR(i, a, b) for(int i = a;i < b;++i)
using namespace std;

const int MAXN = 10005;
int T, M, N;
int H[105][105];

struct node
{
    int x, y;
    node(int _x, int _y)
    {
        x = _x;
        y = _y;
    }
};

int dir[4][2] = {1, 0, 0, 1, -1, 0, 0, -1};

bool bfs(int st_x, int st_y, int h)
{
    bool vis[105][105];
    memset(vis, 0, sizeof(vis));
    queue<node> q;
    q.push(node(st_x, st_y));
    vis[st_x][st_y] = 1;
    while(!q.empty())
    {
        int x = q.front().x;
        int y = q.front().y;
        if(x == 1 || x == N || y == 1 || y == M)
        {
            return true;
        }
        q.pop();
        for(int i = 0;i < 4;++i)
        {
            int X = x + dir[i][0];
            int Y = y + dir[i][1];
            if(vis[X][Y] || H[X][Y] > h || X < 1 || X > N || Y < 1 || Y > M)     continue;
            vis[X][Y] = 1;
            q.push(node(X, Y));
        }
    }
    return false;
}

bool solve()
{
    for(int i = 1;i <= N;++i)
    {
        for(int j = 1;j <= M;++j)
        {
            if(!bfs(i, j, H[i][j])) return false;
        }
    }
    return true;
}

int maxc[105], maxr[105];
int main()
{
    scanf("%d", &T);
    for(int t = 1;t <= T;++t)
    {
        printf("Case #%d: ", t);
        scanf("%d%d", &N, &M);
        memset(maxc, 0, sizeof(maxc));
        memset(maxr, 0, sizeof(maxr));
        for(int i = 1;i <= N;++i)
        {
            for(int j = 1;j <= M;++j)
            {
                scanf("%d", &H[i][j]);
                maxr[i] = max(maxr[i], H[i][j]);
                maxc[j] = max(maxc[j], H[i][j]);
            }
        }
        bool ok = 1;
        for(int i = 1;i <= N;++i)
        {
            for(int j = 1;j <= M;++j)
            {
                if(H[i][j] == maxr[i] || H[i][j] == maxc[j])
                {
                    continue;
                }
                else
                {
                    ok = false;
                    break;
                }
            }
        }
        if(ok)   printf("YES\n");
        else printf("NO\n");
    }
}

