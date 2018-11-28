#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#if __cplusplus > 201103L
#include <initializer_list>
#include <unordered_map>
#include <unordered_set>
#endif

using namespace std;

#ifdef LOCAL
#define DEBUG
#endif

#define oo 0x3F3F3F3F
#define fst first
#define snd second
#define PB push_back
#define SZ(x) (int)((x).size())
#define ALL(x) (x).begin(), (x).end()
#define FOR(i, a, b) for (int _end_ = (b), i = (a); i <= _end_; ++i)
#define ROF(i, a, b) for (int _end_ = (b), i = (a); i >= _end_; --i)

typedef unsigned int uint;
typedef long long int64;
typedef unsigned long long uint64;
typedef long double real;

int64 fpm(int64 b, int64 e, int64 m) { int64 t = 1; for (; e; e >>= 1, b = b * b % m) e & 1 ? t = t * b % m : 0; return t; }
template<class T> inline bool chkmin(T &a, T b) {return a > b ? a = b, true : false;}
template<class T> inline bool chkmax(T &a, T b) {return a < b ? a = b, true : false;}
template<class T> inline T sqr(T x) {return x * x;}
template <typename T> T gcd(T x, T y) {for (T t; x; ) t = x, x = y % x, y = t; return y; }

template<class edge> struct Graph {
    vector<vector<edge> > adj;
    Graph(int n) {adj.clear(); adj.resize(n + 5);}
    Graph() {adj.clear(); }
    void resize(int n) {adj.resize(n + 5); }
    void add(int s, edge e){adj[s].push_back(e);}
    void del(int s, edge e) {adj[s].erase(find(iter(adj[s]), e)); }
    vector<edge>& operator [](int t) {return adj[t];}
};

int f[22], g[22];

int main(int argc, char **argv) {
#ifdef LOCAL
    freopen("A-small-attempt0.in" , "r", stdin);
    freopen("A.out", "w", stdout);
#endif
    ios_base::sync_with_stdio(false);
    
    int T;
    cin >> T;
    for (int tc = 1; tc <= T; ++tc) {
        cout << "Case #" << tc << ": ";

        int x, y;
        cin >> x;
        for (int i = 1; i <= 4; ++i) {
            for (int j = 1, v; j <= 4; ++j) {
                cin >> v;
                f[v] = i;
            }
        }
        cin >> y;
        for (int i = 1; i <= 4; ++i) {
            for (int j = 1, v; j <= 4; ++j) {
                cin >> v;
                g[v] = i;
            }
        }

        int cnt = 0, sum = 0;
        for (int i = 1; i <= 16; ++i) {
            if (f[i] == x && g[i] == y)
                ++cnt, sum += i;
        }
        if (cnt == 0) {
            cout << "Volunteer cheated!" << endl;
        } else if (cnt == 1) {
            cout << sum << endl;
        } else
            cout << "Bad magician!" << endl;
    }

    return 0; 
}
