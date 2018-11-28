#include <cstdio>
#include <cstring>

const int MAXM = 8, MAXN = 4, MAXL = 11;

char a[MAXM][MAXL];
int cs, m, n, mx, cnt, b[MAXM], tot[MAXN], nxt[MAXN][MAXM * MAXL][26];

void dfs(int dep) {
    if (dep == m) {
        int tmp = 0;
        memset(tot, 0, sizeof tot);
        memset(nxt, 0, sizeof nxt);
        for (int i = 0; i < m; ++i)
            for (int j = 0, x = 0; a[i][j]; x = nxt[b[i]][x][a[i][j++] - 'A'])
                if (!nxt[b[i]][x][a[i][j] - 'A'])
                    nxt[b[i]][x][a[i][j] - 'A'] = ++tot[b[i]];
        for (int i = 0; i < n; ++i) {
            if (!tot[i])
                return;
            tmp += tot[i] + 1;
        }
        if (tmp > mx)
            mx = tmp, cnt = 1;
        else if (tmp == mx)
            ++cnt;
        return;
    }
    for (int i = 0; i < n; ++i) {
        b[dep] = i;
        dfs(dep + 1);
    }
}

inline void work() {
    scanf("%d%d", &m, &n);
    for (int i = 0; i < m; ++i)
        scanf("%s", a[i]);
    dfs(mx = cnt = 0);
    printf("Case #%d: %d %d\n", ++cs, mx, cnt);
}

int main() {
    int t;
    scanf("%d", &t);
    while (t--)
        work();
    return 0;
}
