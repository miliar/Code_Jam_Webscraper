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

int ans;
int cnt;

vector<string> buck[10];

set<vector<string>> cache;

int calc(const vector<string>& ves)
{
    set<string> st;
    for (const string& s : ves) {
        forv(i, s) {
            st.insert(s.substr(0, i + 1));
        }
    }
    return st.size() + 1;
}

void update(int n)
{
    int cans = 0;
    forn(i, n) {
        if (buck[i].empty()) return;
        cans += calc(buck[i]);
    }
    if (cans >= ans) {
        if (cans > ans) {
            ans = cans;
            cnt = 0;
        }
        ++cnt;
    }
}

void rec(int i, int m, int n, const vector<string>& s)
{
    if (i == m) {
        update(n);
        return;
    }
    forn(j, n) {
        buck[j].pb(s[i]);
        rec(i + 1, m, n, s);
        buck[j].pop_back();
    }
}

void solveIt()
{
    int n, m;
    cin >> m >> n;
    vector<string> s(m);
    forn(i, m) cin >> s[i];
    ans = 0;
    cnt = 1;
    rec(0, m, n, s);
    cout << ans << " " << cnt << endl;
}

void solve()
{
    int tc;
    cin >> tc;
    forn(it, tc) {
        cerr << it << endl;
        cout << "Case #" << it + 1 << ": ";
        solveIt();
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    solve();
    return 0;
}
