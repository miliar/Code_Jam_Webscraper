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

const int N = 2010;

int n;
vector<int> a, as;

int pos[N];
int z[N][N];

int main() {
    #ifdef ssu1
    assert(freopen("input.txt", "rt", stdin));
    #endif
    
    int tests;
    cin >> tests;
    
    forn(test, tests) {
        assert(scanf("%d", &n) == 1);
        
        a.resize(n);
        forn(i, n) 
            assert(scanf("%d", &a[i]) == 1);
            
        as = a;
        sort(all(as));
        forn(i, n)
            a[i] = (int) (lower_bound(all(as), a[i]) - as.begin());

        forn(i, n + 1)
            forn(j, n + 1)
                z[i][j] = n * n;
                
        z[0][0] = 0;            

        for (int lc = 0; lc < n; ++lc) {
            forn(i, sz(a))
                pos[a[i]] = i;
                
            for (int lf = 0; lf <= lc; ++lf) {
                int rg = lc - lf;
                
                z[lf + 1][rg] = min(z[lf + 1][rg], z[lf][rg] + pos[lc]);
                z[lf][rg + 1] = min(z[lf][rg + 1], z[lf][rg] + sz(a) - pos[lc] - 1);
            }
            
            a.erase(a.begin() + pos[lc]);                            
        }

        int ans = n * n;
        forn(c, n)
            ans = min(ans, z[c][n - c]);        
        
        printf("Case #%d: %d\n", test + 1, ans);
    }

 
    return 0;
}

