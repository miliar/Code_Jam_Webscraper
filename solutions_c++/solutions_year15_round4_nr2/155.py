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

const ldb INF = 1e15L;
const ldb EPS = 1e-10;
const ldb PI = acos(-1.0);
const int MAXN = 210;

struct source {
    ldb t;
    ldb s;
};

bool operator < (source a, source b) {
    return a.t < b.t;
}
source s[MAXN];

int n;
ldb v, x;

int main() {
#ifdef LOCAL
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    //freopen("", "w", stderr);
#endif
    int T;
    cin >> T;
    FOR(t, T) {
        cin >> n >> v >> x;
        ldb sum = 0;
        ldb sumv = 0;
        FOR(i, n) {
            ldb r, c;
            cin >> r >> c;
            s[i].t = c - x;
            s[i].s = r / v;
            sum += s[i].t * s[i].s;
            sumv += s[i].s;
        }
        if (sum < 0) {
            FOR(i, n)
                s[i].t *= -1;
        }

        sort(s, s + n);
        cout << "Case #" << t + 1 << ": ";
        if (s[0].t > EPS) {
            cout << "IMPOSSIBLE\n";
            continue;
        }
        ldb left = 1.0 / sumv;
        ldb right = INF;
        FOR (it, 120) {
            ldb mid = (left + right) / 2;
            ldb a = 0;
            ldb v = 0;
            FOR(i, n) {
                ldb cv = 0;
                if (v + s[i].s * mid > 1.0) {
                    cv = 1.0 - v;
                } else {
                    cv = s[i].s * mid;
                }
                a += cv * s[i].t;
                v += cv;
            }
            if (a > 0) {
                left = mid;
            } else {
                right = mid;
            }
        }
        assert (left < INF / 10);
        cout << fixed << setprecision(10) << double(left) << '\n';
    }
    return 0;
}

