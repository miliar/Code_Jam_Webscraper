#include <bits/stdc++.h>
using namespace std;
#define sz(x) ((int) (x).size())
#define forn(i,n) for (int i = 0; i < int(n); ++i)
typedef long long ll;
typedef long long i64;
typedef long double ld;
const int inf = int(1e9) + int(1e5);
const ll infl = ll(2e18) + ll(1e10);

//const int maxn = 26;
const int maxn = 4;
int a[maxn][maxn];
int b[maxn][maxn];

int test = 1;
void solve() {
    int n;
    cin >> n;
    char tmp[100];
    forn (i, n) {
        scanf("%s", tmp);
        forn (j, n)
            a[i][j] = tmp[j] == '1';
    }
    int res = n * n;
    forn (mask, 1 << (n * n)) {
        forn (ii, n * n) {
            b[ii / n][ii % n] = bool(mask & (1 << ii));
        }
        bool bad = false;
        int cres = 0;
        forn (i, n)
            forn (j, n) {
                if (a[i][j] && !b[i][j])
                    bad = true;
                if (b[i][j] && !a[i][j])
                    ++cres;
            }
        if (bad)
            continue;
        int p[maxn];
        forn (i, n)
            p[i] = i;
        do {
            int q[maxn];
            forn (i, n)
                q[i] = i;
            do {
                bool used[maxn];
                fill(used, used + n, false);
                forn (i, n) {
                    if (b[p[i]][q[i]]) {
                        used[q[i]] = true;
                        continue;
                    }
                    bool fail = false;
                    forn (j, n)
                        if (!used[j] && b[p[i]][j])
                            fail = true;
                    if (!fail) {
                        bad = true;
                    }
                    break;
                }
            } while (!bad && next_permutation(q, q + n));
        } while (!bad && next_permutation(p, p + n));
        if (bad)
            continue;
        res = min(res, cres);
    }
    cout << "Case #" << test++ << ": " << res << '\n';
}

int main() {
    #ifdef LOCAL
    assert(freopen("d.in", "r", stdin));
    #else
    #endif
    int tn;
    cin >> tn;
    forn (i, tn)
        solve();
}
