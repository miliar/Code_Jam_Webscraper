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

bool isPalindrome(ll x)
{
    std::ostringstream os;
    os << x;
    std::string s = os.str();
    for (size_t i = 0; 2 * i + 1 < s.length(); ++i) {
        if (s[i] != s[s.length() - 1]) return false;
    }
    return true;
}

void solve()
{
    int numTests; cin >> numTests;
    const int N = 10 * 1000 * 1000 + 10;
    vi numPalindromes(N);
    forn(n, N) {
        bool isFairSquare = isPalindrome(n) && isPalindrome(n * (ll)n);
        numPalindromes[n] = isFairSquare;
        if (n > 0) numPalindromes[n] += numPalindromes[n - 1]; 
    }
    for1(testId, numTests) {
        ll a, b;
        cin >> a >> b;
        int l = max(sqrt(a) - 10, 0.0);
        int r = max(sqrt(b) - 10, 0.0);
        while ((l + 1) * ll(l + 1) < a) ++l;
        while ((r + 1) * ll(r + 1) <= b) ++r;
        cout << "Case #" << testId << ": ";
        assert(l <= r);
        cout << numPalindromes[r] - numPalindromes[l] << endl;
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    solve();
    return 0;
}
