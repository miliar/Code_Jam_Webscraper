#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <ctime>
#include <cmath>
#include <string>
#include <iomanip>
#include <vector>
#include <set>
#include <map>
#include <cassert>
#include <queue>
#include <bitset>

using namespace std;

#define FOR(a, b) for (int a = 0; a < (b); ++a)
#define clr(a) memset(a, 0, sizeof(a))
#define pb push_back
#define forab(i, a, b) for(int i = int(a); i < int(b); ++i)
#define forba(i, b, a) for(int i = int(b) - 1; i >= int(a); --i)
#define forn(i, n) forab(i, 0, n)
#ifdef LOCAL
#define debug(a) cerr << #a << ": " << a << '\n';
#else
#define debug(a)
#endif

typedef long long ll;
typedef long double ld;

const int INF = 1e9;
const ld EPS = 1e-8;
const ld PI = acos(-1.0L);
const int MAXN = 1100;

struct point {
    int x, y, z;
    point operator + (const point & o) const {
        return {x + o.x, y + o.y,z + o.z};
    }
    point operator - (const point & o) const {
        return {x - o.x, y - o.y,z - o.z};
    }
    ld len() const {
        return sqrt(x * x + y *y + z*z);
    }
    ld distTo(const point & o) const {
        return ((*this) - o).len();
    }
    void read()  {
        cin >> x >> y >> z;
    }
};

point st[MAXN], v[MAXN];

bool used[MAXN];
int n;
void dfs(int v, ld d) {
    used[v] = true;
    forn(i, n) {
        if (used[i])
            continue;
        if (st[i].distTo(st[v]) < d) {
            dfs(i, d);
        }
    }
}

void solve() {
    int s;
    cin >> n >> s;
    forn(i, n) {
        st[i].read();
        v[i].read();
    }
    ld l = 0;
    ld r = 1e4;
    forn(_, 100) {
        ld m = (l + r) / 2;
        clr(used);
        dfs(0, m);
        if (used[1]) {
            r = m;
        } else {
            l = m;
        }
    }
    cout << fixed << setprecision(20) << r << '\n';

}

int main() {
#ifdef LOCAL
    freopen("c.in", "r", stdin);
    //freopen("", "w", stdout);
    //freopen("", "w", stderr);
#endif

    int T;
    cin >> T;
    forn(test,T) {
        cout << "Case #" << test + 1 << ": ";
        solve();
    }
    
    return 0;
}

