#include <bits/stdc++.h>
using namespace std;

int ans, p, q, n;
int h[110], g[110];

void dfs(int id, int gold, int n) {
    bool ok = true;
    int tot = 0;
    for (int i = 0; i < n; i++) {
        if (h[i] > 0) {
            ok = false;
            tot += g[i];
        }
    }
    if (ok) {
        ans = max(ans, gold);
        return;
    }
    if (gold + tot <= ans) return;
    if (id == 0) {
        for (int i = 0; i <= n; i++) {
            if (i != n) {
                if (h[i] <= 0) continue;
                h[i] -= p;
                if (h[i] <= 0) {
                    dfs(1 - id, gold + g[i], n);
                } else {
                    dfs(1 - id, gold, n);
                }
                h[i] += p;
            } else {
                dfs(1 - id, gold, n);
            }
        }
    } else {
        for (int i = 0; i < n; i++) {
            if (h[i] > 0) {
                h[i] -= q;
                dfs(1 - id, gold, n);
                h[i] += q;
                break;
            }
        }
    }
}

int main() {
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        scanf("%d%d%d", &p, &q, &n);
        for (int i = 0; i < n; i++) {
            scanf("%d%d", &h[i], &g[i]);
        }
        ans = 0;
        dfs(0, 0, n);
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
