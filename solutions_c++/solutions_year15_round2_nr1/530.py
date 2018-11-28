/**
 *    author:  enot.1.10, Vladimir Smykalov (enot.1.10@gmail.com)
 *    created: 02.05.2015 19:04:26       
**/
#include <bits/stdc++.h>

#define forn(i, n) for(int i = 0 ; (i) < (n) ; ++i)
#define eprintf(...) fprintf(stderr, __VA_ARGS__),fflush(stderr)

using namespace std;

typedef long long ll;
typedef double dbl;

const int inf = (int)1.01e9;
const dbl eps = 1e-9;

/** --- main part --- **/

#define TASK "a"

#define pb push_back
#define sz(a) ((int)(a).size())
#define all(a) (a).begin(),a.end()
typedef vector<int> vi;



ll halfs(ll n)
{
    vi v;
    while (n > 0)
    {
        v.pb(n % 10);
        n /= 10;
    }
    int k = sz(v);
    ll res = 1e18;
    for (int kk = 1; kk < k; ++kk)
    {
        ll first = 0;
        for (int i = kk - 1; i >= 0; --i) first = first * 10 + v[i];
        ll second = 0;
        for (int i = kk; i < k; ++i) second = second * 10 + v[i];
        ll val = first + second;
        if (second == 1) val -= 1;
        res = min(res, val);
    }
    
    return res;
}

ll solve(ll n)
{
    if (n % 10 == 0)
    {
        return solve(n - 1) + 1;
    }
    if (n < 10) return n;
    ll pw = 1;
    while (pw * 10 <= n) pw *= 10;
    return solve(pw) + halfs(n);
}

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
        ll n;
        scanf("%I64d", &n);
        ll res = solve(n);
        printf("%I64d\n", res);
    }
            
    #ifdef home
        eprintf("Time: %d ms\n", (int)(clock() * 1000. / CLOCKS_PER_SEC));
    #endif
    return 0;
}
 