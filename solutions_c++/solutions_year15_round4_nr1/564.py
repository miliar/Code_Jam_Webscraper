#include <bits/stdc++.h>
using namespace std;

const int dx[4] = {-1, 0, 1, 0};
const int dy[4] = {0, 1, 0, -1};
int T, n, m, dir[128];
char mat[105][105];

bool inMap(int x, int y) {
    return x >= 0 && x < n && y >= 0 && y < m;
}
bool isolate(int x, int y) {
    for (int i = 0; i < n; ++i) {
        if (i == x) continue;
        if (~dir[mat[i][y]]) return false;
    }
    for (int j = 0; j < m; ++j) {
        if (j == y) continue;
        if (~dir[mat[x][j]]) return false;
    }
    return true;
}
int gao() {
    int ret = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            int d = dir[mat[i][j]];
            if (!~d) continue;
            int x = i + dx[d], y = j + dy[d];
            bool turn = false;
            while (inMap(x, y)) {
                if (~dir[mat[x][y]]) {
                    turn = true;
                    break;
                }
                x += dx[d];
                y += dy[d];
            }
            if (isolate(i, j)) return -1;
            if (!turn) ++ret;
        }
    }
    return ret;
}
int main() {
    dir['.'] = -1;
    dir['^'] = 0;
    dir['>'] = 1;
    dir['v'] = 2;
    dir['<'] = 3;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas) {
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; ++i) {
            scanf("%s", mat[i]);
        }
        int ans = gao();
        printf("Case #%d: ", cas);
        if (!~ans) puts("IMPOSSIBLE");
        else printf("%d\n", ans);
    }
}
