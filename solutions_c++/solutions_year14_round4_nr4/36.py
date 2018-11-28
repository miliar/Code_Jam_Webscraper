#ifdef ssu1
#define _GLIBCXX_DEBUG
#endif
#undef NDEBUG

#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <bitset>
#include <sstream>

using namespace std;

#define fore(i, l, r) for(int i = int(l); i < int(r); ++i)
#define forn(i, n) fore(i, 0, n)
#define fori(i, l, r) fore(i, l, (r) + 1)
#define forit(i, a) for(typeof((a).begin()) i = (a).begin(); i != (a).end(); ++i)
#define sz(v) int((v).size())
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define mp make_pair
#define X first
#define Y second

template<typename T> inline T abs(T a){ return ((a < 0) ? -a : a); }
template<typename T> inline T sqr(T a){ return a * a; }

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const int INF = (int)1E9 + 7;
const ld EPS = 1E-9;
const ld PI = 3.1415926535897932384626433832795;

const int SMAX = 110;
const int MMAX = 1010;
const int NMAX = 110;
const int TMAX = SMAX * MMAX;
const int mod = int(1e9) + 7;

struct node{
    map<char, int> next;
    int cnt;
    node(){
        cnt = 0;
    }
};

int szt;
node t[TMAX];

void add(const string& s){
    if(szt == 0){
        t[0] = node();
        szt = 1;
    }
    int v = 0;
    forn(i, sz(s)){
        char c = s[i];
        if(t[v].next.count(c) == 0){
            int u = szt++;
            t[u] = node();
            t[v].next[c] = u;
        }
        v = t[v].next[c];
    }
    t[v].cnt++;
}

int maxd[TMAX];
pt d[TMAX];

int c[NMAX][NMAX];
int C(int n, int k){
    if(k < 0 || k > n)
        return 0;
    if(k == 0)
        return 1 % mod;
    if(c[n][k] == -1)
        c[n][k] = (C(n - 1, k) + C(n - 1, k - 1)) % mod;
    return c[n][k];
}

int process(vector<pt>& a, int n){
    int mv = 0;
    forn(i, sz(a)){
        mv = max(mv, a[i].X);
    }

    vector<int> res(n + 1);

    fori(cur, mv, n){
        int bad = 0;
        fori(emp, 1, cur - mv){
            bad = (int)((bad + C(cur, emp) * 1LL * res[cur - emp]) % mod);
        }
        res[cur] = 1;
        forn(i, sz(a)){
            res[cur] = (int)((res[cur] * 1LL * C(cur, a[i].X)) % mod);
            res[cur] = (int)((res[cur] * 1LL * a[i].Y) % mod);
        }
        res[cur] = (res[cur] - bad + mod) % mod;
    }
    return res[n];
}

int n, m;

pt calcd(int v){
    pt& ans = d[v];

    if(ans.X == -1){
        maxd[v] = t[v].cnt;
        int maxval = 0;
        vector<pt> tmp;

        if(t[v].cnt){
            tmp.pb(mp(1, 1));
        }

        for(map<char, int>::iterator it = t[v].next.begin(); it != t[v].next.end(); it++){
            int u = it->Y;
            pt cur = calcd(u);
            maxval += cur.X;
            maxd[v] = min(n, maxd[v] + maxd[u]);
            tmp.pb(mp(maxd[u], cur.Y));
        }

        maxval += maxd[v];
//        cerr << v << " " << maxd[v] << " " << maxval << endl;
/*
        cerr << maxval << " " << maxd[v] << " " << sz(tmp) << endl;
        forn(i, sz(tmp)){
            cerr << tmp[i].X << " " << tmp[i].Y << endl;
        }
        cerr << endl;
*/
        ans.X = maxval;
        ans.Y = process(tmp, maxd[v]);
//        cerr << ans.Y << endl;
    }

    return ans;
}

void solve_test(){
    cin >> m >> n;
    forn(i, szt){
        t[i].next.clear();
        t[i].cnt = 0;
    }

    szt = 0;
    forn(i, m){
        string s;
        cin >> s;
        add(s);
    }

    memset(d, -1, sizeof d);
    memset(maxd, 0, sizeof maxd);

    pt res = calcd(0);
    printf("%d %d\n", res.X, res.Y);
}

int main() {
    #ifdef ssu1
    assert(freopen("input.txt", "rt", stdin));
//    freopen("output.txt", "wt", stdout);
    #endif

    memset(c, -1, sizeof c);

    int tcases;
    cin >> tcases;
    fori(i, 1, tcases){
        printf("Case #%d: ", i);
        solve_test();
        fprintf(stderr, "-- Time for case %d = %.3lf\n\n", i, (((double)clock())/CLOCKS_PER_SEC));
    }

    return 0;
}


