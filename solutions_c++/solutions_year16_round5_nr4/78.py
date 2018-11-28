#include <bits/stdc++.h>
using namespace std;
#define sz(x) ((int) (x).size())
#define forn(i,n) for (int i = 0; i < int(n); ++i)
typedef long long ll;
typedef long long i64;
typedef long double ld;
const int inf = int(1e9) + int(1e5);
const ll infl = ll(2e18) + ll(1e10);

const int maxn = 250;
string g[maxn];
string b;

int test = 1;
void solve() {
    int n, l;
    cin >> n >> l;
    forn (i, n)
        cin >> g[i];
    cin >> b;
    cout << "Case #" << test++ << ": ";
    forn (i, n) {
        if (b == g[i]) {
            cout << "IMPOSSIBLE\n";
            return;
        }
    }
    forn (i, l)
        cout << "0?";
    cout << ' ';
    forn (i, l - 1)
        cout << "01";
    cout << 0 << '\n';
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
