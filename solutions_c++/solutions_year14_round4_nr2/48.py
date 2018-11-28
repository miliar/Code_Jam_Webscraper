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
        int N;
        cin >> N;
        vi a(N);
        forn(i, N) cin >> a[i];
        vi b = a;
        sort(all(b));
 //    map<int, int> renum;
//        forn(i, N) renum[b[i]] = i;
//        forn(i, N) a[i] = renum[a[i]];
        int ans = 0;
        for (int i = 0; i < N; ++i) {
            int gl = 0, gr = 0;
            bool seen = false;
            for (int j = 0; j < N; ++j) {
                if (a[j] > b[i]) ++(seen ? gr : gl);
                if (a[j] == b[i]) seen = true;
            }
/*            for (int j = 0; j <= i; ++j) {
                dp[j + 1][i - j] = min(dp[j + 1][i - j], dp[j][i - j] + gl);
                dp[j][i - j + 1] = min(dp[j][i - j + 1], dp[j][i - j] + gr);
            }*/
            ans += min(gl, gr);
        }
        cout << "Case #" << t + 1 << ": " << ans << '\n';
    }

#ifdef LOCAL_DEFINE
    cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
#endif
    return 0;
}
