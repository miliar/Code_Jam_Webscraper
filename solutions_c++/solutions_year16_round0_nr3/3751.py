#pragma comment(linker, "/STACK:256000000")

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
#undef NDEBUG
#include <cassert>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <bitset>
#include <queue>
#include <deque>
#include <unordered_map>
#include <unordered_set>
#include <tuple>

using namespace std;

#define pb push_back
#define mp make_pair
#define mt make_tuple
#define pbk pop_back
#define sz(s) ((int) (s).size())
#define fs first
#define sc second
#define all(x) (x).begin(), (x).end()
#ifdef LOCAL42
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
#define eprintf(...) 42
#endif
#if _WIN32 || __WIN32__ || _WIN64 || __WIN64__
#define LLD "%I64d"
#else
#define LLD "%lld"
#endif
#define prev huprev
#define next hunext
#define link hulink
#define hash huhash
#define rank hurank
#define y0 yy0
#define y1 yy1

typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int, int> pii;
typedef vector<int> vi;

const int inf = 1e9;
const double eps = 1e-9;
const double pi = 4 * atan(1.0);

int n, k;
string cur;
vector<pair<string, vector<ll> > > ans;

void gen(int x) {
    if (x >= n) {
        vector<ll> examples;
        for (int i = 2; i <= 10; ++i) {
            ll val = 0;
            for (int j = 0; j < n; ++j) {
                val = val * i + cur[j] - '0';
            }
            if (val <= 1) {
                return;
            }
            bool fl = false;
            for (ll j = 2; j * j <= val; ++j) {
                if (val % j == 0) {
                    examples.pb(j);
                    fl = true;
                    break;
                }
            }
            if (!fl) {
                return;
            }
        }
        ans.pb(mp(cur, examples));
        cerr << "found " << sz(ans) << " of " << k << endl;
        return;
    }
    for (int i = 0; i < 2; ++i) {
        if (i == 0 && (x == 0 || x == n - 1)) {
            continue;
        }
        cur.pb('0' + i);
        gen(x + 1);
        if (sz(ans) >= k) {
            return;
        }
        cur.pbk();
    }
}

inline void solve() {
    cin >> n >> k;
    cur = "";
    ans.clear();
    gen(0);
    assert(sz(ans) == k);
    for (pair<string, vector<ll> > p : ans) {
        cout << p.fs;
        for (ll e : p.sc) {
            cout << " " << e;
        }
        cout << endl;
    }
}

int main() {
#ifdef LOCAL42
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        printf("Case #%d:\n", i + 1);
        solve();
    }
    return 0;
}
