#include <iostream>
#include <iosfwd>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cassert>
#include <cctype>
#include <climits>
#include <vector>
#include <bitset>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <deque>
#include <string>
#include <list>
#include <iterator>
#include <sstream>
#include <complex>
#include <fstream>
#include <functional>
#include <numeric>
#include <utility>
#include <algorithm>
#include <assert.h>
#include <unordered_map>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef double ld;
typedef vector < long long > vll;
typedef pair <long long, long long> pll;
typedef pair <int, int> pii;
typedef vector < int > vii;
typedef complex < double > Point;

#define csl ios_base::sync_with_stdio(false); cin.tie(NULL)
#define mp make_pair
#define fst first
#define snd second
#define prev PREV
int t, n, m, u, v, q, r, ql, qr, k, l, s, w, h, c, z, d, a, b;
const int N = 1e5 + 500;
const long long mod = 1e9 + 7;
const long long INF = 1LL << 52LL;
string str, S;
int X[N], Y[N], Z[N];
int sq(int f) {
    return f * f;
}
queue < int > Q;
bool vis[N];
vii adj[N];
bool check(int m) {
    for (int i = 0; i < n; ++i)
        adj[i].clear();
    for (int i = 0; i < n; ++i)
        for (int j = i + 1; j < n; ++j) {
            if (sq(X[i] - X[j]) + sq(Y[i] - Y[j]) + sq(Z[i] - Z[j]) <= m) {
                adj[i].push_back(j);
                adj[j].push_back(i);
            }
        }
    Q.push(0);
    memset(vis, 0, sizeof(vis));
    while (!Q.empty()) {
        int x = Q.front();
        Q.pop();
        if (vis[x]) continue;
        vis[x] = true;
        for (int u : adj[x]) {
            Q.push(u);
        }
    }
    return vis[1];
}
int main() {
    csl;
    cin >> t;
    for (int ii = 1; ii <= t; ++ii) {
        cout << "Case #" << ii << ": ";
        cin >> n;
        cin >> s;
        for (int i = 0; i < n; ++i) {
            cin >> X[i] >> Y[i] >> Z[i];
            cin >> a >> b >> c;
        }
        int lo = 0, hi = 3 * 1000 * 2000;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (check(mid)) hi = mid;
            else lo = mid + 1;
        }
        double x = lo;
        cout << fixed << setprecision(5) << sqrt(x);
        cout << '\n';
    }
    return 0;
}
