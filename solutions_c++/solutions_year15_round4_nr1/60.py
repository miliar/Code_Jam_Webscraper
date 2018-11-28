#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};

int T;
int n, m, ans;
char c[128][128];
int d[256];

bool check(int x, int y, int d) {
    x += dx[d];
    y += dy[d];
    while (x > 0 && x <= n && y > 0 && y <= m) {
        if (c[x][y] != '.') return true;
        x += dx[d];
        y += dy[d];
    }
    return false;
}

int main() {
    freopen("al.in", "r", stdin);
    freopen("al.out", "w", stdout);
    scanf("%d", &T);
    d['^'] = 0;
    d['>'] = 1;
    d['v'] = 2;
    d['<'] = 3;
    for (int test = 1; test <= T; test++) {
        printf("Case #%d: ", test);
        scanf("%d%d", &n, &m);
        for (int i = 1; i <= n; i++) {
            scanf("%s", c[i] + 1);
            c[i][m + 1] = '.';
        }
        ans = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (c[i][j] != '.') {
                    if (!check(i, j, d[c[i][j]])) {
                        bool flag = false;
                        for (int nd = 0; nd < 4; nd++) {
                            if (check(i, j, nd))
                                flag = true;
                        }
                        if (flag) ans++;
                        else ans = 100000;
                    }
                }
            }
        }
        if (ans >= 100000)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n", ans);
    }
    return 0;
}