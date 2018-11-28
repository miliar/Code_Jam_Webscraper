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

vi min_path(const vi& a, const vi& b)
{
    if (a.empty()) return b;
    assert(a.size() == b.size());
    forv(i, a) {
        if (a[i] < b[i]) return a;
        if (a[i] > b[i]) return b;
    }
    return a;
}

void solve()
{
    int numTests; cin >> numTests;
    for1(testId, numTests) {
        cerr << "Running test " << testId << endl;
        int k, n; cin >> k >> n;
        vi startKeys;
        forn(i, k) {
            int key; cin >> key;
            --key;
            startKeys.pb(key);
        }
        vi type(n);
        vector<vi> keys(n);
        forn(i, n) {
            cin >> type[i];
            --type[i];
            int kn; cin >> kn;
            forn(j, kn) {
                int ck; cin >> ck;
                --ck;
                keys[i].pb(ck);
            }
        }
        vector<vi> d(1 << n);
        vector<vi> path(1 << n);
        d[0] = startKeys;
        forn(mask, 1 << n) {
            forn(i, n) {
                if (mask & (1 << i)) continue;
                vi np = path[mask];
                vi nd = d[mask];
                auto it = find(all(nd), type[i]);
                if (it != nd.end()) {
                    int nmask = mask ^ (1 << i);
                    nd.erase(it);
                    for (int k : keys[i]) {
                        nd.pb(k);
                    }
                    d[nmask] = nd;
                    np.pb(i + 1);
                    path[nmask] = min_path(path[nmask], np);
                    np.pop_back();
                }
            }
        }
        if (path[(1 << n) - 1].empty()) {
            cout << "Case #" << testId << ": IMPOSSIBLE\n";
        } else {
            cout << "Case #" << testId << ":";
            for (int c : path[(1 << n) - 1]) {
                cout << " " << c;
            }
            cout << endl;
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    solve();
    return 0;
}
