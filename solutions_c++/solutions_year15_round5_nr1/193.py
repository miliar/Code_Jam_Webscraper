#include <string>
#include <vector>
#include <set>
#include <map>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <string.h>
#include <queue>
#include <cstdio>
#include <cassert>
#include <deque>
#include <stack>
#include <utility>
#include <numeric>
#include <ctime>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define fore(i, l, r) for (int i = (int)(l); i < (int)(r); i++)
#define forv(i, v) forn(i, v.size())

#define mp make_pair
#define pb push_back
#define all(v) v.begin(), v.end()

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

int n, maxd;
vector<int> s, p;
vector< vector<int> > g;
vector<bool> active;
vector<bool> inc;

int dfs1(int v) {
    if (!active[v]) return 0;
    inc[v] = true;
    int ret = 1;
    forv(i, g[v]) {
        ret += dfs1(g[v][i]);
    }
    return ret;
}

int add(int v) {
    //cerr << "+ " << v << endl;
    if (v == 0) return 0;
    active[v] = true;
    if (inc[p[v]]) return dfs1(v);
    return 0;
}

int dfs2(int v) {
    if (!inc[v]) return 0;
    int ret = 1;
    inc[v] = false;
    forv(i, g[v]) {
        ret += dfs2(g[v][i]);
    }
    return ret;
}

int remove(int v) {
    //cerr << "- " << v << endl;
    if (v == 0) return 0;
    if (!active[v]) return 0;
    active[v] = false;
    if (inc[v]) return dfs2(v);
    return 0;
}

int brute(int v, int l, int r) {
    if (s[v] < l || s[v] > r) return 0;
    int ret = 1;
    forv(i, g[v]) ret += brute(g[v][i], l, r);
    return ret;
}

void solveCase(int tc) {
    cerr << tc << endl;
    printf("Case #%d: ", tc);
    cin >> n >> maxd;
    s = vector<int>(n);
    p = vector<int>(n);
    g = vector< vector<int> >(n);
    p[0] = -1;
    ll x, a, c, r;
    cin >> x >> a >> c >> r;
    s[0] = x;
    for (int i = 1; i < n; i++) {
        x = (x * a + c) % r;
        s[i] = x;
    }
    cin >> x >> a >> c >> r;
    for (int i = 1; i < n; i++) {
        x = (x * a + c) % r;
        p[i] = x % i;
        g[p[i]].push_back(i);
    }
    //forn(i, n) s[i] = rand() % 20;
    //for (int i = 1; i <= n; i++) p[i] = rand() % i, g[p[i]].push_back(i);
    vector<pii> e(n);
    /*forn(i, n) {
        cerr << s[i] << " " << p[i] << endl;
    }*/
    forn(i, n) e[i] = mp(s[i], i);
    sort(all(e));
    active = vector<bool>(n, false);
    inc = vector<bool>(n, false);
    inc[0] = true;
    active[0] = true;
    int cnt = 1;
    int ans = 1;
    int j = 0;
    for (int i = 0; i < n; i++) {
        while (j < n && e[j].first - e[i].first <= maxd) {
            cnt += add(e[j].second);
            //cerr << cnt << endl;
            j++;
        }
        //cerr << cnt << endl;
        if (e[i].first <= s[0] && s[0] <= e[i].first + maxd) {
            ans = max(ans, cnt);
            /*
            if (cnt != brute(0, e[i].first, e[i].first + maxd)) {
                cerr << cnt << " " << brute(0, e[i].first, e[i].first + maxd) << endl;
                throw;
            }
            */
        }
        cnt -= remove(e[i].second);
        //cerr << cnt << endl;
    }
    cout << ans << endl;
}

int main() {
#ifdef NEREVAR_PROJECT
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int tc; cin >> tc;
    forn(it, tc) solveCase(it + 1);
    return 0;
}
