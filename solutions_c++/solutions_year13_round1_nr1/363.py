#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <iterator>
#include <numeric>
using namespace std;

#define rep(i, n)       rep2(i, 0, n)
#define rep2(i, m, n)   for (int i = (int)(m); i < (int)(n); ++i)

typedef long long ll;

const ll INF = 1LL << 62;

inline ll sum(ll x, ll r)
{
    ll n = 2 * x + 2 * r - 1;
    return (x > INF / n) ? INF : (x * n);
}

int main()
{
    int T;
    cin >> T;
    rep (caseno, T) {
        ll r, t;
        cin >> r >> t;
        ll lo = 1, hi = 1000000001LL;
        while (hi - lo > 1) {
            ll mid = (lo + hi) / 2;
            ((sum(mid, r) > t) ? hi : lo) = mid;
        }
        cout << "Case #" << caseno + 1 << ": " << lo << endl;
    }
}
