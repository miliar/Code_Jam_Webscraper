#include <stdio.h>
char c[110][110];
int u[110][110];
int d[110][110];
int dx[] = {0, 1, 0, -1};
int dy[] = {1, 0, -1, 0};
int main(){
    int T, n, m, i, j, k, x, y, ri = 1;
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    while (T--) {
        scanf("%d%d", &n, &m);
        for (i = 0; i < n; i++) {
            scanf("%s", c[i]);
            for (j = 0; j < m; j++) {
                u[i][j] = 0;
                if (c[i][j] == '>') d[i][j] = 0;
                else if (c[i][j] == 'v') d[i][j] = 1;
                else if (c[i][j] == '<') d[i][j] = 2;
                else if (c[i][j] == '^') d[i][j] = 3;
                else d[i][j] = 4;
            }
        }
        int ans = 0;
        for (i = 0; i < n; i++) {
            for (j = 0; j < m; j++) {
                if (d[i][j] == 4) continue;
                k = d[i][j];
                x = i + dx[k];
                y = j + dy[k];
                while (x >= 0 && x < n && y >= 0 && y < m && d[x][y] == 4) {
                    x += dx[k];
                    y += dy[k];
                }
                if (x >= 0 && x < n && y >= 0 && y < m) continue;
                for (k = 0; k < 4; k++) {
                    x = i + dx[k];
                    y = j + dy[k];
                    while (x >= 0 && x < n && y >= 0 && y < m && d[x][y] == 4) {
                        x += dx[k];
                        y += dy[k];
                    }
                    if (x >= 0 && x < n && y >= 0 && y < m) break;
                }
                if (k < 4) ans++;
                else ans = 10000000;
            }
        }
        printf("Case #%d: ", ri++);
        if (ans < 100000) printf("%d\n", ans);
        else printf("IMPOSSIBLE\n");
    }
    return 0;
}
