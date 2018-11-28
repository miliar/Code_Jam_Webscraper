#include <bits/stdc++.h>

using namespace std;

#define sz(x) ((int) (x).size())
#define forn(i,n) for (int i = 0; i < int(n); ++i)
#define forab(i,a,b) for (int i = int(a); i < int(b); ++i)

typedef __int128 ll;
typedef long long i64;
typedef long double ld;

const int inf = int(1e9) + int(1e5);
const ll infl = ll(2e18) + ll(1e10);

int n = 32;
int j = 500;

const ll bound = 1000;
ll factor(ll x) {
    for (ll d = 2; d < min(bound, x); ++d) {
        if (x % d)
            continue;
        return d;
    }
    return -1;
}

int main() {
    cout.precision(10);
    cout.setf(ios::fixed);
    srand(1122);
    cout << "Case #1:\n";

    set<vector<ll>> ss;
    while (j) {
        vector<ll> v(n);
        forn (i, n)
            v[i] = rand() & 1;
        v[0] = v[n - 1] = 1;
        bool ok = true;
        vector<ll> dv;
        for (ll base = 2; base <= 10; ++base) {
            ll x = 0;
            ll c = 1;
            forn (i, n) {
                x += c * v[i];
                c *= base;
            }
            //cerr << "base " << base << ' ' << x << '\n';
            ll div = factor(x);
            if (div == -1) {
                ok = false;
                break;
            } else
                dv.push_back(div);
        }
        if (!ok) {
            //cerr << "shit\n";
            continue;
        }
        reverse(v.begin(), v.end());
        if (ss.count(v))
            continue;
        ss.insert(v);
        forn (i, n)
            cout << int(v[i]);
        for (auto num: dv)
            cout << ' ' << int(num);
        cout << '\n';
        --j;
    }

    #ifdef LOCAL
    cerr << "Time: " << double(clock()) / CLOCKS_PER_SEC << '\n';
    #endif
}
