#include <iostream>
#include <vector>
#include <cassert>
#include <cmath>
#include <ctime>
#include <cstdio>
#include <queue>
#include <set>
#include <map>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <numeric>

#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define fornn(i, a, b) for (int i = (int)(a); i < (int)(b); ++i)
#define fore(i, a, b) for (int i = (int)(a); i <= (int)(b); ++i)

using namespace std;

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;

typedef long long i64;
typedef pair<i64, i64> pi64;
typedef vector<i64> vi64;
typedef vector<vi64> vvi64;

const int maxn = 1000010;
i64 a[maxn], pr[maxn], sf[maxn];

int main() {
#ifdef LOCAL_DEFINE
//    freopen("input.txt", "rt", stdin);
//    freopen("output.txt", "wt", stdout);
#endif

    int T;
    cin >> T;
    forn(t, T) {
        int N, p, q, r, s;
        cin >> N >> p >> q >> r >> s;
        forn(i, N) {
            a[i] = (1LL * i * p + q) % r + s;
            if (N < 100) cerr << a[i] << ' ';
        }
        cerr << '\n';
        pr[0] = sf[0] = 0;
        forn(i, N) {
            pr[i + 1] = pr[i] + a[i];
            sf[i + 1] = sf[i] + a[N - i - 1];
        }
        set<i64> ps;
        ps.insert(0);
        ps.insert(1e18);
        i64 res = pr[N];
        for (int i = 1; i < N; ++i) {
            set<i64>::iterator it = ps.lower_bound((pr[i] + 1) / 2);
            i64 c = *it;
            res = min(res, max(sf[N - i], max(c, pr[i] - c)));
            if (it != ps.begin()) {
                --it;           
                c = *it;
                res = min(res, max(sf[N - i], max(c, pr[i] - c)));
            }
            ps.insert(pr[i]);
        }
        printf("Case #%d: %.10lf\n", t + 1, 1.0 - 1.0 * res / pr[N]);
    }

#ifdef LOCAL_DEFINE
    cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
#endif
    return 0;
}
