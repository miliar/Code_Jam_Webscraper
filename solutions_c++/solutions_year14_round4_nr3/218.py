#undef NDEBUG
#ifdef gridnevvvit
#define _GLIBCXX_DEBUG
#endif

#include <iostream>
#include <fstream>
#include <iomanip>
#include <sstream>

#include <map>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <vector>
#include <string>
#include <deque>
#include <bitset>
#include <algorithm>
#include <utility>
                  
#include <functional>
#include <limits>
#include <numeric>
#include <complex>

#include <cassert>
#include <cmath>
#include <memory.h>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>   

using namespace std;

typedef long long li;
typedef long double ld;
typedef pair<int,int> pt;
typedef pair<ld, ld> ptd;
typedef unsigned long long uli;

#define pb push_back
#define mp make_pair
#define mset(a, val) memset(a, val, sizeof (a))
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define ft first
#define sc second
#define sz(a) int((a).size())
#define x first
#define y second

template<typename X> inline X abs(const X& a) { return (a < 0 ? -a : a); }
template<typename X> inline X sqr(const X& a) { return (a * a); }
template<typename T> inline string toStr(T x) { stringstream st; st << x; string s; st >> s; return s; }
template<typename T> inline int hasBit(T mask, int b) { return (b >= 0 && (mask & (T(1) << b)) != 0) ? 1 : 0; }
template<typename X, typename T>inline ostream& operator<< (ostream& out, const pair<T, X>& p) { return out << '(' << p.ft << ", " << p.sc << ')'; }

inline int nextInt() { int x; if (scanf("%d", &x) != 1) throw; return x; }
inline li nextInt64() { li x; if (scanf("%I64d", &x) != 1) throw; return x; }
inline double nextDouble() { double x; if (scanf("%lf", &x) != 1) throw; return x; }

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define fore(i, a, b) for(int i = int(a); i <= int(b); i++)
#define ford(i, n) for(int i = int(n - 1); i >= 0; i--)
#define foreach(it, a) for(__typeof((a).begin()) it = (a).begin(); it != (a).end(); it++)

const int INF = int(1e9);
const li INF64 = li(INF) * li(INF);
const ld EPS = 1e-9;
const ld PI = ld(3.1415926535897932384626433832795);

const int N = 200000; // verticies
const int M = 500000; //edges
 
struct edge 
{
	int a, b, cap, flow;
};
 
int n, s, t, d[N], ptr[N], q[N];
edge e[M];
int sze = 0;
int w, h, tb;

int A[505][505];


vector<int> g[N];
 
void add_edge (int a, int b, int cap) 
{
	edge e1 = { a, b, cap, 0 };
	edge e2 = { b, a, 0, 0 };
	g[a].pb(sze);
	e[sze++] = e1;
	g[b].pb(sze);
	e[sze++] = e2;
}
 
bool bfs() 
{
	int head = 0, tail = 0;
	q[tail++] = s;
	memset (d, -1, n * sizeof d[0]);
	d[s] = 0;
	while (head < tail && d[t] == -1) 
	{
		int v = q[head++];
		forn(i, sz(g[v])) 
		{
			int id = g[v][i];
		    int to = e[id].b;
			
			if (d[to] == -1 && e[id].flow < e[id].cap) 
			{
				q[tail++] = to;
				d[to] = d[v] + 1;
			}
		}
	}
	
	return d[t] != -1;
}
 
int dfs (int v, int flow) 
{
	if (!flow)  
	    return 0;
	if (v == t)  
	    return flow;
	for (; ptr[v] < sz(g[v]); ++ptr[v]) 
	{
		int id = g[v][ptr[v]];
	    int to = e[id].b;
		if (d[to] != d[v] + 1)  
		    continue;
		int pushed = dfs (to, min (flow, e[id].cap - e[id].flow));
		if (pushed) 
		{
			e[id].flow += pushed;
			e[id ^ 1].flow -= pushed;
			return pushed;
		}
	}
	
	return 0;
}
 
int dinic() 
{
	int flow = 0;
	while(true) 
	{
		if (!bfs())
		    break;
		memset (ptr, 0, n * sizeof ptr[0]);
		while (int pushed = dfs (s, INF))
			flow += pushed;
	}
	return flow;
}

inline bool read() {
	w = nextInt();
	h = nextInt();
	tb = nextInt();

	memset(A, 0, sizeof A);

	forn(i, tb) {
	 	int x[2], y[2];

	 	x[0] = nextInt();
	 	y[0] = nextInt();

	 	x[1] = nextInt();
	 	y[1] = nextInt();

	 	for(int v = x[0]; v <= x[1]; v++)
	 		for(int u = y[0]; u <= y[1]; u++)
	 		 	A[v][u] = 1;
	 
	}

 	return true;
}                 

bool correct(int x, int y, int tx, int ty) {
 	return (x >= 0 && x < tx && y >= 0 && y < ty);
}

inline void solve() {                    
	n = 1;
	s = 0;

	sze = 0;

	forn(i, N)
		g[i].clear();

   	int dx[] = {1, -1, 0, 0};
   	int dy[] = {0, 0, 1, -1};

   	cerr << "ok" << endl;

	forn(x, w) {
		forn(y, h) {
			int pos = x * h + y;
			int in = 2 * pos;
			int out = 2 * pos + 1;

			if (A[x][y]) continue;

			forn(dir, 4) {
				int nx = x + dx[dir];
				int ny = y + dy[dir];

				if (!correct(nx, ny, w, h))  continue;

				if (A[nx][ny]) continue;

				int posn = nx * h + ny;
				int inn = 2 * posn;
				int outn = 2 * posn + 1;


				add_edge(out + 1, inn + 1, 1);

			}

			add_edge(in + 1, out + 1, 1);	
		}	
   	}

   	cerr << "ok" << endl;

   	n += 2 * w * h;

   	t = n;
    
    forn(x, w)
   	{
   	 	int pos = x * h + 0;

   	 	int in = 2 * pos;

   	 	add_edge(0, in + 1, 1);

   	 	pos += h - 1;

   		int out = 2 * pos + 1;

   		add_edge(out + 1, t, 1);
   	}

    n++;

    cerr << sze << endl;

    cerr << "ok" << endl;

   	cout << dinic() << endl;

   	cerr << "ok";

}

int main() 
{

#ifdef gridnevvvit
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
    
	srand(time(NULL));

	cout << setprecision(10) << fixed;
	cerr << setprecision(5) << fixed;
	
	bool multipleTestCases = true;

	if (multipleTestCases) {
		
		int testCnt;

		assert(scanf("%d", &testCnt) == 1);

		forn(test, testCnt) {
		 	printf("Case #%d: ", test + 1);
		 	
		 	cerr << test + 1 << endl;

		 	assert(read());
         	solve();
		}
	 	
	}
	else {
	 	assert(read());
	 	solve();
	}

#ifdef gridnevvvit
	cerr << "===Time: " << clock()  << "===" << endl;
#endif

} 