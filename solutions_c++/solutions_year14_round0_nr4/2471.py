#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

const int N = 10;
const int dx[4] = {1, 0, -1, 0};
const int dy[4] = {0, 1, 0, -1};

int n, m, b;
int isBarrier[N][N];
int isLight[N][N], ans;

void init()
{
    for(int i = 1; i <= n; ++i) fill(isBarrier[i], isBarrier[i] + m + 1, -2);
    scanf("%d", &b);
    for(int i = 0, r, c, k; i < b; ++i)
    {
        scanf("%d %d %d", &r, &c, &k);
        isBarrier[r][c] = k;
    }
}
inline bool inRange(int r, int c)
{
    return r >= 1 && r <= n && c >= 1 && c <= m;
}
void light(int r, int c, int num)
{
    for(int i = 0; i < 4; ++i)
        for(int rr = r, cc = c; rr <= n && cc <= m; rr += dx[i], cc += dy[i])
        {
            if(isBarrier[rr][cc] != -2) break;
            if(!isLight[rr][cc]) isLight[rr][cc] = -num;
        }
}
void unLight(int r, int c, int num)
{
    for(int i = 0; i < 4; ++i)
        for(int rr = r, cc = c; rr <= n && cc <= m; rr += dx[i], cc += dy[i])
        {
            if(isBarrier[rr][cc] != -2) break;
            if(isLight[rr][cc] == -num) isLight[rr][cc] = 0;
        }
}
bool check()
{
    for(int i = 1; i <= n; ++i)
        for(int j = 1; j <= m; ++j)
        {
            if(isBarrier[i][j] == -2)
            {
                if(!isLight[i][j]) return false;
            }
            else if(isBarrier[i][j] != -1)
            {
                int cnt = 0;
                for(int k = 0; k < 4; ++k)
                {
                    int ox = i + dx[k], oy = j + dy[k];
                    if(!inRange(ox, oy)) continue;
                    if(isLight[ox][oy] > 0) cnt++;
                }
                if(cnt != isBarrier[i][j]) return false;
            }
        }
    return true;
}
bool hole(int r, int c)
{
    for(int i = 1; i < r; ++i)
        if(isBarrier[i][c] == -2 && !isLight[i][c]) return false;
    return true;
}
void dfs(int r, int c, int num)
{
    if(num >= ans) return;
    if(r == n + 1)
    {
        if(check())
            ans = min(ans, num);
        return ;
    }
    if(c == m + 1)
    {
        dfs(r + 1, 1, num);
        return ;
    }
    if(isBarrier[r][c] != -2 && !hole(r, c)) return;

    if(!isLight[r][c] && isBarrier[r][c] == -2)
    {
        isLight[r][c] = ++num;
        light(r, c, num);
        dfs(r, c + 1, num);
        isLight[r][c] = 0;
        unLight(r, c, num);
        num--;
    }
    dfs(r, c + 1, num);
}
void solve()
{
    ans = ~0U >> 1;
    memset(isLight, 0, sizeof(isLight));
    dfs(1, 1, 0);
    if(ans == ~0U >> 1) puts("No solution");
    else printf("%d\n", ans);
}
int main()
{
//    freopen("in.txt", "r", stdin);
    while(scanf("%d %d", &n, &m), n + m)
    {
        init();
        solve();
    }
    return 0;
}