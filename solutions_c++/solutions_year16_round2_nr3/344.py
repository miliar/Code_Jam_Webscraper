#include <bits/stdc++.h>
#define next first
#define capacity second.first
#define div second.second
#define mp make_pair
#define int long long

using namespace std;

const int MAXV = 10003;

bool used[MAXV];
vector <pair <int, pair <int, int> > > g[MAXV];

void cadd(int u, int v, int c) {
    g[u].push_back(mp(v, mp(c, g[v].size())));
    g[v].push_back(mp(u, mp(0, g[u].size() - 1)));
}

int dfs(int v, int t, int fl) {
    if (v == t) {
        return fl;
    }
    used[v] = 1;
    for (int i = 0; i < (int) g[v].size(); i++) {
        if (!used[g[v][i].next] && g[v][i].capacity > 0) {
            int min_c = dfs(g[v][i].next, t, min(fl, g[v][i].capacity));
            if (min_c > 0) {
                g[v][i].capacity -= min_c;
                g[g[v][i].next][g[v][i].div].capacity += min_c;
                return min_c;
            }
        }
    }
    return 0;
}

int max_flow(int s, int t) {
    int ans = 0;
    while (true) {
        memset(used, 0, sizeof used);
        int flow = dfs(s, t, LLONG_MAX);
        if (!flow) {
            return ans;
        } else {
            ans += flow;
        }
    }
}

int res = 0;

void solve() {
    res = 0;
    for (int i = 0; i < MAXV; i++) {
        g[i].clear();
    }
    map <string, int> c, d;
    vector <string> a, b;
    int n;
    cin >> n;
    a.resize(n), b.resize(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i] >> b[i];
        c[a[i]] = 0;
        d[b[i]] = 0;
    }
    int cap = 1;
    int ans = 0;
    for (map <string, int>::iterator it = c.begin(); it != c.end(); it++) {
        it->second = ++cap;   
        cadd(3000, it->second, 1);
    }
    for (map <string, int>::iterator it = d.begin(); it != d.end(); it++) {
        it->second = ++cap;   
        cadd(it->second, 3001, 1);
    }
    for (int i = 0; i < n; i++) {
        cadd(c[a[i]], d[b[i]], 1);
    }
    cap -= max_flow(3000, 3001);
    res = n - cap + 1;
}

main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        solve();
        cout << "Case #" << i + 1 << ": " << res << endl;
    }
}
