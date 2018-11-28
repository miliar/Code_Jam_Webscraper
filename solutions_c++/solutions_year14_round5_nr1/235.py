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

li sum(vector<li>& s, int l, int r){
    return s[r] - (l == 0 ? 0 : s[l - 1]);
}

bool can(const vector<li>& a, li x){
    forn(i, sz(a))
        if(a[i] > x)
            return false;

    li sum = a[0];
    int cnt = 1;

    fore(i, 1, sz(a)){
        if(sum + a[i] <= x){
            sum += a[i];
        }else{
            sum = a[i];
            cnt++;
        }
    }
    return cnt <= 3;
}

void solve_test(){
    int n, pp, q, rr, ss;
    cin >> n >> pp >> q >> rr >> ss;
    vector<li> a(n), s(n);
    forn(i, n){
        a[i] = (i * li(pp) + q) % rr + ss;
    }
    forn(i, n){
        s[i] = a[i];
        if(i > 0)
            s[i] += s[i - 1];
    }

//    cerr << a[0] << endl;

    li lf = 0, rg = 1e18;
    while(rg - lf > 1){
        li mid = (lf + rg) >> 1;
        if(can(a, mid))
            rg = mid;
        else
            lf = mid;
    }
//    cerr << rg << endl;

    ld p = 1 - (rg / ld(sum(s, 0, n - 1)));
    printf("%.20lf\n", double(p));
}

int main(int argc, char* argv[]) {
    #ifdef ssu1
    const char* filename = argc >= 2 ? argv[1] : "input.txt";
    assert(freopen(filename, "r", stdin));
    #endif

    int tcases;
    cin >> tcases;
    fori(i, 1, tcases){
        printf("Case #%d: ", i);
        solve_test();
        fprintf(stderr, "-- Time for case %d = %.3lf\n\n", i, (((double)clock())/CLOCKS_PER_SEC));
    }

    return 0;
}


