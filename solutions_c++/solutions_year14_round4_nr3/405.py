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

const int DX[] = {0, -1, 0, 1};
const int DY[] = {1, 0, -1, 0};
const int NMAX = 505;
int n, m;
bool blocked[NMAX][NMAX];

struct Edge
{
    int to;
    int flow;
    int cap;
    int rev;
};

vector<Edge> g[NMAX * NMAX * 2];
bool used[NMAX * NMAX * 2];

bool inside(int x, int y)
{
    return x >= 0 && y >= 0 && x < n && y < m;
}

bool dfs(int v, int source, int target)
{
    if (v == target) return true;
    if (used[v]) return false;
    used[v] = true;
    int x, y;
    if (v & 1) {
        x = (v - 1) / 2 / m;
        y = (v - 1) / 2 % m;
    } else {
        x = v / 2 / m;
        y = v / 2 % m;
    }
    //cerr << x << " " << y << endl;
    if (source != v && blocked[x][y]) return false;
    forv(i, g[v]) {
        Edge& e = g[v][i];
        if (e.cap - e.flow == 0) continue;
        if (dfs(e.to, source, target)) {
            e.flow += 1;
            g[e.to][e.rev].flow -= 1;
            return true;
        }
    }
    return false;
}

bool findMaxFlow(int source, int target)
{
    forn(i, target + 1) used[i] = false;
    return dfs(source, source, target);
}

int maxFlow(int source, int target)
{
    int ret = 0;
    while (findMaxFlow(source, target)) ++ret;
    return ret;
}

int solveIt()
{
    int b;
    cin >> m >> n >> b;
    forn(i, n) forn(j, m) blocked[i][j] = false;
    forn(i, b) {
        int x0, y0, x1, y1;
        cin >> y0 >> x0 >> y1 >> x1;
        for (int x = x0; x <= x1; ++x)
            for (int y = y0; y <= y1; ++y) blocked[x][y] = true;
    }
    forn(i, NMAX * NMAX * 2) g[i].clear();

    forn(i, n) {
        forn(j, m) {
            int from = 2 * (i * m + j);
            int to = from + 1;
            Edge e{to, 0, 1, (int)g[to].size()};
            Edge e2{from, 0, 0, (int)g[from].size()};
            g[from].pb(e);
            g[to].pb(e2);
            forn(k, 4) {
                int x = i + DX[k];
                int y = j + DY[k];
                if (!inside(x, y)) continue;
                int from = 2 * (i * m + j) + 1;
                int to = 2 * (x * m + y);
                Edge e{to, 0, 1, (int)g[to].size()};
                Edge e2{from, 0, 0, (int)g[from].size()};
                g[from].pb(e);
                g[to].pb(e2);
            }
        }
    }

    int source = n * m * 2;
    int target = source + 1;
    
    forn(j, m) {
        int from = source;
        int to = 2 * j;
        Edge e{to, 0, 1, (int)g[to].size()};
        Edge e2{from, 0, 0, (int)g[from].size()};
        g[from].pb(e);
        g[to].pb(e2);
    }
    forn(j, m) {
        int from = 2 * ((n - 1) * m + j) + 1;
        int to = target;
        Edge e{to, 0, 1, (int)g[to].size()};
        Edge e2{from, 0, 0, (int)g[from].size()};
        g[from].pb(e);
        g[to].pb(e2);
    }
    //cerr << "X" << endl;
    return maxFlow(source, target);
}

void solve()
{
    int tc;
    cin >> tc;
    forn(it, tc) {
        cerr << it << endl;
        cout << "Case #" << it + 1 << ": " << solveIt() << endl;
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    solve();
    return 0;
}
