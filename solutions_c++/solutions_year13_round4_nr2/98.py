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

#define x first
#define y second
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


#define TASK "a"
ll calc1(int n, ll p) {
    if ((1ll << n) <= p) {
        return 1ll << n;
    }
    if ((1ll << (n - 1)) >= p) {
        return 1;
    }
    ll res = calc1(n - 1, p - (1ll << (n - 1)));
    return res * 2 + 1;
}
ll calc2(int n, ll p) {
    if ((1ll << n) <= p) {
        return 1ll << n;
    }
    if ((1ll << (n - 1)) >= p) {
        ll res = calc2(n - 1, p);
        return res * 2 - 1;
    }    
    return (1ll << n) - 1;
}

int main()
{
    #ifdef home
        assert(freopen(TASK".in", "r", stdin));
        assert(freopen(TASK".out", "w", stdout));
    #endif
    int T;
    cin>>T;
    for (int ti = 1; ti <= T; ti++) {
        printf("Case #%d: ", ti);
        ll n, p;
        cin>>n>>p;
        cout<<calc1(n, p) - 1<<" "<<calc2(n, p) - 1<<endl;
    }
    #ifdef home
        eprintf("Time: %d ms\n", (int)(clock() * 1000. / CLOCKS_PER_SEC));
    #endif
    return 0;
}
 