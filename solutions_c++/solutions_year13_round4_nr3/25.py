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

const int maxn = 2200;

Graph<int> G;

int h[maxn], v[maxn], B[maxn], o[maxn], lx[maxn];

void dfs_get(int v, vector<int> &vec)
{
	if (h[v]) return ;
	h[v] = true;
	vec.push_back(v);
	for (auto u : G[v]) {
		dfs_get(u, vec);
	}
}

void dfs_out(int v)
{
	if (o[v]) return ;
	vector<int> vec;

	memset(h, 0, sizeof(h));
	dfs_get(v, vec);
	sort(ALL(vec));
	for (auto u : vec)
		if (u != v)
			dfs_out(u);
	o[v] = ++o[0];
}

int main(int argc, char **argv)
{
#ifndef ONLINE_JUDGE
	freopen("C-large.in" , "r", stdin);
	freopen("C.out", "w", stdout);
#endif
	ios_base::sync_with_stdio(false);

	int T, n;
	
	cin >> T;
	FOR (tc, 1, T) {
		cin >> n;
		
		fill(lx + 1, lx + n + 1, 0);
		G.adj.clear(), G.resize(n);
		FOR (i, 1, n) {
			int a;
			cin >> a;
			if (lx[a]) G.add(lx[a], i);
			if (lx[a - 1]) G.add(i, lx[a - 1]);
			lx[a] = i;
		}

		fill(lx + 1, lx + n + 1, 0);
		FOR (i, 1, n) {
			cin >> B[i];
		}
		ROF (i, n, 1) {
			int b = B[i];
			if (lx[b]) G.add(lx[b], i);
			if (lx[b - 1]) G.add(i, lx[b - 1]);
			lx[b] = i;
		}

		fill(o, o + n + 1, 0);

		cout << "Case #" << tc << ":";
		FOR (i, 1, n) {
			dfs_out(i);
			cout << " " << o[i];
		}
		cout << endl;
	}

	return 0; 
}
