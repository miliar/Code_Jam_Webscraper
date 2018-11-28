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

struct Node
{
    int l, r;
};
const ll MOD = 1000002013;

ll solve(int n, const vector<Node>& nodes)
{
    auto ns = nodes;
    sort(all(ns), [](const Node& a, const Node& b) { return a.l < b.l; });
    ll ret = 0;
    while (!ns.empty()) {
        Node node = ns[0];
        ns.erase(ns.begin());
        int l = node.l, r = node.r;
        if (l == r) continue;
        for (Node& nn : ns) {
            if (nn.l == l) continue;
            if (nn.r <= r) continue;
            if (nn.l > r) break;
            ll add = (nn.l - l) * (nn.r - r);
            ret = (ret + add) % MOD;
            int rr = nn.r;
            nn.r = r;
            r = rr;
        }
    }
    return ret;
}

void solve()
{
    int numTests; cin >> numTests;
    for1(testId, numTests) {
        int n, m;
        cin >> n >> m;
        vector<Node> nodes;
        forn(i, m) {
            int cnt;
            Node node;
            cin >> node.l >> node.r >> cnt;
            --node.l, --node.r;
            forn(j, cnt) nodes.pb(node);
        }
        cout << "Case #" << testId << ": ";
        cout << solve(n, nodes) << endl;
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    solve();
    return 0;
}
