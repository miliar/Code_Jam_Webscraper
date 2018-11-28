
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

#define TWO(X) (1<<(X))
#define CONTAIN(S,X) (S & TWO(X))

const int MN = 444;
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

int m, n;
int a[22][22];
int go[22 * 22];
int hor[22][22], ver[22][22];

bool check() {
    memset(hor, 0, sizeof hor);
    memset(ver, 0, sizeof ver);
    // top
    int cur = 0;
    FOR(j,1,n) hor[1][j] = ++cur;

    // right
    FOR(i,1,m) ver[i][n+1] = ++cur;

    // bottom
    FORD(j,n,1) hor[m+1][j] = ++cur;

    // left
    FORD(i,m,1) ver[i][1] = ++cur;


    FOR(i,1,m+1) FOR(j,1,n) if (!hor[i][j]) hor[i][j] = ++cur;
    FOR(i,1,m) FOR(j,1,n+1) if (!ver[i][j]) ver[i][j] = ++cur;


    DSU dsu; dsu.init(cur);

    FOR(i,1,m) FOR(j,1,n) {
        if (a[i][j] == '/') {
            dsu.merge(hor[i][j], ver[i][j]);
            dsu.merge(hor[i+1][j], ver[i][j+1]);
        }
        else {
            dsu.merge(hor[i][j], ver[i][j+1]);
            dsu.merge(ver[i][j], hor[i+1][j]);
        }
    }

    FOR(i,1,2*(m+n)) {
        int x = dsu.getRoot(i);
        int y = dsu.getRoot(go[i]);
        if (x != y) {
            return false;
        }
    }
    return true;
}

#undef int
int main() {
#define int long long
    ios :: sync_with_stdio(0); cin.tie(0);
    cout << (fixed) << setprecision(9);
    int ntest; cin >> ntest;
    FOR(test,1,ntest) {
        cin >> m >> n;
        int bound = (m + n);
        FOR(i,1,bound) {
            int u, v; cin >> u >> v;
            go[u] = v;
            go[v] = u;
        }

        cout << "Case #" << test << ":\n";
        try {
            REP(mask,TWO(m*n)) {
                int cur = 0;
                FOR(i,1,m) FOR(j,1,n) {
                    if (CONTAIN(mask,cur)) a[i][j] = '/';
                    else a[i][j] = '\\';
                    ++cur;
                }

                if (check()) throw 1;
            }
            cout << "IMPOSSIBLE" << endl;
        } catch (...) {
            FOR(i,1,m) {
                FOR(j,1,n) cout << (char) a[i][j];
                cout << endl;
            }
        }
    }
}
