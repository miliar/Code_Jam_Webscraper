#include <iostream>
#include <vector>
#include <cmath>
#include <ctime>
#include <cassert>
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
#define fi first
#define se second
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define for1(i, n) for (int i = 1; i <= (int)(n); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define fore(i, a, b) for (int i = (int)(a); i <= (int)(b); ++i)

using namespace std;

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef long long i64;
typedef vector<i64> vi64;
typedef vector<vi64> vvi64;

template<class T> bool uin(T &a, T b) { return a > b ? (a = b, true) : false; }
template<class T> bool uax(T &a, T b) { return a < b ? (a = b, true) : false; }

vi64 a, v;

bool exc(i64 x) {
    vi64 A = a, V = v;
    vector<pair<i64, i64> > b;
    bool neg = x < 0;
    if (x < 0) {
        reverse(all(A));
        reverse(all(V));
        forn(i, A.size()) A[i] = -A[i];
        x = -x;
    }
    if (x == 0) {
        forn(i, V.size()) {
            if (V[i] % 2) return false;
            V[i] /= 2;
        }
        v = V;
        return true;
    } else {
        ford(i, A.size()) {
            if (!V[i]) continue;
            int j = i;
            while (j >= 0 && A[j] != A[i] - x) --j;
            if (j < 0) return false;
            if (V[i] > V[j]) return false;
            b.pb(mp(A[j], V[i]));
            V[j] -= V[i];
            V[i] = 0;
        }
    }
    if (neg) forn(i, b.size()) b[i].fi = -b[i].fi;
    sort(all(b));
    a.clear(); v.clear();
    for (auto p: b) a.pb(p.fi), v.pb(p.se);
    return true;
}

map<i64, vi64> dp[70];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.precision(10);
    cout << fixed;

    int T;
    cin >> T;
    for1(tn, T) {
        cerr << tn << '\n';
        int N;
        cin >> N;
        a.resize(N);
        v.resize(N);
        forn(i, N) cin >> a[i];
        forn(i, N) cin >> v[i];
        vi64 ans;
        while (a.size() > 1 || v[0] > 1) {
            while (exc(0)) ans.pb(0);
            i64 x = a[1] - a[0];
            if (exc(x)) {
                ans.pb(x);
                continue;
            }
            x = a[a.size() - 1] - a[a.size() - 2];
            if (exc(x)) {
                ans.pb(x);
                continue;
            }
        }

        i64 t = a[0];
        sort(all(ans));

        forn(i, 70) dp[i].clear();
        dp[0][0] = vi64();
        forn(i, ans.size()) {
            for (auto w: dp[i]) {
                vi64 z = w.se;
                z.pb(ans[i]);
                if (!dp[i + 1].count(w.fi)) dp[i + 1][w.fi] = vi64(1, 1e18);
                uin(dp[i + 1][w.fi], z);
                z.pop_back();
                reverse(all(z));
                z.pb(-ans[i]);
                reverse(all(z));
                if (!dp[i + 1].count(w.fi + ans[i])) dp[i + 1][w.fi + ans[i]] = vi64(1, 1e18);
                uin(dp[i + 1][w.fi + ans[i]], z);
            }
        }

        ans = dp[ans.size()][-t];

        cout << "Case #" << tn << ":";
        for (i64 c: ans) cout << ' ' << c;
        cout << '\n';
    }

#ifdef LOCAL_DEFINE
    cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
#endif
    return 0;
}
