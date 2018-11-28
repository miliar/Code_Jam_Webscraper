#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

#ifdef LOCAL
	#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
	#define eprintf(...) 42
#endif

const int INF = (int)1e9;
const int pow2 = (1 << 21);
const int N = (int)3e6 + 10;

struct SegmentTree
{
	int minTree[pow2 * 2];
	int cntTree[pow2 * 2];
	int d[pow2 * 2];
	SegmentTree ()
	{
		for (int i = pow2; i < pow2 * 2; i++)
		{
			minTree[i] = 0;
			cntTree[i] = 1;
			d[i] = 0;
		}
		for (int i = pow2 - 1; i >= 0; i--)
		{
			minTree[i] = 0;
			cntTree[i] = cntTree[2 * i] + cntTree[2 * i + 1];
			d[i] = 0;
		}
	}
	void push(int v)
	{
		minTree[2 * v] += d[v];
		d[2 * v] += d[v];
		minTree[2 * v + 1] += d[v];
		d[2 * v + 1] += d[v];
		d[v] = 0;
	}
	void addValue(int a, int b, int val, int v = 1, int l = 0, int r = pow2 - 1)
	{
		if (l >= a && r <= b)
		{
			minTree[v] += val;
			d[v] += val;
			return;
		}
		if (l > b || r < a)
			return;
		push(v);
		int m = (l + r) / 2;
		addValue(a, b, val, 2 * v, l, m);
		addValue(a, b, val, 2 * v + 1, m + 1, r);
		minTree[v] = min(minTree[2 * v], minTree[2 * v + 1]);
		cntTree[v] = 0;
		if (minTree[2 * v] == minTree[v])
			cntTree[v] += cntTree[2 * v];
		if (minTree[2 * v + 1] == minTree[v])
			cntTree[v] += cntTree[2 * v + 1];
	}
	pair<int, int> getValue(int a, int b, int v = 1, int l = 0, int r = pow2 - 1)
	{
		if (l >= a && r <= b)
			return make_pair(minTree[v], cntTree[v]);
		if (l > b || r < a)
			return make_pair(INF, 0);
		push(v);
		int m = (l + r) / 2;
		auto p1 = getValue(a, b, 2 * v, l, m);
		auto p2 = getValue(a, b, 2 * v + 1, m + 1, r);
		if (p1.first < p2.first)
			return p1;
		if (p2.first < p1.first)
			return p2;
		return make_pair(p1.first, p1.second + p2.second);
	}
};

SegmentTree tree;

struct Generator
{
	int values[N];
	int a, c, r;
	Generator() {}
	void gen(int n)
	{
		for (int i = 1; i < n; i++)
		{
			long long res = ((long long)values[i - 1] * (long long)a + c) % (long long)r;
			values[i] = res;
		}
	}
	void scan()
	{
		scanf("%d%d%d%d", &values[0], &a, &c, &r);
	}
};

Generator salary, par;
vector <int> g[N];
int tme = 0;
int tin[N], tout[N];
int euler[2 * N];
int h[N];
vector <int> withS[N];
int perm[N];

void dfs(int v)
{
	tin[v] = tme;
	euler[tme++] = v;
	for (int to : g[v])
	{
		h[to] = h[v] + 1;
		dfs(to);
	}
	tout[v] = tme - 1;
}

bool cmpBySal(int a, int b)
{
	return salary.values[a] < salary.values[b];
}

int ans = 0;

void relaxAns()
{
	auto p = tree.getValue(0, tme - 1);
	if (p.first == 0)
		ans = max(ans, p.second);
}

void solve()
{
	ans = 0;
	int n, D;
	scanf("%d%d", &n, &D);
	salary.scan();
	salary.gen(n);
	par.scan();
	par.gen(n);

	int maxS = 0;
	for (int i = 0; i < N; i++)
		withS[i].clear();
	for (int i = 0; i < n; i++)
	{
		maxS = max(maxS, salary.values[i]);
		withS[salary.values[i]].push_back(i);
		perm[i] = i;
	}
	sort(perm, perm + n, cmpBySal);
	tme = 0;
	for (int i = 0; i < n; i++)
		g[i].clear();
	for (int i = 1; i < n; i++)
		g[par.values[i] % i].push_back(i);
	h[0] = 1;
	dfs(0);
	tree = SegmentTree();	
	for (int i = 0; i < n; i++)
	{
		tree.addValue(tin[i], tin[i], h[i]);
	}
	for (int i = 0; i <= D; i++)
	{
		for (int v : withS[i])
		{
			tree.addValue(tin[v], tout[v], -1);
		}
	}
	relaxAns();
	for (int i = 0; i <= maxS - D; i++)
	{
		for (int v : withS[i])
		{
			tree.addValue(tin[v], tout[v], 1);
		}
		for (int v : withS[i + D + 1])
		{
			tree.addValue(tin[v], tout[v], -1);
		}
		relaxAns();
	}
	printf("%d\n", ans);
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++)
	{
		eprintf("%d\n", i );
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
