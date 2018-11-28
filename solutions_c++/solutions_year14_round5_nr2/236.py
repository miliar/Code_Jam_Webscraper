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

map<vector<pt>, int> d;
int P, Q;

void shoot(vector<pt>& a){
    if(a.empty())
        return;
    a[0].X -= Q;
    if(a[0].X <= 0)
        a.erase(a.begin());
}

int solve(const vector<pt>& a){
    if(d.count(a))
        return d[a];
    int& ans = d[a];
    forn(i, sz(a) + 1){
        vector<pt> cur = a;
        int add = 0;
        if(i < sz(a)){
            cur[i].X -= P;
            if(cur[i].X <= 0){
                add = cur[i].Y;
                cur.erase(cur.begin() + i);
            }
        }
        shoot(cur);
        ans = max(ans, solve(cur) + add);
    }
    return ans;
}

void solve_test(){
    int n;    
    cin >> P >> Q >> n;
    vector<pt> a(n);
    forn(i, sz(a)){
        cin >> a[i].X >> a[i].Y;
    }
    d.clear();
    int ans = solve(a);
    cout << ans << endl;
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


