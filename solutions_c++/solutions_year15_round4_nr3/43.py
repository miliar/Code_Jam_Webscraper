#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstring>
#include <vector>
#include <map>
#define prev def1
using namespace std;
const int MAXN = 20005;
const int MAXE = 1000005;
int to[MAXE * 2], cap[MAXE * 2], prev[MAXE * 2], ptr[MAXN], d[MAXN], q[MAXN], head[MAXN], ecnt;
map<string, int> mp;
void add_edge(int u, int v, int uv, int vu = 0)
{
	to[ecnt] = v, cap[ecnt] = uv, prev[ecnt] = head[u]; head[u] = ecnt++;
	to[ecnt] = u, cap[ecnt] = vu, prev[ecnt] = head[v]; head[v] = ecnt++;
}
bool bfs(int source, int sink)
{
	memset(d, 63, sizeof(d));
	int h = 0, t = 0;
	d[sink] = 0;
	q[t++] = sink;
	while (h < t)
	{
		int v = q[h++];
		for (int i = head[v]; i != -1; i = prev[i])
			if (cap[i ^ 1] > 0 && d[to[i]] > d[v] + 1)
			{
				d[to[i]] = d[v] + 1;
				q[t++] = to[i];
			}
	}
	return (d[source] < MAXN);
}
int dfs(int v, int sink, int flow = 2147483647)
{
	if (v == sink)
		return flow;
	int ans = 0;
	for (; ptr[v] != -1; ptr[v] = prev[ptr[v]])
		if (cap[ptr[v]] && d[v] == d[to[ptr[v]]] + 1)
		{
			int x = dfs(to[ptr[v]], sink, min(flow, cap[ptr[v]]));
			flow -= x;
			ans += x;
			cap[ptr[v]] -= x;
			cap[ptr[v] ^ 1] += x;
			if (flow == 0)
				break;
		}
	return ans;
}
int max_flow(int source, int sink)
{
	int ans = 0;
	while (bfs(source, sink))
	{
		memcpy(ptr, head, sizeof(head));
		ans += dfs(source, sink);
	}
	return ans;
}
int main()
{
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	for (int _ = 1; _ <= t; _++)
	{
		memset(head, -1, sizeof(head));
		ecnt = 0;
		mp.clear();
		int n;
		cin >> n;
		string s, str;
		getline(cin, s);
		getline(cin, s);
		stringstream ss(s);
		int mpc = 0;
		while (ss >> str)
		{
			if (!mp.count(str))
				mp[str] = mpc++;
			add_edge(MAXN - 1, 2 * mp[str], 10000000);
		}
		getline(cin, s);
		stringstream ss2(s);
		while (ss2 >> str)
		{
			if (!mp.count(str))
				mp[str] = mpc++;
			add_edge(2 * mp[str] + 1, MAXN - 2, 10000000);
		}
		for (int i = 0; i < n - 2; i++)
		{
			getline(cin, s);
			stringstream ss3(s);
			vector<int> v;
			while (ss3 >> str)
			{
				if (!mp.count(str))
					mp[str] = mpc++;
				v.push_back(mp[str]);
			}
			sort(v.begin(), v.end());
			v.resize(unique(v.begin(), v.end()) - v.begin());
			for (int x = 0; x < v.size(); x++)
				for (int y = 0; y < v.size(); y++)
					if (x != y)
						add_edge(2 * v[x] + 1, 2 * v[y], 10000000);
		}
		for (int i = 0; i < mpc; i++)
			add_edge(2 * i, 2 * i + 1, 1);
		cout << "Case #" << _ << ": " << max_flow(MAXN - 1, MAXN - 2) << endl;
	}
	return 0;
}
