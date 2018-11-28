#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

bool vis[108][108];
bool tvis[108][108];
int r, c, ret;
char m[108][108];
int dx[] = {-1, 1, 0, 0}, dy[] = {0, 0, -1, 1};



bool impossible(int x, int y)
{
    int tx, ty;
    for (int i = 0; i < 4; i++) {
        tx = x, ty = y;
        while (tx > 0 && ty > 0 && tx <= r && ty <= c) {
            tx += dx[i];
            ty += dy[i];
            if (tx > 0 && ty > 0 && tx <= r && ty <= c) {
            if (m[tx][ty] != 4) {
                return false;
            }
            }
        }
    }
    return true;
}

bool go2(int x, int y, int dir, int fadir) {
    tvis[x][y] = true;
    int tx = x, ty = y;
    while (tx > 0 && ty > 0 && tx <= r && ty <= c) {
        tx += dx[dir];
        ty += dy[dir];
        if (tx > 0 && ty > 0 && tx <= r && ty <= c) {
        if (m[tx][ty] != 4) {
            if (tvis[tx][ty] == true) {
                vis[tx][ty] = true;
                return true;
            } else {
                if (go2(tx, ty, m[tx][ty], dir) == true) {
                    vis[tx][ty] = true;
                    return true;
                }
            }
        }
        }
    }
    m[x][y] = fadir ^ 1;
    ret++;
    tvis[x][y] = false;
    return true;
}


bool go(int x, int y, int dir) {
    tvis[x][y] = true;
    int tx = x, ty = y;
    while (tx > 0 && ty > 0 && tx <= r && ty <= c) {
        tx += dx[dir];
        ty += dy[dir];
        if (tx > 0 && ty > 0 && tx <= r && ty <= c) {
        if (m[tx][ty] != 4) {
            if (tvis[tx][ty] == true) {
                vis[tx][ty] = true;
                return true;
            } else {
                if (go2(tx, ty, m[tx][ty], dir) == true) {
                    vis[tx][ty] = true;
                    return true;
                }
            }
        }
        }
    }
    tvis[x][y] = false;
    return false;
}


int work()
{
    memset(vis, 0, sizeof vis);
    memset(tvis, 0, sizeof tvis);
    ret = 0;
    scanf("%d%d", &r, &c);
    for (int i = 1; i <=r; i++) {
        scanf("%s", m[i] + 1);
        for (int j = 1; j <= c; j++) {
            if (m[i][j] == '.') {
                m[i][j] = 4;
            } else if (m[i][j] == '^') {
                m[i][j] = 0;
            } else if (m[i][j] == 'v') {
                m[i][j] = 1;
            } else if (m[i][j] == '<') {
                m[i][j] = 2;
            } else if (m[i][j] == '>') {
                m[i][j] = 3;
            }
            // assert(m[i][j] <= 4);
        }
    }
    for (int i = 1; i <= r; i++) {
        for (int j = 1; j <= c; j++) {
            if (m[i][j] != 4 && !vis[i][j]) {
                if (impossible(i, j)) {
                    return -1;
                }
                bool flag = false;
                if (go(i, j, m[i][j]) == false) {
                    ret++;
                    for (int k = 1; k < 4; k++) {
                        if (go(i, j, (m[i][j] + k) % 4) == true) {
                            flag = true;
                        }
                    }
                    if (flag == true) {
//                      ret++;
                    }
                }
            }
        }
    }
    return ret;
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; i++) {
        printf("Case #%d: ", i);
        int ret = work();
        if (ret == -1) {
            printf("IMPOSSIBLE\n");
        } else {
            printf("%d\n", ret);
        }
    }
    return 0;
}