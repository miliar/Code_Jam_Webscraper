#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <utility>
#include <algorithm>
#include <cmath>
#include <map>
#include <set>
#include <memory>
#include <string.h>
#include <queue>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;

#define pb push_back
#define mp make_pair
#define sz(a) int((a).size())
#define forn(i, n) for (int i=0; i<(n); ++i)

ll one = 1;

int f(ll x) {
    int res = 0;
    forn (i, 60) if (x&(one<<i)) res = max(res, i);
    return res;
}


ll solve1(ll n, ll p) {
    ll l = 0, r = (one << n)-1;
    while (r-l > 1) {
        ll mid = (l+r) >> 1;
        int b = f(mid+1);
        ll q = (one<<b)-1;
        q <<= n-b;
        if (q < p) l = mid; else r = mid;
    }
    int b = f(r+1);
    ll q = (one<<b)-1;
    q <<= n-b;
    if (q < p) return r;
    return l;
}

ll solve2(ll n, ll p) {
    ll l = 0, r = (one<<n)-1;
    while (r-l > 1) {
        ll mid = (l+r) >> 1;
        int b = f((one<<n)-mid);
        ll q = (one<<(n-b))-1;
        if (q < p) l = mid;
        else r = mid;
    }
    int b = f((one<<n)-r);
    ll q = (one<<(n-b))-1;
    if (q < p) return r;
    return l;
}

int main()
{
    freopen("b.in", "r", stdin);
    freopen("b2.out", "w", stdout);

    int tc; scanf("%d", &tc);
    for (int tt=1; tt<=tc; ++tt) {
        ll n, p; cin >> n >> p;
        printf("Case #%d: ", tt);
        cout << solve1(n, p) << " " << solve2(n, p) << endl;
    }

    return 0;
}
