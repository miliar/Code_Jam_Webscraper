#include <iostream>
#include <sstream>

#include <vector>
#include <set>
#include <bitset>
#include <map>
#include <string>
#include <deque>

#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <ctime>

#include <algorithm>
#include <numeric>

#define pb push_back
#define pbk pop_back
#define mp make_pair
#define fs first
#define sc second
#define all(x) (x).begin(), (x).end()
#define foreach(i, x) for (__typeof((x).begin()) i = (x).begin(); i != (x).end(); ++i)
#define len(x) ((int) (x).size())
#define endl '\n'

#ifdef CUTEBMAING
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
#define eprintf(...) 42
#endif

using namespace std;

typedef long long int64;
typedef long double ld;
typedef unsigned long long lint;

const int inf = ((1 << 30) - 1);
const int64 linf = ((1ll << 62) - 1);

namespace dinic{
	const int N = 3e6 + 100;
	int a[N], b[N], f[N], cf[N], m = 0, n;
	vector<int> g[N];

	void addEdge(int u, int v, int flowN, int flowB = 0){
		//eprintf("%d %d %d %d\n", u, v, flowN, flowB);
		a[m] = u, b[m] = v, f[m] = 0, cf[m] = flowN, g[u].pb(m), m++;
		a[m] = v, b[m] = u, f[m] = 0, cf[m] = flowB, g[v].pb(m), m++;
	}

	int dist[N];
	deque<int> q;
	int cc;

	void bfs(){
		fill_n(dist, n, inf);
		dist[0] = 0;
		q.pb(0);
		while (!q.empty()){
			int v = q.front();
			q.pop_front();
			for (int e : g[v]){
				if (cf[e] < cc)
					continue;
				int to = b[e];
				if (dist[to] > dist[v] + 1){
					dist[to] = dist[v] + 1;
					q.pb(to);
				}
			}
		}
	}

	int first[N];

	bool u[N];
	int state[N];
	int curState = 0;

	bool& getU(int v){
		if (state[v] != curState)
			state[v] = curState, u[v] = false;
		return u[v];
	}

	int dfs(int v, int flow = inf){
		if (v == n - 1)
			return flow;
		bool &u = getU(v);
		if (u)
			return 0;
		u = true;
		for (int &i = first[v]; i < len(g[v]); i++){
			int e = g[v][i], to = b[e];
			if (cf[e] < cc || dist[v] + 1 != dist[to])
				continue;
			int res = dfs(to, min(flow, cf[e]));
			if (res == 0)
				continue;
			f[e] += res, cf[e] -= res;
			f[e ^ 1] -= res, cf[e ^ 1] += res;
			return res;
		}
		return 0;
	}

	int dinics(){
		int ans = 0;
		fill_n(first, n, 0);
		bfs();
		for (;;){
			curState++;
			int curRes = dfs(0);
			if (!curRes)
				break;
			ans += curRes;
		}
		return ans;
	}

	int dinic(){
		int ans = 0;
		for (cc = 1; cc > 0; cc >>= 1){
			for (;;){
				int curAns = dinics();
				if (!curAns)
					break;
				ans += curAns;
			}
		}
		return ans;
	}
};

const int N = 1101;

#define y1 _y1
#define x1 _x1

int w, h, b;
int x1[N], y1[N], x2[N], y2[N];
int zx[N], zy[N];
int ccx, ccy;

void zipCoords(int *x1, int *x2, int *z, int &cc, int mx){
	for (int i = 0; i < b; i++)
		z[i] = x1[i];
	for (int i = 0; i < b; i++)
		z[i + b] = x2[i];
	cc = b * 2 + 2;
	z[cc - 2] = 0, z[cc - 1] = mx;
	sort(z, z + cc);
	cc = unique(z, z + cc) - z;
	for (int i = 0; i < b; i++){
		x1[i] = lower_bound(z, z + cc, x1[i]) - z;
		x2[i] = lower_bound(z, z + cc, x2[i]) - z;
	}
	cc--;
}

int p[N][N];

int f[N][N], t[N][N];

inline void solve(){
	cin >> w >> h >> b;
	for (int i = 0; i < b; i++){
		cin >> x1[i] >> y1[i] >> x2[i] >> y2[i];
		if (x1[i] > x2[i])
			swap(x1[i], x2[i]);
		if (y1[i] > y2[i])
			swap(y1[i], y2[i]);
		x2[i]++, y2[i]++;
	}
	//zipCoords(x1, x2, zx, ccx, w);
	//zipCoords(y1, y2, zy, ccy, h);
	ccx = w, ccy = h;
	for (int i = 0; i <= ccx; i++)
		zx[i] = i;
	for (int i = 0; i <= ccy; i++)
		zy[i] = i;
	for (int i = 0; i < ccx; i++)
		for (int j = 0; j < ccy; j++)
			p[i][j] = 0;
	for (int i = 0; i < b; i++){
		p[x1[i]][y1[i]]++;
		p[x2[i]][y1[i]]--;
		p[x1[i]][y2[i]]--;
		p[x2[i]][y2[i]]++;
	}
	for (int i = 0; i < ccx; i++)
		for (int j = 0; j < ccy; j++){
			if (i > 0)
				p[i][j] += p[i - 1][j];
			if (j > 0)
				p[i][j] += p[i][j - 1];
			if (i > 0 && j > 0)
				p[i][j] -= p[i - 1][j - 1];
		}
	dinic::n = 1, dinic::m = 0;
	for (int i = 0; i < ccx; i++)
		for (int j = 0; j < ccy; j++){
			f[i][j] = dinic::n++;
			t[i][j] = dinic::n++;
		}
	dinic::n++;
	for (int i = 0; i < dinic::n; i++)
		dinic::g[i].clear();
	for (int i = 0; i < ccx; i++)
		for (int j = 0; j < ccy; j++){
			if (j < ccy - 1 && !p[i][j] && !p[i][j + 1]){
				dinic::addEdge(t[i][j], f[i][j + 1], inf, 0);
				dinic::addEdge(t[i][j + 1], f[i][j], inf, 0);
			}
			if (i < ccx - 1 && !p[i][j] && !p[i + 1][j]){
				dinic::addEdge(t[i][j], f[i + 1][j], inf, 0);
				dinic::addEdge(t[i + 1][j], f[i][j], inf, 0);
			}
		}
	for (int i = 0; i < ccx; i++)
		for (int j = 0; j < ccy; j++)
			dinic::addEdge(f[i][j], t[i][j], min(zx[i + 1] - zx[i], zy[j + 1] - zy[j]));
	for (int i = 0; i < ccx; i++)
		if (!p[i][0])
			dinic::addEdge(0, f[i][0], (zx[i + 1] - zx[i]));
	for (int i = 0; i < ccx; i++)
		if (!p[i][ccy - 1])
			dinic::addEdge(t[i][ccy - 1], dinic::n - 1, (zx[i + 1] - zx[i]));
	printf("%d\n", dinic::dinic());
}

int main(){
#if defined CUTEBMAING && !defined STRESS
    assert(freopen("input.txt", "r", stdin));
	assert(freopen("output.txt", "w", stdout));
#endif
	int t; cin >> t;
	for (int i = 0; i < t; i++){
		printf("Case #%d: ", i + 1);
		solve();
		eprintf("%d\n", i + 1);
	}
    return 0;
}
