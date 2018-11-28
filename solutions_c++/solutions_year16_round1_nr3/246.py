#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

#define MAX 1010

int n, f[MAX];
vector<int> g[MAX];
int vis[MAX], cycle[MAX];

void dfs1(int u, int r) {
    if (vis[u]) {
        if (vis[u] == r)
            cycle[u] = 1;
        return;
    }
    vis[u] = r;
    dfs1(f[u], r);
}

int dfs2(int u) {
    if (vis[u])
        return 0;
    vis[u] = 1;
    return dfs2(f[u]) + 1;
}

int dfs3(int u, int p) {
    int ret = 0;
    for (int i = 0; i < g[u].size(); i++)
        if (g[u][i] != p && !vis[g[u][i]])
            ret = max(ret, dfs3(g[u][i], u));
    return ret + 1;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d", &n);
        for (int i = 1; i <= n; i++)
            g[i].clear();
        for (int i = 1; i <= n; i++) {
            scanf("%d", &f[i]);
            g[f[i]].push_back(i);
        }
        memset(vis, 0, sizeof(vis));
        memset(cycle, 0, sizeof(cycle));
        for (int i = 1; i <= n; i++)
            if (!vis[i])
                dfs1(i, i);
        int ans = 0, sum = 0;
        memset(vis, 0, sizeof(vis));
        for (int i = 1; i <= n; i++) {
            if (f[f[i]] == i && i < f[i])
                sum += dfs3(i, f[i]) + dfs3(f[i], i);
            else if (cycle[i])
                ans = max(ans, dfs2(i));
        }
        ans = max(ans, sum);
        printf("Case #%d: %d\n", t, ans);
    }
}
