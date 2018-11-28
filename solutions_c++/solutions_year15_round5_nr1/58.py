#include <bits/stdc++.h>
using namespace std;

vector<int> g[1000010];
int l[1000010], r[1000010], d;
int sum[1000010];
int s[1000010], m[1000010];

void dfs(int u, int vL, int vR) {
    l[u] = max(vL, s[u] - d);
    r[u] = min(vR, s[u]);
    //printf("l[%d] = %d, r[%d] = %d\n", u, l[u], u, r[u]);
    if (l[u] <= r[u]) {
        sum[l[u]]++;
        sum[r[u] + 1]--;
    }
    for (auto v : g[u]) {
        dfs(v, l[u], r[u]);
    }
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        memset(sum, 0, sizeof(sum));
        int n;
        scanf("%d%d", &n, &d);
        int am, cm, rm;
        int as, cs, rs;
        scanf("%d%d%d%d", &s[0], &as, &cs, &rs);
        scanf("%d%d%d%d", &m[0], &am, &cm, &rm);
        for (int i = 0; i < n; i++) {
            g[i].clear();
        }
        for (int i = 1; i < n; i++) {
            s[i] = ((long long)s[i - 1] * as % rs + cs) % rs;
            //printf("%d\n", s[i]);
            m[i] = ((long long)m[i - 1] * am % rm + cm) % rm;
            //printf("%d %d\n", m[i] % i, i);
            g[m[i] % i].push_back(i);
        }
        dfs(0, 0, 1000000);
        int cur = 0, res = 0;
        for (int i = 0; i <= 1000000; i++) {
            cur += sum[i];
            if (i <= s[0] && i + d >= s[0]) {
                res = max(res, cur);
            }
        }
        printf("Case #%d: %d\n", cas, res);
        fprintf(stderr, "%d: %d\n", cas, res);
    }
    return 0;
}