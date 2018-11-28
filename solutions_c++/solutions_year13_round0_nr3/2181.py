#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <utility>
#include <algorithm>
#include <cmath>
#include <map>
#include <set>
#include <queue>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;

#define pb push_back
#define mp make_pair
#define sz(a) int((a).size())
#define forn(i, n) for (int i=0; i<(n); ++i)


const int maxn = 100005;

ll rev[maxn];
ll ten[maxn];

void init(int x) {
  static int a[32];
  int n = 0;
  int y = x;
  for (; y>0; y/=10)
      a[n++] = y%10;
  ten[x] = 1;
  rev[x] = 0;
  forn (i, n)
      ten[x] *= 10, rev[x] = rev[x]*10+a[i];
}

bool is_pal(ll x) {
    static int a[32];
    int n = 0;
    for (;x>0; x/=10)
        a[n++] = x%10;
    forn (i, n/2)
        if (a[i] != a[n-i-1])
            return false;
    return true;
}

inline bool test(ll x, ll n) {
    x *= x;
    if (x <= n && is_pal(x)) {
  //      cout << x << endl;
        return true;
    }
    return false;
}


int func(ll n) {
//    printf("func: %lld\n", n);
    int res = 0;
    for (int x=1; ; ++x) {
        ll y1 = rev[x]/10*ten[x]+x;
        if (y1*y1 > n) break;
        res += test(y1, n);
        res += test(rev[x]*ten[x]+x, n);
    }
    return res;
}

int main()
{
    freopen("c.out", "w", stdout);
    forn (i, maxn)
        init(i);
    int tc; scanf("%d", &tc);
    for (int tt=1; tt<=tc; ++tt) {
        ll a, b; cin >> a >> b;
        int res = func(b) - func(a-1);
        printf("Case #%d: %d\n", tt, res);
    }

    return 0;
}
