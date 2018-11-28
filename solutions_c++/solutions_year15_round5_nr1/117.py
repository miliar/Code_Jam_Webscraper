#include <algorithm>
#include <iostream>
#include <cstring>
#include <vector>
using namespace std;
const int MAX = 1000005;
vector<int> adj[MAX];
int s[MAX], m[MAX], st[MAX], fi[MAX], num;
void dfs(int v)
{
	st[v] = num++;
	for (int i = 0; i < adj[v].size(); i++)
	{
		int u = adj[v][i];
		dfs(u);
	}
	fi[v] = num;
}
int mn[4 * MAX], cnt[4 * MAX], lazy[4 * MAX];
void shift(int v)
{
	lazy[2 * v] += lazy[v];
	lazy[2 * v + 1] += lazy[v];
	mn[2 * v] += lazy[v];
	mn[2 * v + 1] += lazy[v];
	lazy[v] = 0;
}
void merge(int v)
{
	mn[v] = min(mn[2 * v], mn[2 * v + 1]);
	cnt[v] = 0;
	if (mn[v] == mn[2 * v])
		cnt[v] += cnt[2 * v];
	if (mn[v] == mn[2 * v + 1])
		cnt[v] += cnt[2 * v + 1];
}
void build(int v, int s, int e)
{
	lazy[v] = 0;
	if (e - s < 2)
	{
		mn[v] = 0;
		cnt[v] = 1;
		return;
	}
	int mid = (s + e) / 2;
	build(2 * v, s, mid);
	build(2 * v + 1, mid, e);
	merge(v);
}
void add(int l, int r, int val, int v, int s, int e)
{
	if (l <= s && e <= r)
	{
		lazy[v] += val;
		mn[v] += val;
		return;
	}
	if (e <= l || r <= s)
		return;
	shift(v);
	int mid = (s + e) / 2;
	add(l, r, val, 2 * v, s, mid);
	add(l, r, val, 2 * v + 1, mid, e);
	merge(v);
}
int main()
{
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	for (int _ = 1; _ <= t; _++)
	{
		num = 0;
		memset(s, 0, sizeof(s));
		memset(m, 0, sizeof(m));
		memset(st, 0, sizeof(st));
		memset(fi, 0, sizeof(fi));
		for (int i = 0; i < MAX; i++)
			adj[i].clear();
		int n, d;
		cin >> n >> d;
		long long as, cs, rs, am, cm, rm;
		cin >> s[0] >> as >> cs >> rs;
		cin >> m[0] >> am >> cm >> rm;
		vector<pair<int, int> > vals;
		for (int i = 1; i < n; i++)
		{
			s[i] = (s[i - 1] * as + cs) % rs;
			m[i] = (m[i - 1] * am + cm) % rm;
			adj[m[i] % i].push_back(i);
		}
		dfs(0);
		build(1, 0, n);
		for (int i = 0; i < n; i++)
		{
			vals.push_back(make_pair(s[i], i));
			add(st[i], fi[i], 1, 1, 0, n);
		}
		sort(vals.begin(), vals.end());
		int p = 0;
		int ans = 0;
		for (int i = 0; i < n; i++)
		{
			while (p < n && vals[p].first - vals[i].first <= d)
			{
				int v = vals[p].second;
				add(st[v], fi[v], -1, 1, 0, n);
				p++;
			}
			if (mn[1] == 0)
				ans = max(ans, cnt[1]);
			int v = vals[i].second;
			add(st[v], fi[v], 1, 1, 0, n);
		}
		cout << "Case #" << _ << ": " << ans << endl;
		cerr << "TEST " << _ << endl;
	}
	return 0;
}
