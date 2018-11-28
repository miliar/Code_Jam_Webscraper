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

int main() {
#ifdef LOCAL_DEFINE
#endif

    int T;
    cin >> T;
    forn(t, T) {
        int N, X;
        cin >> N >> X;
        vi a(N);
        forn(i, N) cin >> a[i];
        sort(all(a));
        int l = 0, r = N / 2 + 1;
        while (r - l > 1) {
            int m = (l + r) / 2;
            bool ok = true;
            forn(i, m) {
                ok &= a[i] + a[2 * m - i - 1] <= X;
            }
            if (ok) l = m;
            else r = m;
        }
        cout << "Case #" << t + 1 << ": " << N - l << '\n';
    }

#ifdef LOCAL_DEFINE
    cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
#endif
    return 0;
}
