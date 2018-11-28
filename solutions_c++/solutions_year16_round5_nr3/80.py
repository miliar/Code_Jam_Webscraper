#include <bits/stdc++.h>
using namespace std;
#define sz(x) ((int) (x).size())
#define forn(i,n) for (int i = 0; i < int(n); ++i)
typedef long long ll;
typedef long long i64;
typedef long double ld;
const int inf = int(1e9) + int(1e5);
const ll infl = ll(2e18) + ll(1e10);

struct pt {
    ld x, y, z;

    pt operator-(const pt &p) const {
        return pt{x - p.x, y - p.y, z - p.z};
    }

    ld abs() const {
        return sqrtl(x * x + y * y + z * z);
    }
};

istream &operator>>(istream &in, pt &p) {
    return in >> p.x >> p.y >> p.z;
}

const int maxn = 1005;
pt p[maxn], v[maxn];

namespace dsu {

int col[maxn];

int get(int u) {
    if (u == col[u])
        return u;
    return col[u] = get(col[u]);
}

void join(int u, int v) {
    u = get(u), v = get(v);
    col[u] = v;
}

void init(int n) {
    forn (i, n)
        col[i] = i;
}

};

int test = 1;
void solve() {
    int n, s;
    cin >> n >> s;
    forn (i, n) {
        cin >> p[i] >> v[i];
        if (v[i].abs() != 0)
            cerr << "TEST " << test << '\n';
    }
    dsu::init(n);
    vector<pair<ld, pair<int, int>>> V;
    forn (i, n)
        forn (j, i) {
            V.emplace_back((p[i] - p[j]).abs(), pair<int, int>{i, j});
        }
    sort(V.begin(), V.end());
    ld res = 0;
    for (auto v: V) {
        dsu::join(v.second.first, v.second.second);
        if (dsu::get(0) == dsu::get(1)) {
            res = v.first;
            break;
        }
    }
    cout << "Case #" << test++ << ": " << res << '\n';
}

int main() {
    cout << fixed;
    cout.precision(10);
    #ifdef LOCAL
    assert(freopen("c.in", "r", stdin));
    #else
    #endif
    int tn;
    cin >> tn;
    forn (i, tn)
        solve();
}
