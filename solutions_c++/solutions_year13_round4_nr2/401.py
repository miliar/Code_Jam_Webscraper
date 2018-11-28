#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <bitset>
#include <sstream>
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

using namespace std;

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define for1(i, n) for(int i = 1; i <= int(n); ++i)
#define ford(i, n) for(int i = int(n) - 1; i >= 0; --i)
#define fore(i, l, r) for(int i = int(l); i < int(r); ++i)
#define forit(i, v) for(typeof((v).begin()) i = (v).begin(); i != (v).end(); ++i)
#define sz(v) int((v).size())
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define X first
#define Y second
#define mp make_pair
template<typename T> inline T abs(T a){ return ((a < 0) ? -a : a); }
template<typename T> inline T sqr(T a){ return a * a; }

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const int INF = (int)1E9 + 7;
const ld EPS = 1E-9;
const ld PI = 3.1415926535897932384626433832795;

li get(li n, li x){
    if(n == 1) return 0;

    li lf = x, rg = n - lf - 1;

    if(lf == 0) return 0;

    li ans = n>>1;
    lf--;

    return ans + get(n>>1, lf>>1);
}

li win(li n, li x){
    if(n == 1) return 0;

    li lf = x, rg = n - lf - 1;

    if(rg != 0){
        rg--;
        return win(n>>1, (n>>1) - (rg>>1) - 1);
    }

    return n-1;
}

int main() {
    #ifdef myproject
    freopen("input.txt", "rt", stdin);
    //freopen("output.txt", "wt", stdout);
    #endif

    int tests;
    cin >> tests;
    forn(testsit, tests){
        printf("Case #%d: ", testsit+1);

        li n, p;
        cin >> n >> p;

        assert(n <= 60);

        n = (1LL << n);

        li ans1 = 0, ans2 = 0;

        {
            li lf = -1, rg = n;
            while(rg-lf > 1){
                li mid = (lf+rg) >> 1;

                if(get(n, mid) < p)
                    lf = mid;
                else
                    rg = mid;
            }
            ans1 = lf;
        }

        {
            li lf = -1, rg = n;
            while(rg-lf > 1){
                li mid = (lf+rg) >> 1;

                if(win(n, mid) < p)
                    lf = mid;
                else
                    rg = mid;
            }
            ans2 = lf;
        }

        assert(0 <= ans1 && ans1 < n);
        assert(0 <= ans2 && ans2 < n);

        cout << ans1 << " " << ans2 << endl;
        //cerr << "testsit=" << testsit+1 << " " << clock() << endl;
    }
    return 0;
}


