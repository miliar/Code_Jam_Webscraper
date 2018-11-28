#include <bits/stdc++.h>

#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; i--)
#define REP(i,a) for(int i=0,_a=(a); i<_a; i++)
#define EACH(it,a) for(__typeof(a.begin()) it = a.begin(); it != a.end(); ++it)

#define DEBUG(x) { cout << #x << " = "; cout << (x) << endl; }
#define PR(a,n) { cout << #a << " = "; FOR(_,1,n) cout << a[_] << ' '; cout << endl; }
#define PR0(a,n) { cout << #a << " = "; REP(_,n) cout << a[_] << ' '; cout << endl; }

#define sqr(x) ((x) * (x))
using namespace std;

const int MN = 2000111;

int n, D;
vector<int> ke[MN];
vector<int> ls[MN];
int father[MN], value[MN];
bool chosen[MN];

int cur;

void go(int u, int l, int r) {
    ++cur;
    chosen[u] = 1;
    for(int v : ke[u]) {
        if (v == father[u]) continue;

        if (value[v] < l || r < value[v]) continue;
        go(v, l, r);
    }
}

void remove(int u) {
    --cur;
    chosen[u] = 0;
    for(int v : ke[u]) {
        if (v == father[u]) continue;

        if (chosen[v]) remove(v);
    }
}

int solve() {
    int res = 0;
    int from = max(0, value[1] - D);
    int to = from + D;

    cur = 0;
    go(1, from, to);

    res = max(res, cur);
    while (true) {
        ++from; ++to;
        if (from > value[1]) break;

        for(int u : ls[from-1]) {
            if (chosen[u]) {
                remove(u);
            }
        }
        for(int v : ls[to]) {
            if (!chosen[v] && chosen[father[v]]) {
                go(v, from, to);
            }
        }
        res = max(res, cur);
    }

    return res;
}

void init() {
    FOR(i,1,n) ke[i].clear();

    REP(i,MN) ls[i].clear();
    memset(chosen, false, sizeof chosen);
}

int S[MN], M[MN];

int main() {
    ios :: sync_with_stdio(false);
    int ntest; cin >> ntest;
    FOR(test,1,ntest) {
        cin >> n >> D;
        init();
        long long As, Cs, Rs, Am, Cm, Rm;
        cin >> S[0] >> As >> Cs >> Rs;
        cin >> M[0] >> Am >> Cm >> Rm;

        FOR(i,1,n-1) {
            S[i] = (S[i-1] * As + Cs) % Rs;
            M[i] = (M[i-1] * Am + Cm) % Rm;
        }
//        PR0(S, n);
//        PR0(M, n);

        REP(i,n) {
            int u = i + 1;
            ls[S[i]].push_back(u);
            value[u] = S[i];

            if (i == 0) continue;
            int v = (M[i] % i) + 1;

            ke[u].push_back(v);
            ke[v].push_back(u);
            father[u] = v;

//            cout << v << ' ' << u << endl;
        }
        int res = solve();
        cout << "Case #" << test << ": " << res << endl;
        cerr << test << endl;
    }
    return 0;
}

