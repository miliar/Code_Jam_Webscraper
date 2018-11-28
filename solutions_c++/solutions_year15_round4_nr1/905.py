#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

#define MAX 105

#define U '^'
#define R '>'
#define D 'v'
#define L '<'

char dir[] = {'^', 'v', '<', '>'};
int di[] = {-1, 1, 0, 0};
int dj[] = {0, 0, -1, 1};

int n, m;
char g[MAX][MAX];
int vis[MAX][MAX];
char from[MAX][MAX];
int ans;

int valid(int i, int j) {
    return 0 <= i && i < n && 0 <= j && j < m;
}

int dfs(int i, int j, int pi, int pj, char last) {
    if (g[i][j] != '.')
        vis[i][j] = 1;
    from[i][j] = last;
    int ni = i, nj = j;
    char cur = g[i][j] != '.' ? g[i][j] : last;
    for (int k = 0; k < 4; k++)
        if (cur == dir[k])
            ni += di[k], nj += dj[k];
    if (!valid(ni, nj)) {
        if (g[i][j] != '.') {
            if (last == 0)
                return 0;
            for (int k = 0; k < 4; k++)
                if (last == dir[k])
                    g[i][j] = dir[k^1];
        }
        else {
            if (from[pi][pj] == 0)
                return 0;
            for (int k = 0; k < 4; k++)
                if (from[pi][pj] == dir[k])
                    g[pi][pj] = dir[k^1];
        }
        ans++;
        return 1;
    }
    if (vis[ni][nj])
        return 1;
    if (g[i][j] != '.')
        return dfs(ni, nj, i, j, cur);
    return dfs(ni, nj, pi, pj, cur);
}

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d %d", &n, &m);
        for (int i = 0; i < n; i++)
            scanf("%s", g[i]);
        ans = 0;
        int fail = 0;
        memset(vis, 0, sizeof(vis));
        for (int i = 0; !fail && i < n; i++) {
            for (int j = 0; !fail && j < m; j++) {
                if (!vis[i][j] && g[i][j] != '.') {
                    if (!dfs(i, j, i, j, 0)) {
                        fail = 1;
                        char cur = g[i][j];
                        for (int k = 0; k < 4; k++) {
                            if (cur != dir[k]) {
                                g[i][j] = dir[k];
                                if (dfs(i, j, i, j, 0)) {
                                    ans++;
                                    fail = 0;
                                    break;
                                }
                            }
                        }
                    }
                }
            }
        }
        if (!fail)
            printf("Case #%d: %d\n", t, ans);
        else
            printf("Case #%d: IMPOSSIBLE\n", t);
    }
}
