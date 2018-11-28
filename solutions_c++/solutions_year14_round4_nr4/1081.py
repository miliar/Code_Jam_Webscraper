#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
using namespace std;

#define N 105
#define L 105
#define M 1005

int n;
vector < string > vs;

void init() {
    int m;
    char str[L];
    scanf("%d %d", &m, &n);
    vs.clear();
    for (int i = 0; i < m; ++i) {
        scanf("%s", str);
        vs.push_back(str);
    }
}

bool vis[M];
multiset < int > mst;
vector < string > vc[N];
int chd[M][26];

int cal(const vector < string > &vc) {
    int tot = 1;
    memset(chd, 0, sizeof(chd));
    for (auto it = vc.begin(); it != vc.end(); ++it) {
        int cur = 1;
        for (int i = 0; i < it->size(); ++i) {
            int k = (*it)[i] - 'A';
            if (!chd[cur][k]) chd[cur][k] = ++tot;
            cur = chd[cur][k];
        }
    }
    return tot;
}

int cal() {
//    for (int i = 0; i < n; ++i)
//        if (0 == vc[i].size())
//            return 0;
    int sum = 0;
    for (int i = 0; i < n; ++i)
        sum += cal(vc[i]);
    return sum;
}

void dfs(int k, int c, int p) {
    if (k == vs.size()) {
        if (c == n - 1)
            mst.insert(cal());
        return;
    }
    for (int i = p; i < vs.size(); ++i)
        if (!vis[i]) {
            vis[i] = true;
            vc[c].push_back(vs[i]);
            dfs(k + 1, c, i + 1);
            vc[c].pop_back();
            vis[i] = false;
        }
    if (vc[c].size() > 0 && c < n)
        dfs(k, c + 1, 0);
}

void solve() {
    mst.clear();
    for (int i = 0; i < n; ++i)
        vc[i].clear();
    fill(vis, vis + vs.size(), false);
    dfs(0, 0, 0);
    int ans = *mst.rbegin();
    printf("%d %d\n", ans, mst.count(ans));
}

int main() {
    freopen("D-small-attempt1.in", "r", stdin);
    freopen("D-small-attempt1.out", "w", stdout);
    int t, cas = 0;
    scanf("%d", &t);
    while (t--) {
        init();
        printf("Case #%d: ", ++cas);
        solve();
    }
    return 0;
}
