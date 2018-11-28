#include <cstdio>
#define MAXN 105
int n, m;
int mp[MAXN][MAXN], mp2[MAXN][MAXN];

bool solve() {
    for (int i = 0; i < n; i++) {
        int maxn = 0;
        for (int j = 0; j < m; j++)
            if (mp[i][j] > maxn)
                maxn = mp[i][j];
        for (int j = 0; j < m; j++)
            if (mp2[i][j] > maxn)
                mp2[i][j] = maxn;
    }

    for (int j = 0; j < m; j++) {
        int maxn = 0;
        for (int i = 0; i < n; i++)
            if (mp[i][j] > maxn)
                maxn = mp[i][j];
        for (int i = 0; i < n; i++)
            if (mp2[i][j] > maxn)
                mp2[i][j] = maxn;
    }
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            if (mp[i][j] != mp2[i][j])
                return false;
    return true;
}

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++) {
                scanf("%d", &mp[i][j]);
                mp2[i][j] = 100;
            }
        if (solve()) printf("Case #%d: YES\n", cas);
        else printf("Case #%d: NO\n", cas);
    }
}