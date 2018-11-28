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

const int maxn = 2000;
int x0[maxn], y0[maxn], x1[maxn], y1[maxn];

int dist(int i, int j) {
    int res = 0;
    res = max(res, x0[i] - x1[j] - 1);
    res = max(res, x0[j] - x1[i] - 1);
    res = max(res, y0[i] - y1[j] - 1);
    res = max(res, y0[j] - y1[i] - 1);
    return res;
}

int main() {
#ifdef LOCAL_DEFINE
//    freopen("input.txt", "rt", stdin);
//    freopen("output.txt", "wt", stdout);
#endif

    int T;
    cin >> T;
    forn(t, T) {
        int W, H, B;
        cin >> W >> H >> B;
        x0[0] = x1[0] = -1;
        x0[B + 1] = x1[B + 1] = W;
        y0[0] = y0[B + 1] = 0;
        y1[0] = y1[B + 1] = H;
        forn(i, B) {
            cin >> x0[i + 1] >> y0[i + 1] >> x1[i + 1] >> y1[i + 1];
        }
        vi d(B + 2, 1e9);
        d[0] = 0;
        vi vis(B + 2, 0);
        while (true) {
            int m = -1;
            forn(i, B + 2) {
                if (vis[i]) continue;
                if (m == -1 || d[i] < d[m]) m = i;
            }
            if (m == -1) break;
            vis[m] = 1;
            forn(i, B + 2) {
                d[i] = min(d[i], d[m] + dist(i, m));
            }
        }
        cout << "Case #" << t + 1 << ": " << d[B + 1] << '\n';
    }

#ifdef LOCAL_DEFINE
    cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
#endif
    return 0;
}
