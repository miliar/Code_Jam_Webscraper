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

const int maxn = 110;

ll x[maxn];

int main()
{
    #ifdef home
        assert(freopen(TASK".in", "r", stdin));
        assert(freopen(TASK".out", "w", stdout));
    #endif
    int tn;
    scanf("%d", &tn);
    x[37] = (ll)1e18;
    forn(_, tn)
    {
        printf("Case #%d: ", _ + 1);
        forn(i, 37) x[i] = 0;
        ll B;
        int n;
        scanf("%I64d%d", &B, &n);
        forn(i, n) scanf("%I64d", &x[i]);
        sort(x, x + 37);
        double res = 0;
        for(int k1 = 1 ; k1 <= 37 ; k1++)
        {
            for(int k2 = 0 ; k2 <= 37 - k1 ; k2 ++)
            {
                ll s = x[k1 + k2 - 1];
                if(x[k1 - 1] == s) s += 1;
                if(x[k1 + k2 - 1] == x[k1 + k2]) continue;
                ll b = 0;
                forn(i, k1 + k2)
                {
                    b += s - x[i];
                    if(i < k1) b -= 1;
                }
                if(b > B) continue;
                double total = 0;
                forn(i, k1) total += 36 * (s - 1 - x[i]) - b;
                total = total * 1. / k1;
                res = max(res, total);
                if(k1 + k2 >= 36) continue;
                ll t = min(x[k1 + k2] - s - 1, (B - b) / (k1 + k2));
                total += 36 * t - (k1 + k2) * t;
                res = max(res, total); 
            }
        }
        printf("%.18lf\n", res);
    }
                

    #ifdef home
        eprintf("Time: %d ms\n", (int)(clock() * 1000. / CLOCKS_PER_SEC));
    #endif
    return 0;
}
 