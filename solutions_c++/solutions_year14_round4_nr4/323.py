#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
char s[8][12];
int m, n, u, v, r[4], p[4], q[4][8], t[4][81][26];
void dfs(int x) {
    if (x >= m) {
        for (int i = 0 ; i < n ; ++i) if (!p[i]) return ;
        for (int i = 0 ; i < n ; ++i) r[i] = 1;
        memset(t, 0, sizeof(t));
        for (int i = 0 ; i < n ; ++i)
            for (int j = 0 ; j < p[i] ; ++j) {
                x = q[i][j];
                int y = 0;
                for (int k = 0 ; s[x][k] ; ++k)
                    if (t[i][y][s[x][k] - 'A']) y = t[i][y][s[x][k] - 'A'];
                    else y = t[i][y][s[x][k] - 'A'] = r[i]++;
            }
        int s = 0;
        for (int i = 0 ; i < n ; ++i) s += r[i];
        if (s > u) u = s, v = 1;
        else if (s == u) ++v;
        return ;
    }
    for (int i = 0 ; i < n ; ++i) {
        q[i][p[i]++] = x;
        dfs(x + 1);
        --p[i];
    }
}
int main() {
    int cas;
    freopen("1.txt", "r", stdin);
    freopen("2.txt", "w", stdout);
    scanf("%d", &cas);
    for (int c = 0 ; c < cas ; ++c) {
        scanf("%d%d", &m, &n);
        for (int i = 0 ; i < m ; ++i) scanf("%s", s[i]);
        fill(p, p + n, 0);
        u = v = 0;
        dfs(0);
        printf("Case #%d: %d %d\n", c + 1, u, v);
    }
    return 0;
}