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
const int MAXN = 1100;

int b[MAXN];
int l[MAXN];
int h[MAXN];
int a[MAXN];

int main() {
#ifdef LOCAL
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    //freopen("", "w", stderr);
#endif
     
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        debug(test);
        int n, k;
        cin >> n >> k;
        FOR(i, n - k + 1) {
            cin >> b[i];
        }
        FOR(i, k) {
            a[i] = 0;
            l[i] =0;
            h[i] = 0;
        }
        for (int i = k; i < n; ++i) {
            a[i] = a[i - k] + b[i - k + 1] - b[i - k];
            l[i % k] = min(l[i % k], a[i]);
            h[i % k] = max(h[i % k], a[i]);
        }
        int d;
        int mn = 0;
        FOR(i, k) {
            if (h[i] - l[i] > h[mn] - l[mn])
                mn = i;
        }
        swap(h[0], h[mn]);
        swap(l[0], l[mn]);

        for (d = h[0] - l[0];; ++d) {
            int mn = 0;
            int mx = 0;
            bool flag = true;
            for (int i = 1; i < k; ++i) {
                int cl = h[0] - d - l[i];
                int cr = l[0] + d - h[i];
                if (cl > cr) {
                    flag = false;
                    break;
                }
                mn += cl;
                mx += cr;
            }
            if (!flag)
                continue;
//            cerr << d << ' ' << mn << ' ' << mx << '\n';
            for (int i = mn; i <= mx; ++i) {
                if (((i % k + k) % k) == ((b[0] % k + k) % k)) {
                    flag = false;
                    break;
                }
            }
            if (!flag)
                break;
        }
        printf("Case #%d: %d\n", test, d);
    }
    return 0;
}

