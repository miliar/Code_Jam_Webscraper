/* --- Author: Vladimir Smykalov, enot.1.10@gmail.com --- */
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

using namespace std;

typedef long long ll;
typedef double ld;
typedef vector<int> vi;
typedef pair<int, int> pi;

const int inf = (int)1e9;
const ld eps = 1e-9;

/* --- main part --- */

#define TASK "a"


const int maxn = (int)110;

int a[maxn], ac = 0;
inline bool pal(ll x)
{
    if(x == 0) return true;
    ac = 0;
    while(x)
    {
        a[ac++] = x % 10;
        x /= 10;
    }
    for(int i = 0 ; i < ac - 1 - i ; i++) if(a[i] != a[ac - 1 - i]) return false;
    return true;
}          

ll fair[maxn], fc = 0;

int main()
{
    #ifdef home
        assert(freopen(TASK".in", "r", stdin));
        assert(freopen(TASK".out", "w", stdout));
    #endif
    for(ll i = 1 ; i < (int)1e7 + 10 ; i++)
    {
        if(pal(i) && pal(i * i)) fair[fc++] = i * i;
    }

    int test_count;
    scanf("%d", &test_count);
    forn(test, test_count)
    {
        printf("Case #%d: ", test + 1);
        ll a, b;
        scanf("%I64d%I64d", &a, &b);
        int res = lower_bound(fair, fair + fc, b + 1) - lower_bound(fair, fair + fc, a);
        printf("%d\n", res);
    }    

    #ifdef home
        eprintf("Time: %d ms\n", (int)(clock() * 1000. / CLOCKS_PER_SEC));
    #endif
    return 0;
}
 