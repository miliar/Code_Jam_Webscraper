#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <sstream>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <stack>
#include <vector>
#include <cassert>

using namespace std;

#define pb push_back
#define mp make_pair
#define REP(i, n) for (int i = 0; i < (int)(n); ++i)
#define foreach(e, x) for (__typeof(x.begin()) e = x.begin(); e != x.end(); ++e)
typedef long long LL;
typedef pair<int, int> PII;

int tt;
int n, d;
int s[1000005], m[1000005];
int lo[1000001], hi[1000005];
vector<int> g[1000005];
int dep[1000005];

struct Cmp1 {
    bool operator()(const int &lhs, const int &rhs) const {
        if (lo[lhs] != lo[rhs]) return lo[lhs] < lo[rhs];
        if (dep[lhs] != dep[rhs]) return dep[lhs] > dep[rhs];
        return lhs < rhs;
    }
};

struct Cmp2 {
    bool operator()(const int &lhs, const int &rhs) const {
        if (hi[lhs] != hi[rhs]) return hi[lhs] < hi[rhs];
        return lhs < rhs;
    }
};

set<int, Cmp1> se1;
set<int, Cmp2> se2;

void readArray(int *arr) {
    int z, a, c, r;
    scanf("%d%d%d%d", &z, &a, &c, &r);
    arr[0] = z;
    for (int i = 1; i < n; ++i) {
        arr[i] = (arr[i - 1] * (LL)a + c) % r;
    }
}

void dfs(int v, int curLo, int curHi, int curDep = 0) {
    dep[v] = curDep;
    curLo = min(curLo, s[v]);
    curHi = max(curHi, s[v]);
    lo[v] = curLo;
    hi[v] = curHi;
    for (int to : g[v]) dfs(to, curLo, curHi, curDep + 1);
}

int best;

bool go(int v) {
    if (hi[v] > s[0] || lo[v] < s[0] - d) return false;
    for (int to : g[v]) if (go(to)) {

    } else {
        se2.insert(to);
    }
    if (v != 0) {
        se1.insert(v);
    }
    ++best;
    return true;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &tt);
    for (int test = 1; test <= tt; ++test) {
        printf("Case #%d: ", test);
        scanf("%d%d", &n, &d);
        readArray(s);
        readArray(m);
        for (int i = 1; i < n; ++i)
            m[i] %= i;
        REP(i, n) g[i].clear();
        for (int i = 1; i < n; ++i)
            g[m[i]].pb(i);
        dfs(0, 1e7, -1e7);
        best = 0;
        se1.clear();
        se2.clear();
        go(0);
        int cur = best;
        for (int bot = s[0] - d + 1; bot <= s[0]; ++bot) {
            int to = bot + d;
            while (!se1.empty()) {
                int v = *se1.begin();
                if (lo[v] < bot) {
                    se1.erase(se1.begin());
                    for (int u : g[v]) {
                        se2.erase(u);
                    }
                    --cur;
                } else {
                    break;
                }
            }
            while (!se2.empty()) {
                int v = *se2.begin();
                if (lo[v] < bot) {
                    se2.erase(v);
                } else if (hi[v] <= to) {
                    se2.erase(v);
                    se1.insert(v);
                    ++cur;
                    for (int u : g[v]) if (lo[u] >= bot) {
                        se2.insert(u);
                    }
                } else {
                    break;
                }
            }
            best = max(best, cur);
        }
        printf("%d\n", best);
    }
	return 0;
}
