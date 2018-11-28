#undef NDEBUG
#ifdef ssu1
#define _GLIBCXX_DEBUG
#endif

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

const int N = 100500;

int n, x;
int a[N];

int main() {
    #ifdef ssu1
    assert(freopen("input.txt", "rt", stdin));
    #endif

    int tests;
    cin >> tests;
    
    forn(test, tests) {
        assert(scanf("%d %d", &n, &x) == 2);
        
        forn(i, n)
            assert(scanf("%d", &a[i]) == 1);
            
        sort(a, a + n);
        
        int ans = 0;
        int lf = 0;
        for (int rg = n - 1; rg >= lf;) {
            if (rg == lf) {
                ans++;
                break;
            }
            
            if (a[rg] + a[lf] <= x) {
                ans++;
                lf++;
                rg--;
            } else {
                ans++;
                rg--;
            }                
        }
        
        printf("Case #%d: %d\n", test + 1, ans);
    }
 
    return 0;
}

