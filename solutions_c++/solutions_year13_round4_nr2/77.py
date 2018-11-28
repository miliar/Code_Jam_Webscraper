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


int main()
{
    #ifdef home
        assert(freopen(TASK".in", "r", stdin));
        assert(freopen(TASK".out", "w", stdout));
    #endif
    int tn;
    scanf("%d", &tn);
    forn(_, tn)
    {
        printf("Case #%d: ", _ + 1);
        ll n, p;
        scanf("%I64d%I64d", &n, &p);
        if(p == 1LL << n)
        {
            printf("%I64d %I64d\n", (1LL << n) - 1, (1LL << n) - 1);
            continue;
        }
        int k = 0;
        while(p - 1 >= (1LL << n) - (1LL << (n - k))) k += 1;
        ll X = (1LL << k) - 2;
        k = 0;
        while(p >= (1LL << k)) k += 1;
        k -= 1;
        ll Y = (1LL << n) - (1LL << (n - k));
        printf("%I64d %I64d\n", X, Y);
    }         
    #ifdef home
        eprintf("Time: %d ms\n", (int)(clock() * 1000. / CLOCKS_PER_SEC));
    #endif
    return 0;
}
 