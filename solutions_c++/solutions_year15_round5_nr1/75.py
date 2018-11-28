#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int n, d;
int s[1 << 20];
int m[1 << 20];

vector<int> a[1 << 20];

void read() {
    int as, cs, rs;
    int am, cm, rm;

    for (int i = 0; i < (1 << 20); i++) a[i].clear();

    scanf("%d%d", &n, &d);

    scanf("%d%d%d%d", &s[0], &as, &cs, &rs);
    scanf("%d%d%d%d", &m[0], &am, &cm, &rm);

    for (int i = 1; i < n; i++) {
        s[i] = (s[i - 1] * as + cs) % rs;
        m[i] = (m[i - 1] * am + cm) % rm;

        a[ m[i] % i ].push_back(i);
    }
}


vector<int> f1, f2;

void dfs(int x, int l, int r) {
    if (s[x] < l) l = s[x];
    if (s[x] > r) r = s[x];
    if (r - l <= d) {
        f1.push_back(l);
        f2.push_back(r);
    }

    for (int i = 0; i < (int)a[x].size(); i++) {
        dfs(a[x][i], l, r);
    }
}

void solve() {
    f1.clear();
    f2.clear();
    dfs(0, s[0], s[0]);
    sort(f1.begin(), f1.end());
    sort(f2.begin(), f2.end());

    int ans = 0;
    int cur = 0;
    int j = 0;
    for (int i = 0; i < (int)f1.size(); i++) {
        while (j < (int)f2.size() && f2[j] - f1[i] <= d) {
            ++ cur;
            ++ j;
        }
        ans = max(ans, cur);
        -- cur;
    }
    printf ("%d\n", ans);
}

int main() {
    int cases;
    
    scanf("%d", &cases);
    for (int i = 1; i <= cases; i++) {
        read();
        printf ("Case #%d: ", i);
        solve();
    }
    
    return 0;
}
