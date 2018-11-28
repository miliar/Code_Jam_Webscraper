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

vi ans;
int g[30][30];
int used[30];
int p[30];
vi A, B;

bool check(int n)
{
    for1(i, n - 1) {
        int ba = 1;
        forn(j, i) {
            if (p[i] > p[j]) {
                ba = max(ba, A[j] + 1);
            }
        }
        if (ba != A[i]) return false;
    }
    for (int i = n - 2; i >= 0; --i) {
        int ba = 1;
        for (int j = i + 1; j < n; ++j) {
            if (p[i] > p[j]) {
                ba = max(ba, B[j] + 1);
            }
        }
        if (ba != B[i]) return false;
    }
    return true;
}

void calc(int idx, int n)
{
    if (ans.size()) return;
    if (idx == n) {
        if (check(n)) {
            ans = vi(n);
            forn(i, n) ans[i] = p[i];
        }
        return;
    }

    forn(i, n) {
        if (used[i]) continue;
        bool ok = true;
        forn(j, idx) {
            if (p[j] < i) {
                if (g[j][idx] == 1) {
                    ok = false;
                    break;
                }
            } else {
                if (g[j][idx] == -1) {
                    ok = false;
                    break;
                }
            }
            if (!ok) break;
        }
        if (!ok) continue;
        used[i] = true;
        p[idx] = i;
        calc(idx + 1, n);
        used[i] = false;
    }
}

void solve()
{
    int numTests; cin >> numTests;
    for1(testId, numTests) {
        cerr << testId << endl;
        int n; cin >> n;
        vi a(n), b(n);
        forn(i, n) cin >> a[i];
        forn(i, n) cin >> b[i];
        ans.clear();
        forn(i, n) forn(j, n) g[i][j] = 0;
        forn(j, n) {
            forn(i, j) {
                if (a[i] >= a[j]) g[i][j] = 1, g[j][i] = -1;
                if (b[i] <= b[j]) g[i][j] = -1, g[j][i] = 1;
            }
            /*
            for (int i = j - 1; i >= 0; --i) {
                if (a[i] + 1 == a[j]) {
                    g[i][j] = -1;
                    g[j][i] = 1;
                    break;
                }
            }
            for (int i = j + 1; i < n; ++i) {
                if (b[i] + 1 == b[j]) {
                    g[i][j] = -1;
                    g[j][i] = 1;
                }
            }
            */
        }
        forn(i, n) used[i] = false;
        A = a;
        B = b;
        calc(0, n);
        assert(ans.size());
        cout << "Case #" << testId << ":";
        forn(i, n) cout << " " << ans[i] + 1;
        cout << endl;
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    solve();
    return 0;
}
