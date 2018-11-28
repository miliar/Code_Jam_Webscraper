#include <bits/stdc++.h>
using namespace std;
#define sz(x) ((int) (x).size())
#define forn(i,n) for (int i = 0; i < int(n); ++i)
typedef long long ll;
typedef long long i64;
typedef long double ld;
const int inf = int(1e9) + int(1e5);
const ll infl = ll(2e18) + ll(1e10);

const int maxn = 205;
ld p[maxn];
ld pp[maxn];

ld calc(int k, int K, ld p = 1, int ch = 0) {
    if (k == K)
        return (ch == k / 2) * p;
    return calc(k + 1, K, p * pp[k], ch + 1) + calc(k + 1, K, p * (1 - pp[k]), ch);
}

ld d[maxn][maxn];
ld calc2(int k) {
    forn (i, k + 1)
        forn (j, k + 1)
            d[i][j] = 0;
    d[0][0] = 1;
    forn (i, k) {
        forn (j, k) {
            d[i + 1][j] += d[i][j] * (1 - pp[i]);
            d[i + 1][j + 1] += d[i][j] * pp[i];
        }
    }
    return d[k][k / 2];
}

bool eq(ld a, ld b) {
    return fabsl(a - b) < 1e-9;
}

ld solve2(int n, int k) {
    sort(p, p + n);
    ld best = 0;
    forn (i, n) {
        forn (len, k + 1) {
            if (i + k - len > n)
                continue;
            if (i < len)
                continue;
            forn (j, len)
                pp[j] = p[j];
            forn (j, k - len)
                pp[j + len] = p[i + j];
            ld cur = calc2(k);
            if (cur > best)
                best = cur;
        }
    }
    return best;
}

int test = 1;
ld solve(int n, int k) {
    sort(p, p + n);
    ld best = 0;
    int bmask = 0;
    forn (mask, 1 << n) {
        if (__builtin_popcount(mask) != k)
            continue;
        int c = 0;
        forn (i, n)
            if (mask & (1 << i))
                pp[c++] = p[i];
        assert(c == k);
        ld cur = calc2(k);
        if (cur > best)
            best = cur, bmask = mask;
    }
    //forn (i, n)
        //if (bmask & (1 << i))
            //cerr << '1';
        //else
            //cerr << '0';
    //cerr << '\n';
    return best;
}

int main() {
    cout << fixed;
    cout.precision(10);
    #ifdef LOCAL
    assert(freopen("b.in", "r", stdin));
    #else
    #endif
    int tn;
    cin >> tn;
    forn (i, tn) {
        int n, k;
        cin >> n >> k;
        forn (i, n)
            cin >> p[i];
        //ld res = solve(n, k);
        ld res2 = solve2(n, k);
        //cerr << res << ' ' << res2 << '\n';
        //assert(eq(res, res2));
        cout << "Case #" << test++ << ": " << res2 << '\n';
    }
}
