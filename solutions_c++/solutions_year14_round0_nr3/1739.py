#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

int dx[8] = {-1, -1, -1, 0, 0, 1, 1, 1};
int dy[8] = {-1, 0, 1, -1, 1, -1, 0, 1};
int T, R, C;
int M;
char map[12][12];
bool vis[12][12];
int ansr, ansc;

void clk(int i, int j) {
    vis[i][j] = 1;
    int cnt = 0;
    for (int k = 0; k < 8; ++k) {
        int ni = i+dx[k], nj = j+dy[k];
        if (map[ni][nj]=='*') cnt++;
    }
    if (cnt==0) {
        for (int k = 0; k < 8; ++k) {
            int ni = i+dx[k], nj = j+dy[k];
            if (!vis[ni][nj] && map[ni][nj]=='.') clk(ni, nj);
        }
    }
}

bool check_clk(int r, int c) {
    memset(vis, 0, sizeof vis);
    int i, j;
    for (j = 0; j <= C+1; ++j) {
        vis[0][j] = vis[R+1][j] = 1;
    }
    for (i = 0; i <= R+1; ++i) {
        vis[i][0] = vis[i][C+1] = 1;
    }
    clk(r, c);
    for (i = 1; i <= R; ++i)
        for (j = 1; j <= C; ++j)
            if (map[i][j]=='.' && !vis[i][j]) return false;
    ansr = r; ansc = c;
    return true;
}

bool check() {
    int i, j;
    for (i = 1; i <= R; ++i) {
        for (j = 1; j <= C; ++j) {
            if (map[i][j]=='.' && check_clk(i, j)) return true;
        }
    }
    return false;
}

bool fill(int r, int c) {
    if (r==R+1) return check();
    if (c==C+1) return fill(r+1, 1);
    if (M>0) {
        map[r][c] = '*';
        M--;
        if (fill(r, c+1)) return true;
        M++;
    }
    if (M<(R-r)*C+C-c+1) {
        map[r][c] = '.';
        if (fill(r, c+1)) return true;
    }
    return false;
}

int main() {
    cin>>T;
    int i, j, k;
    for (int t = 1; t <= T; ++t) {
        cin>>R>>C>>M;
        ansr = ansc = 0;
        memset(map, '.', sizeof map);
        printf("Case #%d:\n", t);
        if (fill(1, 1)) {
            for (i = 1; i <= R; ++i) {
                for (j = 1; j <= C; ++j) {
                    if (i==ansr && j==ansc)
                        putchar('c');
                    else
                        printf("%c", map[i][j]);
                }
                puts("");
            }
        } else {
            puts("Impossible");
        }
    }
    return 0;
}
