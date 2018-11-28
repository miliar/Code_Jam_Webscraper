#include <bits/stdc++.h>

using namespace std;

#define sz(x) ((int) (x).size())
#define forn(i,n) for (int i = 0; i < int(n); ++i)
#define forab(i,a,b) for (int i = int(a); i < int(b); ++i)

typedef long long ll;
typedef long long i64;
typedef long double ld;

const int inf = int(1e9) + int(1e5);
const ll infl = ll(2e18) + ll(1e10);


int test = 1;
void solve() {
    ll n;
    cin >> n;
    if (n == 0) {
        printf("Case #%d: INSOMNIA\n", test++);
        return;
    }
    set<char> dig;
    ll mul = 1;
    while (sz(dig) < 10) {
        ll k = n * mul;
        ostringstream sout;
        sout << k;
        for (auto c: sout.str()) {
            dig.insert(c);
        }
        ++mul;
    }
    printf("Case #%d: %lld\n", test++, n * (mul - 1));
}

int main() {
    cout.precision(10);
    cout.setf(ios::fixed);
    #ifdef LOCAL
    assert(freopen("a.in", "r", stdin));
    #else
    #endif

    int tn;
    cin >> tn;
    forn (i, tn)
        solve();

    #ifdef LOCAL
    cerr << "Time: " << double(clock()) / CLOCKS_PER_SEC << '\n';
    #endif
}
