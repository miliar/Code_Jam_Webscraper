#include <bits/stdc++.h>
#define int long long
#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; ++i)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; --i)
#define REP(i,a) for(int i=0,_a=(a); i < _a; ++i)

#define DEBUG(X) { cout << #X << " = " << (X) << endl; }
#define PR(A,n)  { cout << #A << " = "; FOR(_,1,n) cout << A[_] << ' '; cout << endl; }
#define PR0(A,n) { cout << #A << " = "; REP(_,n) cout << A[_] << ' '; cout << endl; }

#define sqr(x) ((x) * (x))
#define ll long long
#define __builtin_popcount __builtin_popcountll
#define SZ(x) ((int) (x).size())
using namespace std;

double safe_sqrt(double x) {
    return sqrt(max((double)0.0,x));
}
int GI(ll& x) {
    return scanf("%lld", &x);
}
const int MN = 1011;
struct DSU {
    int lab[MN];
    void init(int n) {
        REP(i,n+1) lab[i] = -1;
    }

    int getRoot(int u) {
        if (lab[u] < 0) return u;
        return lab[u] = getRoot(lab[u]);
    }

    bool merge(int u, int v) {
        u = getRoot(u); v = getRoot(v);
        if (u == v) return false;
        if (lab[u] > lab[v]) swap(u, v);
        lab[u] += lab[v];
        lab[v] = u;
        return true;
    }
};

struct Point {
    double x, y, z;

    Point() { x = y = z = 0; }
    Point(double x, double y, double z) : x(x), y(y), z(z) {}

    Point operator - (const Point& a) const {
        return Point(x-a.x, y-a.y, z-a.z);
    }

    void read() {
        cin >> x >> y >> z;
    }

    double len() {
        return sqrt(x*x + y*y + z*z);
    }
} a[1011], v[1011];

#undef int
int main() {
#define int long long
    ios :: sync_with_stdio(0); cin.tie(0);
    cout << (fixed) << setprecision(9);
    int ntest; cin >> ntest;
    FOR(test,1,ntest) {
        int n; double S;
        cin >> n >> S;
        FOR(i,1,n) {
            a[i].read(); v[i].read();
        }
        vector< pair<double, pair<int,int> > > edges;
        FOR(i,1,n) FOR(j,i+1,n) {
            edges.emplace_back((a[i] - a[j]).len(), make_pair(i, j));
        }
        sort(edges.begin(), edges.end());

        double res = 1e9;
        DSU dsu; dsu.init(n);
        for(auto e : edges) {
            dsu.merge(e.second.first, e.second.second);
            if (dsu.getRoot(1) == dsu.getRoot(2)) {
                res = e.first;
                break;
            }
        }
        cout << "Case #" << test << ": " << res << endl;
    }
}
