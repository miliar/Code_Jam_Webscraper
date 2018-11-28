#include <bits/stdc++.h>
using namespace std;
const int MAXN = 105;
const int DIR_X[4] = {1, 0, -1, 0};
const int DIR_Y[4] = {0, 1, 0, -1};

int a[MAXN];
char b[MAXN][MAXN];

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int T, R, C;
    scanf("%d", &T);
    a['^'] = 2;
    a['v'] = 0;
    a['<'] = 3;
    a['>'] = 1;
    for (int t = 1; t <= T; ++t) {
        scanf("%d%d", &R, &C);
        map<int, int> h, v;
        for (int i = 0; i < R; ++i) {
            scanf("%s", b[i]);
            for (int j = 0; j < C; ++j) {
                if (b[i][j] != '.') {
                    ++h[i];
                    ++v[j];
                }
            }
        }
        bool flag = true;
        int cnt = 0;
        for (int i = 0; i < R and flag; ++i) {
            for (int j = 0; j < C; ++j) {
                if (b[i][j] != '.') {
                    int dx = DIR_X[a[b[i][j]]];
                    int dy = DIR_Y[a[b[i][j]]];
                    int tx = i;
                    int ty = j;
                    bool isBad = false;
                    while (true) {
                        tx += dx;
                        ty += dy;
                        if (tx < 0 or tx >= R) {
                            isBad = true;
                            break;
                        }
                        if (ty < 0 or ty >= C) {
                            isBad = true;
                            break;
                        }
                        if (b[tx][ty] != '.') {
                            break;
                        }
                    }
                    if (isBad) {
                        ++cnt;
                        if (h[i] == 1 and v[j] == 1) {
                            flag = false;
                            break;
                        }
                    }
                }
            }
        }
        printf("Case #%d: ", t);
        if (flag) {
            printf("%d\n", cnt);
        } else {
            puts("IMPOSSIBLE");
        }
    }
    return 0;
}
