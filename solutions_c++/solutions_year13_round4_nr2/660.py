#include <iostream>
#include <sstream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <utility>
#include <cassert>
#include <numeric>
#include <sstream>
using namespace std;

#define REQUIRE(cond, message) \
    do { \
        if (!(cond)) { \
            std::cerr << message << std::endl; \
            assert(false); \
        } \
    } while (false)

#define forn(i, n) for (int i = 0; i < int(n); ++i)
#define for1(i, n) for (int i = 1; i <= int(n); ++i)
#define forv(i, v) forn(i, (v).size())
#define pb push_back
#define mp make_pair
#define all(v) (v).begin(), (v).end()

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef long long ll;
typedef vector<ll> vl;
typedef pair<int, int> pii;
typedef vector<string> vs;
typedef long double ld;

ll maxCan(ll n, ll p)
{
    ll l = 0, r = 1ll << n;
    ll N = 1ll << n;
    while (l + 1 < r) {
        ll k = (l + r + 1) / 2;
        ll s = 0;
        while ((1ll << (s + 1)) <= N - k) ++s;
        assert((1ll << s) <= N - k);
        assert(s <= N);
        if ((1ll << (n - s)) <= p) {
            l = k;
        } else {
            r = k - 1;
        }
    }
    return l;
}

ll maxMust(ll n, ll p)
{
    ll l = 0, r = 1ll << n;
    while (l + 1 < r) {
        ll k = (l + r + 1) / 2;
        ll s = 0;
        while ((1ll << (s + 1)) <= k + 1) ++s;
        assert(s <= n);
        assert((1ll << s) <= k + 1);
        ll above = ((1ll << s) - 1) * ((1 << (n - s)));
        if (above  + 1<= p) {
            l = k;
        } else {
            r = k - 1;
        }
    }
    return l;
}

void solve()
{
    int numTests; cin >> numTests;
    for1(testId, numTests) {
        int n, p;
        cin >> n >> p;
        cout << "Case #" << testId << ":";
        cout << " " << maxMust(n, p) << " " << maxCan(n, p) << endl;
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    solve();
    return 0;
}
