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

#ifndef ONLINE_JUDGE
#define DEBUG
#endif

#define oo 0x3F3F3F3F
#ifdef DEBUG
#define cvar(x) cerr << "<" << #x << ": " << x << ">"
#define evar(x) cvar (x) << endl
template<class T> void DISP(const char *s, T x, int n) {cerr << "[" << s << ": "; for (int i = 0; i < n; ++i) cerr << x[i] << " "; cerr << "]" << endl;}
#define disp(x,n) DISP(#x " to " #n, x, n)
#else
#define cvar(...) ({})
#define evar(...) ({})
#define disp(...) ({})
#endif
#define car first
#define cdr second
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
template <typename T> T gcd(T x, T y) {for (T t; x; t = x, x = y % x, y = t); return y; }

template<class edge> struct Graph
{
  vector<vector<edge> > adj;
  Graph(int n) {adj.clear (); adj.resize (n + 5);}
  Graph() {adj.clear (); }
  void resize(int n) {adj.resize (n + 5); }
  void add(int s, edge e){adj[s].push_back (e);}
  void del(int s, edge e) {adj[s].erase (find (iter (adj[s]), e)); }
  vector<edge>& operator [](int t) {return adj[t];}
};

const int maxS = 1 << 20;

struct node {
	double P, E;
} ;

node dp[2][maxS], *f = dp[0], *g = dp[1];

int main(int argc, char **argv)
{
#ifndef ONLINE_JUDGE
	freopen("D-small-attempt0.in" , "r", stdin);
	freopen("D.out", "w", stdout);
#endif
	ios_base::sync_with_stdio(false);

	int T; string S;
	cin >> T;

	cout << setprecision(20);
	FOR (tc, 1, T) {
		cin >> S;
		int n = SZ(S);
		fill(f, f + (1 << n), (node){0, 0});

		int s = 0;
		FOR (i, 0, n - 1) s |= (S[i] == 'X') << i;
		f[s] = (node){1, 0};

		double ans = 0;
		int mask = (1 << n) - 1;
		for (; f[mask].P == 0; ) {
			fill(g, g + (1 << n), (node){0, 0});
			FOR (S, 0, mask) {
				if (f[S].P == 0) continue;
				int x = S;
				for (; x >> (n - 1); x = ((x << 1) | 1) & mask);

				int cnt = 0;
				FOR (i, 0, n - 1) {
					if (x >> i & 1) {
						++cnt;
					} else {
						int y = x | 1 << i;
						double p = f[S].P * (cnt + 1) / n;
						g[y].P += p;
						g[y].E += p * (f[S].E + cnt / 2.0);
						
						cnt = 0;
					}
				}
			}
			FOR (S, 0, mask) {
				if (g[S].P) {
					g[S].E /= g[S].P;
				}
			}
			
			ans += n;
			swap(f, g);
		}
		cout << "Case #" << tc << ": " << ans - f[mask].E << endl;
		cerr << "Case #" << tc << ": " << ans - f[mask].E << endl;
	}

	return 0; 
}
