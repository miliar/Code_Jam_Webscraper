#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cfloat>
#include <ctime>
#include <cassert>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <numeric>
#include <list>
#include <iomanip>
#include <fstream>
#include <bitset>

using namespace std;

#define foreach(it, c) for (__typeof__((c).begin()) it=(c).begin(); it != (c).end(); ++it)
template <typename T> void print_container(ostream& os, const T& c) { const char* _s = " "; if (!c.empty()) { __typeof__(c.begin()) last = --c.end(); foreach (it, c) { os << *it; if (it != last) os << _s; } } }
template <typename T> ostream& operator<<(ostream& os, const vector<T>& c) { print_container(os, c); return os; }
template <typename T> ostream& operator<<(ostream& os, const set<T>& c) { print_container(os, c); return os; }
template <typename T> ostream& operator<<(ostream& os, const multiset<T>& c) { print_container(os, c); return os; }
template <typename T> ostream& operator<<(ostream& os, const deque<T>& c) { print_container(os, c); return os; }
template <typename T, typename U> ostream& operator<<(ostream& os, const map<T, U>& c) { print_container(os, c); return os; }
template <typename T, typename U> ostream& operator<<(ostream& os, const pair<T, U>& p) { os << "(" << p.first << ", " << p.second << ")"; return os; }

template <typename T> void print(T a, int n, const string& split = " ") { for (int i = 0; i < n; i++) { cout << a[i]; if (i + 1 != n) cout << split; } cout << endl; }
template <typename T> void print2d(T a, int w, int h, int width = -1, int br = 0) { for (int i = 0; i < h; ++i) { for (int j = 0; j < w; ++j) { if (width != -1) cout.width(width); cout << a[i][j] << ' '; } cout << endl; } while (br--) cout << endl; }
template <typename T> void input(T& a, int n) { for (int i = 0; i < n; ++i) cin >> a[i]; }
#define dump(v) (cout << #v << ": " << v << endl)

#define rep(i, n) for (int i = 0; i < (int)(n); ++i)
#define erep(i, n) for (int i = 0; i <= (int)(n); ++i)
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define clr(a, x) memset(a, x, sizeof(a))
#define sz(a) ((int)(a).size())
#define mp(a, b) make_pair(a, b)
#define ten(n) ((long long)(1e##n))

template <typename T, typename U> void upmin(T& a, const U& b) { a = min<T>(a, b); }
template <typename T, typename U> void upmax(T& a, const U& b) { a = max<T>(a, b); }
template <typename T> void uniq(T& a) { sort(a.begin(), a.end()); a.erase(unique(a.begin(), a.end()), a.end()); }
template <class T> string to_s(const T& a) { ostringstream os; os << a; return os.str(); }
template <class T> T to_T(const string& s) { istringstream is(s); T res; is >> res; return res; }
void fast_io() { cin.tie(0); ios::sync_with_stdio(false); }
bool in_rect(int x, int y, int w, int h) { return 0 <= x && x < w && 0 <= y && y < h; }

typedef long long ll;
typedef pair<int, int> pint;

const int dx[] = { 0, 1, 0, -1 };
const int dy[] = { 1, 0, -1, 0 };


template<class T, size_t ...sizes> struct ArrayHelper;
template<class T> struct ArrayHelper<T>{ using type = T; };
template<class T, size_t s, size_t ...ss> struct ArrayHelper<T, s, ss...>{ using type = std::array<typename ArrayHelper<T, ss...>::type, s>; };

template<class T, size_t ...ss> using Array = typename ArrayHelper<T, ss...>::type;
int main()
{
    int T;
    cin >> T;
    for (int case_i = 1; case_i <= T; ++case_i)
    {
        int n;
        cin >> n;
        int ok = 0;
        rep(i, n)
        {
            string s;
            cin >> s;
            rep(j, n)
                if (s[j] == '1')
                    ok |= 1 << (n * i + j);
        }

        const auto pri = [n](int ok)
        {
            rep(i, n)
            {
                string s;
                rep(j, n)
                {
                    s += '0' + (ok >> (i * n + j) & 1);
                }
                cout << s << endl;
            }
            cout << endl;
        };
        const auto check = [n](int ok)
        {
            int order[4];
            rep(i, n)
                order[i] = i;

            const auto check_order = [&]()
            {
                bool dp[5][1 << 4] = {};
                clr(dp, 0);
                dp[0][0] = true;
                rep(i, n) rep(mask, 1 << n)
                {
                    if (!dp[i][mask])
                        continue;

                    const int oi = order[i];

                    bool any = false;
                    rep(j, n)
                    {
                        if (!(mask >> j & 1) && (ok >> (oi * n + j) & 1))
                        {
                            any = true;
                            dp[i + 1][mask | (1 << j)] = true;
                        }
                    }
                    if (!any)
                        return false;
                }
                return dp[n][(1 << n) - 1];
            };

            do {
                if (!check_order())
                    return false;
            } while (next_permutation(order, order + n));
            return true;
        };

        int res = n * n;
        rep(mask, 1 << (n * n))
        {
            const int cost = __builtin_popcount(mask);
            if (cost < res && (mask & ok) == 0)
            {
                if (check(ok | mask))
                {
                    upmin(res, cost);
                }
            }
        }
        cout << "Case #" << case_i << ": " << res << endl;
    }
}
