#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker,"/STACK:64000000")
#include <iostream>
#include <sstream>
#include <stdio.h>
#include <memory.h>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <cassert>
#include <time.h>
#include <bitset>

using namespace std;

#define mp make_pair
#define pb push_back
#define _(a,b) memset( (a), b, sizeof( a ) )
#define all(a) a.begin(), a.end()
#define sz(a) (int)a.size()
#ifdef WIN32
#define dbg(...) {fprintf(stderr, __VA_ARGS__); fflush(stderr);}
#define dbgx(x) {cerr << #x << " = " << x << endl;}
#define dbgv(v) {cerr << #v << " = {"; for (typeof(v.begin()) it = v.begin(); it != v.end(); it ++) cerr << *it << ", "; cerr << "}"; cerr << endl;}
#else
#define dbg(...) { }
#define dbgx(x) { }
#define dbgv(v) { }
#endif

typedef unsigned long long ull;
typedef long long lint;
typedef pair < int , int > pii;
typedef long double ld;

const int INF = 1000 * 1000 * 1000;
const lint LINF = 1000000000000000000LL;
const double eps = 1e-9;

void prepare()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
}

const int nmax = 1000 * 1000 + 5;

int s0, as, cs, rs;
int m0, am, cm, rm;
int n, d, par[nmax], cost[nmax];
vector < int > g[nmax];
vector < pii > ord;

void read()
{
	scanf("%d%d", &n, &d);
	scanf("%d%d%d%d", &s0, &as, &cs, &rs);
	scanf("%d%d%d%d", &m0, &am, &cm, &rm);

	cost[0] = s0;
	par[0] = m0;
	for (int i = 1; i < n; i ++)
	{
		cost[i] = ((lint)cost[i - 1] * (lint)as + cs) % rs;
		par[i] = ((lint)par[i - 1] * (lint)am + cm) % rm;
	}
	for (int i = 1; i < n; i ++)
	{
		par[i] %= i;
	}
	par[0] = -1;

	for (int i = 0; i < n; i ++)
		g[i].clear();
	for (int i = 1; i < n; i ++)
		g[par[i]].pb(i);
}

struct Event
{
	int t, id, type;
	Event(int _t, int _id, int _type)
	{
		t = _t;
		id = _id;
		type = _type;
	}
	bool operator < (const Event &oth) const
	{
		return t < oth.t;
	}
};

vector < Event > e;
bool isEnabled[nmax];
int curAns, ans;

int dfs(int id, bool isKill)
{
	if (!isEnabled[id])
		return 0;
	if (isKill)
	{
		isEnabled[id] = 0;
	}
	int ret = 1;
	for (int i = 0; i < sz(g[id]); i ++)
		ret += dfs(g[id][i], isKill);
	return ret;
}

bool hasPathToParent(int id)
{
	while (par[id] >= 0 && isEnabled[par[id]])
	{
		id = par[id];
	}

	return id == 0;
}

void process(Event ev)
{
	if (ev.type == +1)
	{
		int id = ev.id;
		isEnabled[id] = 1;
		if (hasPathToParent(id))
		{
			curAns += dfs(id, 0);
		}
	}
	else
	{
		int id = ev.id;
		if (hasPathToParent(id))
		{
			curAns -= dfs(id, 1);
		}
		isEnabled[id] = 0;
	}
}

bool solve()
{
	ans = 0;

	curAns = 0;
	ord.clear();
	e.clear();
	for (int i = 0; i < n; i ++)
	{
		ord.pb(mp(cost[i], i));
		isEnabled[i] = 0;
		
		e.pb(Event(cost[i] - d, i, +1));
		e.pb(Event(cost[i] + 1, i, -1));
	}
	sort(all(ord));
	sort(all(e));

	for (int l = 0, r = 0; l < sz(e); l = r)
	{
		for (r = l + 1; r < sz(e) && e[r].t == e[l].t; r ++);

		for (int i = l; i < r; i ++)
			process(e[i]);

		if (isEnabled[0])
		{
			ans = max(ans, curAns);
		}
	}

	printf("%d\n", ans);
	return false;
}

int main()
{
	prepare();
	int t;
	scanf("%d",&t);
	for (int i = 0; i < t; i ++)
	{
		dbg("Test %d\n", i);
		printf("Case #%d: ", i + 1);
		read();
		solve();
	}
	return 0;
}
