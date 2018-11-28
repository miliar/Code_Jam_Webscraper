#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int t, n, m;
char str[105][105];
int vis[105][105];
const int d[4][2] = {0, 1, 1, 0, -1, 0, 0, -1};

int get(char c) {
    if (c == '>') return 0;
    if (c == '^') return 2;
    if (c == '<') return 3;
    return 1;
}

int to[4] = {2, 3, 0, 1};

bool dfs(int x, int y, int dir) {
    if (x < 0 || x >= n || y < 0 || y >= m) return true;
    if (vis[x][y] == 1) return false;
    vis[x][y] = 1;
    if (str[x][y] != '.') dir = get(str[x][y]);
    dfs(x + d[dir][0], y + d[dir][1], dir);
}

int judge() {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (vis[i][j]) continue;
            if (str[i][j] == '.') continue;
            if (dfs(i, j, 0)) return false;
        }
    }
    return true;
}

bool judge2() {
    memset(vis, 0, sizeof(vis));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (str[i][j] == '.') continue;
            int dir = get(str[i][j]);
            int x = i, y = j;
            x += d[dir][0];
            y += d[dir][1];
            int flag = 0;
            while (x >= 0 && x < n && y >= 0 && y < m) {
                if (str[x][y] != '.') {
                    vis[x][y] = vis[i][j] = 1;
                    break;
                }
                x += d[dir][0];
                y += d[dir][1];
            }
        }
    }
    for(int i = 0; i < n; i++)
        for(int j = 0; j < m; j++)
        if(str[i][j] != '.' && !vis[i][j]) return false;
        return true;
}

bool check() {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            int flag = 1;
            if (str[i][j] != '.') {
                flag = 0;
                for (int x = 0; x < n; x++) {
                    if (x != i && str[x][j] != '.') {
                        flag = 1;
                        break;
                    }
                }
                for (int y = 0; y < m; y++) {
                    if (y != j && str[i][y] != '.') {
                        flag = 1;
                        break;
                    }
                }
            }
            if (!flag) return true;
        }
    }
    return false;
}

int main() {
    int cas = 0;
    scanf("%d", &t);
    while (t--) {
        memset(vis, 0, sizeof(vis));
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; i++)
            scanf("%s", str[i]);
        printf("Case #%d: ", ++cas);
        if (check()) printf("IMPOSSIBLE\n");
        else {
            if (judge()) printf("0\n");
            else {
                if (judge2()) printf("1\n");
                else printf("2\n");
            }
        }
    }
    return 0;
}
