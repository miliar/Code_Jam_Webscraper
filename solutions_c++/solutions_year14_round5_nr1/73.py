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

const int N = 2000100;

int n;
li a[N], sum[N];

inline li getSum(int lf, int rg) {
    if (lf > rg)
        return 0;        
    return sum[rg] - ((lf == 0) ? 0 : sum[lf - 1]);
}

int main() {
    #ifdef ssu1
    assert(freopen("input.txt", "rt", stdin));
    #endif

    int tests;
    cin >> tests;
    
    forn(test, tests) {
        li p, q, r, s;
        cin >> n >> p >> q >> r >> s;
        
        forn(i, n) {
            a[i] = (i * p + q) % r + s;
            sum[i] = a[i];
            if (i > 0)
                sum[i] += sum[i - 1];
        }    
        
        li ans = 0;
        
        for (int x = 0; x < n; ++x) {
            int lf = x;
            int rg = n - 1;
            
            while (rg - lf > 10) {
                int mid = (lf + rg) >> 1;
                
                if (getSum(x, mid) > getSum(mid + 1, n - 1))
                    rg = mid;
                else
                    lf = mid;
            }            
            
            for (int mid = lf; mid <= rg; ++mid) {
                li cur = getSum(0, x - 1);
                cur = max(cur, max(getSum(x, mid), getSum(mid + 1, n - 1)));
                
                ans = max(ans, getSum(0, n - 1) - cur);
            }
        }     
        
        //cerr << ans << " " << getSum(0, n - 1) << endl;           
        
        printf("Case #%d: ", test + 1);
        cout.precision(10);
        cout << fixed << ld(ans) / ld(getSum(0, n - 1)) << endl;
    }
 
    return 0;
}

