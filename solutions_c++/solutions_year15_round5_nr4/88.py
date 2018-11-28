#include <cassert>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <ctime>
#include <cmath>
#include <string>
#include <iomanip>
#include <vector>
#include <set>
#include <map>
#include <cassert>
#include <queue>

using namespace std;

#define FOR(a, b) for (int a = 0; a < (b); ++a)
#define clr(a) memset(a, 0, sizeof(a))
#define pb(i) push_back(i)
#define forab(i, a, b) for(int i = int(a); i < int(b); ++i)
#define forba(i, b, a) for(int i = int(b) - 1; i >= int(a); --i)
#define forn(i, n) forab(i, 0, n)
#ifdef LOCAL
#define debug(a) cerr << #a << ": " << a << '\n';
#else
#define debug(a)
#endif

typedef long long ll;
typedef long double ldb;

const int INF = 1e9;
const ldb EPS = 1e-8;
const ldb PI = acos(-1.0);
const int MAXN = 2e6;
ll e[MAXN];
ll f[MAXN];
ll a[MAXN];

int main() {
#ifdef LOCAL
    freopen("d.in", "r", stdin);
    freopen("d.out", "w", stdout);
    //freopen("", "w", stderr);
#endif
     
    int T;
//    T = 10;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        debug(test);
        int p;
        multiset<ll> s;
        /*
        FOR(i, 1 << 20) {
            ll sum = 0;
            FOR(j, 20) {
                if (i & (1 << j))
                    sum += (j + 1);
            }
            s.insert(sum);
        }
        */
        cin >> p;
        FOR(i, p) {
            cin >> e[i];
        }
        FOR(i, p) {
            cin >> f[i];
        }
        FOR(i, p) {
            FOR(j, f[i])
                s.insert(e[i]);
        }
        int m = s.size();
        int n = 0;
        while (m > 1) {
            m >>= 1;
            n++;
        }
        /*
        for (auto i : s) {
            cerr << i << ' ';
        }
        cerr << '\n';*/
        s.erase(s.find(0));
        FOR(i, n) {
        //    debug(i);
            a[i] = *s.begin();
            FOR(j, 1 << i) {
                ll sum = a[i];
                FOR(k, i) {
                    if (j & (1 << k))
                        sum += a[k];
                }
        //        debug(sum);
                s.erase(s.find(sum));
          //      cerr << "!!\n";
            }
        }
        assert(s.size() == 0);
        printf("Case #%d: ", test);
        FOR(i, n) {
            printf("%lld ", a[i]);
        }
        printf("\n");
    }
    return 0;
}

