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


void solve()
{
    ll p, q;
    scanf("%I64d/%I64d", &p, &q);
    ll g = __gcd(p, q);
    p /= g;
    q /= g;
    int stq = 0;
    while ((1LL << stq) < q) stq += 1;
    if ((1LL << stq) != q)
    {
        printf("impossible\n");
        return;
    }
    int stp = 0;
    while ((1LL << stp) <= p) stp += 1;
    stp -= 1;
    int ans = stq - stp;
    printf("%d\n", ans);
       
}

int main()
{
    #ifdef home
        assert(freopen(TASK".in", "r", stdin));
        assert(freopen(TASK".out", "w", stdout));
    #endif
    int tn;
    scanf("%d", &tn);
    forn(i, tn)
    {
        printf("Case #%d: ", i + 1);
        solve();
    }
    #ifdef home
        eprintf("Time: %d ms\n", (int)(clock() * 1000. / CLOCKS_PER_SEC));
    #endif
    return 0;
}
 