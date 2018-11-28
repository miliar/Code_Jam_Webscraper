#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <memory>
#include <cassert>
#include <climits>
using namespace std;

#define FOR(i, a, b) for(int (i) = (a); (i) <= (b); (i)++)
#define FORD(i, a, b) for(int (i) = (a); (i) >= (b); (i)--)
#define REP(i, n) for (int (i) = 0; (i) < n; (i)++)
#define SIZE(a) (int)(a).size()
#define ALL(a) (a).begin(), (a).end()

typedef long long LL;
typedef vector<pair<int, int> > vpii;

#define DBG(x) cout << #x << " = " << x << endl
// #define DBG(x) ;

template<typename T>
void dbg_vector(const vector<T>& v, const string& name) {
    cout << name << " = ";
    REP(i, SIZE(v)) {
        cout << v[i] << ' ';
    }
    cout << endl;
}

LL MOD = 1000002013;

LL f(LL N, LL n) {
    return n * (N * 2 - n + 1) / 2;
}

struct TPass {
    LL o;
    LL e;
    int p;

    TPass() {}
    TPass(LL _o, LL _e, int _p): o(_o), e(_e), p(_p) {}
};

bool pass_less(const TPass& a, const TPass& b) {
    if (a.o != b.o) return a.o < b.o;
    if (a.e != b.e) return a.e < b.e;
    return a.p < b.p;
}

void read(TPass& p) {
    cin >> p.o >> p.e >> p.p;
}

LL cost(LL N, const vector<TPass>& oe) {
    LL res = 0;
    REP(i, SIZE(oe)) {
        LL c = f(N, oe[i].e - oe[i].o);
        c %= MOD;
        c *= oe[i].p;
        c %= MOD;
        res += c;
        res %= MOD;
    }
    return res % MOD;
}

typedef map< pair<LL, LL>, int> hm;

void add_hm(hm& n, const TPass& oe) {
    hm::iterator it = n.find(make_pair(oe.o, oe.e));
    if (it == n.end()) {
        n[make_pair(oe.o, oe.e)] = oe.p;
    } else {
        it->second += oe.p;
    }
}

void dbg_oe(const vector<TPass>& oe, const string& msg) {
    cout << msg << endl;
    REP(i, SIZE(oe)) {
        cout << oe[i].o << " -> " << oe[i].e << " *" << oe[i].p << endl;
    }
}

void dbg_pass(const TPass& p, const string& msg) {
    cout << msg << ": " << p.o << " -> " << p.e << " *" << p.p << endl;
}

void copy_hm(hm& n, vector<TPass>& oe) {
    for (size_t i = 0; i < oe.size(); ++i) {
        if (oe[i].p > 0) {
            add_hm(n, oe[i]);
        }
    }
    oe.clear();
    for (hm::const_iterator it = n.begin(); it != n.end(); ++it) {
        LL e = it->first.first;
        LL o = it->first.second;
        int p = it->second;
        if (p > 0 && e != o) {
            oe.push_back(TPass(e, o, p));
        }
    }
    // dbg_oe(oe, "after_copy_hm");
}

bool ok(const TPass& _a, const TPass& _b) {
    if (_a.p == 0 || _b.p == 0) return false;
    if (_a.e == _a.o || _b.e == _b.o) return false;
    TPass a, b;
    if (pass_less(_a, _b)) {
        a = _a;
        b = _b;
    } else {
        a = _b;
        b = _a;
    }
    if (b.o > a.o && b.e > a.e && b.o <= a.e) {
        return true;
    }
    return false;
}

void do_swap(TPass& a, TPass& b, hm& n) {
    int p = min(a.p, b.p);
    a.p -= p;
    b.p -= p;
    TPass n1(min(a.o, b.o), max(a.e, b.e), p);
    TPass n2(max(a.o, b.o), min(a.e, b.e), p);
    add_hm(n, n1);
    add_hm(n, n2);
}

LL doit(LL N, vector<TPass>& oe) {
    LL orig = cost(N, oe);
    LL res;
    bool ops = false;
    hm n;
    int iter = 0;
    while (true) {
        ops = false;
        n.clear();

        REP(i, SIZE(oe)) if (oe[i].p != 0) {
            FOR(j, i + 1, SIZE(oe) - 1) {
                if (ok(oe[i], oe[j])) {
                    do_swap(oe[i], oe[j], n);
                    ops = true;
                }
                if (oe[i].p == 0) break;
            }
        }

        copy_hm(n, oe);
        n.clear();
        if (!ops) break;
        if (++iter > 1000) break;
    }
    LL dest = cost(N, oe);
    // DBG(dest);
    return (orig + MOD - dest) % MOD;
}

int main() {
    int tests;
    cin >> tests;
    REP(zzz, tests) {
        LL N, M;
        cin >> N >> M;
        vector<TPass> oe(M);
        REP(i, M) read(oe[i]);
        // DBG(SIZE(oe));
        LL res = doit(N, oe);
        oe.clear();
        cout << "Case #" << zzz + 1 << ": " << res << endl;
    }

    /*
    REP(N, 100) REP(o1, N) FOR(e1, o1 + 1, N - 1) FOR(o2, o1, e1) FOR(e2, max(o2, e1), N - 1) if (o1 != e1 && o2 != e2) {
        LL n1 = o1 - e1;
        LL n2 = o2 - e2;
        LL orig = f(N, n1) + f(N, n2);
        LL chng = f(N, o2 - e1) + f(N, o1 - e2);
        if (chng > orig) {
            cout << N << ' ' << o1 << ' ' << e1 << ' ' << o2 << ' ' << e2 << '\n';
        }
    }
    */

    return 0;
}
