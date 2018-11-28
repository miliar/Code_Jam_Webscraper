#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <iostream>
#include <queue>
#include <map>
#define FI first
#define SE second
using namespace std;
const double EPS = 1e-8;
const int MAXN = 105;
const int INF = 1111111111;
char g[MAXN][MAXN];
int  r, c;
bool flag;
int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, 1, -1};
int walk(int x0, int y0, int dir) {
    for (int i = 0; i < 3; ++i) {
        dir = (dir + i) % 4;
        int x = x0 + dx[dir];
        int y = y0 + dy[dir];
        while(x >= 0 && x < r && y >= 0 && y < c) {
            if (g[x][y] != '.') {
                return (i != 0);
            }
            x += dx[dir];
            y += dy[dir];
        }
    }
    return -1;
}
int solve() {
    flag = false;
    int ing;
    int ret = 0;
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            if (g[i][j] == '.') continue;
            if (g[i][j] == '>') {
                ing = walk(i, j, 0);
            }
            if (g[i][j] == '<') {
                ing = walk(i, j, 1);
            }
            if (g[i][j] == '^') {
                ing = walk(i, j, 2);
            }
            if (g[i][j] == 'v') {
                ing = walk(i, j, 3);
            }
            if (ing == -1) return ret;
            ret += ing;
        }
    }
    flag = true;
    return ret;
}
int main() {
    freopen("F:\\retired\\gcj2015\\in.txt","r",stdin);
    //freopen("F:\\retired\\gcj2015\\out.txt","w",stdout);
    int cas;
    int n, ans;

    scanf("%d", &cas);
    for (int ca = 1; ca <= cas; ++ca) {
        scanf("%d%d", &r, &c);
        ans = 0;
        flag = false;
        for (int i = 0; i < r; ++i) {
            scanf("%s", g[i]);
        }
        ans = solve();
        if (false == false) {
            printf("Case #%d: IMPOSSIBLE\n", ca);
        } else {
             printf("Case #%d: %d\n", ca, ans);
        }

    }
    return 0;
}
