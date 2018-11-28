#include <bits/stdc++.h>
using namespace std;
#define sz(x) ((int) (x).size())
#define forn(i,n) for (int i = 0; i < int(n); ++i)
typedef long long ll;
typedef long long i64;
typedef long double ld;
const int inf = int(1e9) + int(1e5);
const ll infl = ll(2e18) + ll(1e10);

int test = 1;
void solve() {
    string s;
    cin >> s;
    vector<char> v;
    int res = 0;
    for (auto c: s) {
        if (!v.empty() && v.back() == c) {
            res += 10;
            v.pop_back();
        } else
            v.push_back(c);
    }
    res += v.size() / 2 * 5;
    cout << "Case #" << test++ << ": " << res << '\n';
}

int main() {
    #ifdef LOCAL
    assert(freopen("a.in", "r", stdin));
    #else
    #endif
    int tn;
    cin >> tn;
    forn (i, tn)
        solve();
}
