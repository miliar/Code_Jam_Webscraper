/* --- author: enot-the-rockstar ---*/
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <ctime>
#include <cassert>

#define fs first
#define sc second
#define pb push_back
#define mp make_pair
#define forn(i, n) for(int i = 0 ; (i) < (n) ; ++i)
#define forit(it,v) for(typeof((v).begin()) it = v.begin() ; it != (v).end() ; ++it)
#define eprintf(...) fprintf(stderr, __VA_ARGS__),fflush(stderr)
#define sz(a) ((int)(a).size())
#define all(a) (a).begin(),a.end()

static inline unsigned long long rdtsc() { unsigned long long d; __asm__ __volatile__ ("rdtsc" : "=A" (d) ); return d; }

using namespace std;

typedef long long ll;
typedef double dbl;
typedef vector<int> vi;
typedef pair<int, int> pi;

const int inf = (int)1e9;
const dbl eps = 1e-9;

/* --- main part --- */

#define TASK "a"
 
const int maxn = (int)1010;

int a[maxn];

int main()
{
    #ifdef home
        assert(freopen(TASK".in", "r", stdin));
        assert(freopen(TASK".out", "w", stdout));
    #endif
    int tn;
    scanf("%d", &tn);
    forn(tt, tn)
    {
        printf("Case #%d: ", tt + 1);
        int n;
        scanf("%d", &n);
        forn(i, n) scanf("%d", a + i);
        int res = inf;
        for (int i = 1; i <= 1000; ++i)
        {   
            int val = i;
            forn(j, n) val += (a[j] - 1) / i;
            res = min(res, val);
        }
        printf("%d\n", res);
    }
    #ifdef home
        eprintf("Time: %d ms\n", (int)(clock() * 1000. / CLOCKS_PER_SEC));
    #endif
    return 0;
}
 