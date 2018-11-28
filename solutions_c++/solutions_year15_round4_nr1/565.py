#include <iostream>
#include <map>
#include <cstdio>
#include <cstring>

using namespace std;
int a[110][110];
int to[4][2] = {-1, 0, 1, 0, 0, -1, 0, 1};
int good[4] = {1, 0, 3, 2};
int n, m;
bool ok(int x, int y) {
    return x >= 1 && x <= n && y >= 1 && y <= m;
}
bool can[110][110][4];
bool dfs(int x, int y, int dir) {
    int nx, ny;
    nx = x + to[dir][0];
    ny = y + to[dir][1];
    if(ok(nx, ny)) {
        if(a[nx][ny] == -1) {
            bool fg = dfs(nx, ny, dir);
            return fg;
        } else {
            return 1;
        }
    }
    return 0;
}
int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T, cas = 0;
    scanf("%d", &T);
    while(T--) {
        memset(can, 0, sizeof(can));
        scanf("%d%d", &n, &m);
        char str[110];
        for(int i = 1; i <= n; i++) {
            scanf("%s", str);
            for(int j = 0; j < m; j++) {
                if(str[j] == '^') {
                    a[i][j + 1] = 0;
                } else if(str[j] == 'v') {
                    a[i][j + 1] = 1;
                } else if(str[j] == '<') {
                    a[i][j + 1] = 2;
                } else if(str[j] == '>') {
                    a[i][j + 1] = 3;
                } else {
                    a[i][j + 1] = -1;
                }
            }
        }
        bool imp = 0;
        int cnt = 0;
        for(int i = 1; i <=n ;i++) {
            for(int j = 1; j <= m; j++) {
                if(a[i][j] == -1) {
                    continue;
                }
                int tmp = a[i][j];
                bool fg = 0;
                for(int g = 0; g < 4; g++) {
                    a[i][j] = g;
                    if(dfs(i, j, g)) {
                        can[i][j][g] = 1;
                        fg = 1;
                    }
                    //cout<<i<<" "<<j<<" "<<can[i][j][g]<<endl;
                }
                a[i][j] = tmp;
                if(!fg) {
                    imp = 1;
                    break;
                } else {
                    if(can[i][j][a[i][j]]) {

                    } else {
                        cnt++;
                    }
                }
            }
        }
        printf("Case #%d: ", ++cas);
        if(imp) {
            puts("IMPOSSIBLE");
        } else {
            printf("%d\n", cnt);
        }


    }
    return 0;
}
