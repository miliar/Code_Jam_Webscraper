/*
 TASK:
 LANG: C++
 */
#include <algorithm>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iterator>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <bitset>
#include <cstring>
#include <string>
#include <climits>
#include <deque>
#include <utility>
#include <complex>
#include <numeric>
#include <functional>
#include <stack>
#include <iomanip>
#include <ctime>
#include <valarray>
//#include "vc.h"
#ifdef _MSC_VER
#include <hash_set>
#include <hash_map>
using namespace stdext;
#define __typeof(x) auto
#else
#if __GNUC__ > 2
#include <ext/hash_set>
#include <ext/hash_map>
using namespace __gnu_cxx;
#else
#include <hash_set>
#include <hash_map>
#endif
#endif

template<class key>
struct hashtemp {

	enum {
		bucket_size = 4, min_buckets = 8
	};
	virtual size_t operator()(const key &p) const=0;
	virtual ~hashtemp() {
	}

};

using namespace std;
#ifndef M_PI
const long double M_PI=acos((long double)-1);
#endif
#define rep(i,n) for(int  i=0;i<(int)(n);++i)
long double ZERO = 0;
const long double INF = 1 / ZERO, EPSILON = 1e-12;
#define all(c) (c).begin(),(c).end()
#define rep2(i,a,b) for(int i=(a);i<=((int)b);++i)
#define foreach(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

#define sz(v) ((int)((v).size()))
#define let(x,y) __typeof(y) x(y)

#define rrep(i,n) for(int  i=((int)n)-1;i>=0;--i)
#define rall(c) (c).rbegin(),(c).rend()
#define rrep2(i,a,b) for(int i=(a);i>=((int)b);--i)
#define rforeach(it,c) for(__typeof((c).rbegin()) it=(c).rbegin();it!=(c).rend();++it)
#define rep2d(i, j, v) rep(i, sz(v)) rep(j, sz(v[i]))
#define foreach2d(i, j, v) foreach(i,v) foreach(j,*i)
#define IN(x) ((x)*2)
#define OUT(x) ((x)*2+1)

int compress(map<int, int> &mp, int arr[], int last = -2) {
	int nxt = 0;
	for (map<int, int>::iterator it = mp.begin(); it != mp.end(); ++it) {
		if (last + 1 != it->first) {
			arr[nxt++] = it->first - last - 1;
		}
		arr[it->second = nxt++] = 1;
		last = it->first;
	}
	return nxt;
}

void rename(map<int, int> &mp, int arr[], int sz) {
	for (int i = 0; i < sz; ++i)
		arr[i] = mp[arr[i]];
}

int x0[1000], x1[1000], Y0[1000], Y1[1000];
int xsz[1000], ysz[1000];

struct edge {
  int to, flow, revID;
};
vector<vector<edge> > adj;
vector <int> vis;
inline void addEdge(int u, int v, int fl) {
  edge e1 = {v, fl, (int)adj[v].size()};
  edge e2 = {u, 0, (int)adj[u].size()};
  adj[u].push_back(e1);
  adj[v].push_back(e2);
}

int vid = 1;
inline int dfs(int u, int snk, int fl) {
  if(vis[u] == vid) return 0;
  if(!fl) return 0;
  if(u == snk) return fl;
  vis[u] = vid;
  for(int i = 0; i < (int)adj[u].size(); ++i) {
    int v = adj[u][i].to;
    int nfl = dfs(v, snk, min(fl, adj[u][i].flow));
    if(nfl) {
      int rid = adj[u][i].revID;
      adj[u][i].flow -= nfl;
      adj[v][rid].flow += nfl;
      return nfl;
    }
  }
  return 0;
}

inline int maxFlow(int src, int snk) {
  int mf = 0;
  vid++;
  while(int fl = dfs(src, snk, 1 << 30)) {
    mf += fl;
    vid++;
  }
  return mf;
}

int di[] = {0, 0, 1, -1} ;
int dj[] = {1, -1, 0, 0} ;

int main() {
	std::ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
#ifndef ONLINE_JUDGE
	freopen("1.in", "rt", stdin);
	freopen("3.out", "wt", stdout);
#endif
	int tt, w, h, b;
	cin >> tt;
	rep2(t,1,tt)
	{
		cin >> w >> h >> b;
		map<int, int> xs, ys;
		for (int i = 0; i < b; i++) {
			cin >> x0[i] >> Y0[i] >> x1[i] >> Y1[i];
			xs[x0[i]];
			xs[x1[i]];
			ys[Y0[i]];
			ys[Y1[i]];
		}
		xs[0], ys[-1], xs[w], ys[h];
		int cw = compress(xs, xsz);
		int ch = compress(ys, ysz);
		rename(xs, x0, b);
		rename(xs, x1, b);
		rename(ys, Y0, b);
		rename(ys, Y1, b);

		vector <vector <int> > grid(ch, vector <int> (cw, -2));
		for (int k=0 ; k < b ; k++) {
			for (int i=Y0[k]; i <= Y1[k] ; i++) {
				for (int j=x0[k] ; j<= x1[k] ; j++) {
					grid[i][j] = -1;
				}
			}
		}
		for (int i=0 ; i < ch ; i++)
			grid[i][0] = grid[i].back() = -1;

		int cnt = 0;
		for (int i=0 ; i < ch ; i++) {
			for (int j=0 ; j < cw ; j++)
				if (grid[i][j] == -2)
					grid[i][j] = cnt++;
		}
//
//		for (int i=ch-1 ; i >= 0; i--) {
//			for (int j=0 ; j < cw ; j++)
//				printf ("%3d", grid[i][j]);
//			printf ("\n");
//		}
		cnt*=2;
		int src = cnt, snk = cnt+1;
		cnt += 2;
		vis.clear();
		vis.resize(cnt);
		adj.clear();
		adj.resize(cnt);
		for (int j=0 ; j< cw ; j++) {
			if (grid[0][j] != -1)
				addEdge(src, IN(grid[0][j]), xsz[j]);
			if (grid.back()[j] != -1)
				addEdge(OUT(grid.back()[j]), snk, xsz[j]);
		}

		for (int i=0 ; i < ch ; i++) {
			for (int j=0 ; j < cw ; j++)
				if (grid[i][j] != -1) {
					addEdge(IN(grid[i][j]), OUT(grid[i][j]), max(xsz[j], ysz[i]));
				for (int d = 0 ; d < 4 ; d++) {
					int ni = i + di[d];
					int nj = j + dj[d];
					if (ni >= ch || ni < 0 || nj >= cw || nj < 0 || grid[ni][nj] == -1)
						continue;
					addEdge(OUT(grid[i][j]), IN(grid[ni][nj]),(d < 2)? ysz[i] : xsz[j]);
				}
			}
		}

		int res = maxFlow(src, snk);
		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}
