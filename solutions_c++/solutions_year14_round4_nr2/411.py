#include <iostream>
#include <sstream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <utility>
#include <cassert>
#include <numeric>
#include <sstream>
#include <limits>
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

template<typename T>
inline int popcount(T t) {
    if (std::numeric_limits<T>::digits <=
                            std::numeric_limits<unsigned int>::digits) {
        return __builtin_popcount(t);
    } else {
        return __builtin_popcountll(t);
    }
}

const ld EPS = 1e-8;
const ld PI = acosl(0.0) * 2;

bool isOk(const vi& p)
{
    int i = 0;
    int n = p.size();
    while (i + 1 < n && p[i + 1] > p[i]) ++i;
    while (i + 1 < n && p[i] > p[i + 1]) ++i;
    return i >= n - 1;
}

int fact[12];

int solveIt()
{
    int n;
    cin >> n;
    vi a(n);
    forn(i, n) cin >> a[i];
    int ret = 0;
    while (!a.empty()) {
        int mi = 0;
        forv(i, a) if (a[i] < a[mi]) mi = i;
        ret += min(mi, (int)a.size() - 1 - mi);
        a.erase(a.begin() + mi);
    }
    return ret;
}

void solve()
{
    fact[0] = 1;
    for1(i, 11) fact[i] = fact[i - 1] * i;
    int tc;
    cin >> tc;
    forn(it, tc) {
        cout << "Case #" << it + 1 << ": " << solveIt() << endl;
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    solve();
    return 0;
}
