#define _CRT_SECURE_NO_DEPRECATE
#include <algorithm>
#include <cmath>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>
#include <utility>
using namespace std;

#define fi(i,a,b) for(int i=(a);i<(b); ++i)
#define fd(i,a,b) for(int i=(a);i>(b); --i)
#define fie(i,a,b) for(int i=(a);i<=(b); ++i)
#define fde(i,a,b) for(int i=(a);i>=(b); --i)
#define mp(a,b) make_pair(a,b)
#define pb(x) push_back(x)
#define all(x) x.begin(), x.end()
#define rall(s) (s).rbegin(),(s).rend()
#define C(u) memset((u),0,sizeof((u)))
#define x first
#define y second
#define inf 1000000000
typedef unsigned int uint;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<vi > vvi;
typedef pair<int, int> pii;

#define INP_FILE "A-large.in"
#define OUT_FILE "output.txt"
struct Cnt {
    int p, r, s;
    void count(string &a) {
        p = r = s= 0;
        fi(i, 0, a.size()) {
            if (a[i] == 'P') ++p;
            if (a[i] == 'R') ++r;
            if (a[i] == 'S') ++s;
        }
    }
    bool equal(int _p, int _r, int _s) {
        return (p == _p) && (r == _r) && (s == _s);
    }
};
struct State {
    string p,r,s;
    Cnt xp, xr, xs;
};

State pc[13];

int main()
{
    freopen(INP_FILE, "r", stdin);
    freopen(OUT_FILE, "w", stdout);
    int tstCnt; cin >> tstCnt;

    pc[0].p = "P";
    pc[0].r = "R";
    pc[0].s = "S";
    pc[0].xp.count(pc[0].p);
    pc[0].xr.count(pc[0].r);
    pc[0].xs.count(pc[0].s);

    fi(i, 1, 13) {
        auto &prev = pc[i - 1];
        auto &cur = pc[i];
        cur.p = (prev.p > prev.r) ? prev.r + prev.p : prev.p + prev.r;
        cur.r = (prev.r > prev.s) ? prev.s + prev.r : prev.r + prev.s;
        cur.s = (prev.s > prev.p) ? prev.p + prev.s : prev.s + prev.p;
        cur.xp.count(cur.p);
        cur.xr.count(cur.r);
        cur.xs.count(cur.s);
    }

    for (int tst = 1; tst <= tstCnt; tst++)
    {
        int n, p, r, s; cin >> n >> r >> p >> s;
        auto &cur = pc[n];
        if (cur.xp.equal(p, r, s)) printf("Case #%d: %s\n", tst, cur.p.c_str()); else
            if (cur.xr.equal(p, r, s)) printf("Case #%d: %s\n", tst, cur.r.c_str()); else
                if (cur.xs.equal(p, r, s)) printf("Case #%d: %s\n", tst, cur.s.c_str()); else
                   printf("Case #%d: %s\n", tst, "IMPOSSIBLE");

        //printf("Case #%d: ",tst);
    }

    return 0;
}