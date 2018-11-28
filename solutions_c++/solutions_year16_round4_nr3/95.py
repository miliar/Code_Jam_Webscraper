/**
 * Copyright © 2016 Authors. All rights reserved.
 * 
 * FileName: C.cpp
 * Author: Beiyu Li <sysulby@gmail.com>
 * Date: 2016-05-28
 */
#include <bits/stdc++.h>

using namespace std;

#define rep(i,n) for (int i = 0; i < (n); ++i)
#define For(i,s,t) for (int i = (s); i <= (t); ++i)
#define foreach(i,c) for (__typeof(c.begin()) i = c.begin(); i != c.end(); ++i)

typedef long long LL;
typedef pair<int, int> Pii;

const int inf = 0x3f3f3f3f;
const LL infLL = 0x3f3f3f3f3f3f3f3fLL;

const int maxn = 16 + 5;

int r, c;
char g[maxn][maxn];
int cp[maxn*2][2];
int vis[maxn][maxn][2];
map<char, int> dir[2], side[4];
int dx[] = {0, -1, 0, 1}, dy[] = {-1, 0, 1, 0};

bool inside (int x, int y) { return 1 <= x && x <= r && 1 <= y && y <= c; }

void get_pos(int id, int &x, int &y, int &o)
{
        if (id <= c) x = 1, y = id, o = (g[x][y] == '\\');
        else if (id <= r + c) x = id - c, y = c, o = 1;
        else if (id <= r + 2 * c) x = r, y = r + 2 * c - id + 1, o = (g[x][y] == '/');
        else x = 2 * (r + c) - id + 1, y = 1, o = 0;
}

bool flood_fill(int x, int y, int o, int c)
{
        if (~vis[x][y][o] && vis[x][y][o] != c) return false;
        vis[x][y][o] = c;
        int d = dir[o][g[x][y]];
        rep(i,2) {
                int nx = x + dx[d], ny = y + dy[d];
                if (inside(nx, ny)) {
                        int no = side[d][g[nx][ny]];
                        if (vis[nx][ny][no] == -1) {
                                if (!flood_fill(nx, ny, no, c)) return false;
                        } else if (vis[nx][ny][no] != c) {
                                return false;
                        }
                }
                d = (d + 1) % 4;
        }
        return true;
}

bool check()
{
        int x, y, o;
        memset(vis, -1, sizeof(vis));
        rep(i,r+c) {
                get_pos(cp[i][0], x, y, o);
                if (!flood_fill(x, y, o, i)) return false;
                get_pos(cp[i][1], x, y, o);
                if (vis[x][y][o] != i) return false;
        }
        return true;
}

bool dfs(int x, int y)
{
        if (x > r) {
                if (check()) {
                        For(i,1,r) {
                                For(j,1,c) putchar(g[i][j]);
                                puts("");
                        }
                        return true;
                }
                return false;
        }
        g[x][y] = '/';
        if (dfs(y == c? x + 1: x, y == c? 1: y + 1)) return true;
        g[x][y] = '\\';
        return dfs(y == c? x + 1: x, y == c? 1: y + 1);
}

int main()
{
        int T, cas = 0;
        scanf("%d", &T);

        dir[0]['/'] = 0, dir[1]['\\'] = 1, dir[1]['/'] = 2, dir[0]['\\'] = 3;
        side[0]['/'] = 1, side[0]['\\'] = 1;
        side[1]['/'] = 1, side[1]['\\'] = 0;
        side[2]['/'] = 0, side[2]['\\'] = 0;
        side[3]['/'] = 0, side[3]['\\'] = 1;
        while (T--) {
                scanf("%d%d", &r, &c);
                rep(i,r+c) scanf("%d%d", &cp[i][0], &cp[i][1]);
                printf("Case #%d:\n", ++cas);
                if (!dfs(1, 1)) puts("IMPOSSIBLE");
        }

        return 0;
}
