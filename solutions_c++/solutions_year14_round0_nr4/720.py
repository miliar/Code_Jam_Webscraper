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

int n;

int normal(vector<ld> a, vector<ld> b){
    vector<int> used(n);
    int res = 0;
    for(int i = n - 1; i >= 0; --i){
        int idx = -1;
        forn(j, n){
            if(!used[j] && a[j] < b[i])
                idx = j;
        }
        if(idx != -1){
            res++;
            used[idx] = 1;
        }
    }
    return n - res;
}

int hack(vector<ld> a, vector<ld> b){
    vector<int> used(n);
    int res = 0, l = 0, r = sz(b) - 1;
    forn(i, sz(a)){
        if(a[i] > b[l])
            l++, res++;
        else
            r--;
    }
    return res;
}

void solve_test(){
    cin >> n;
    vector<ld> a(n), b(n);
    forn(i, n)
        cin >> a[i];
    forn(i, n)
        cin >> b[i];
    sort(all(a));
    sort(all(b));

    /*
    cout << endl;
    forn(i, sz(a))
        cout << a[i]*1000 << " ";
    cout << endl;
    forn(i, sz(b))
        cout << b[i]*1000 << " ";
    cout << endl;
    */

    int ans2 = normal(a, b);
    int ans1 = hack(a, b);
    cout << ans1 << " " << ans2 << endl;
}
int main() {
    #ifdef ssu1
    assert(freopen("input.txt", "rt", stdin));
//    freopen("output.txt", "wt", stdout);
    #endif

    int tcases;
    cin >> tcases;
    fori(i, 1, tcases){
        printf("Case #%d: ", i);
        solve_test();
//        fprintf(stderr, "-- Time for case %d = %.3lf\n\n", i, (((double)clock())/CLOCKS_PER_SEC));
    }

    return 0;
}


