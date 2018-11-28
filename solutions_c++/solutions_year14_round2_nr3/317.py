#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

const int maxN = 60;

int zip[maxN];
string szip[maxN];
vector<int> edges[maxN];
int used[maxN], use = 0;
int n, m;
string best, cur;
int perm[maxN];
int uk;

string toStr(int v)
{
	string res;
	while (v){
		res += v % 10 + '0';
		v /= 10;
	}
	reverse(res.begin(), res.end());
	return res;
}

bool cmp(int a, int b)
{
	return zip[a] < zip[b];
}

void dfs(int v)
{
	used[v] = use;
	cur += szip[v];
	while (true)
	{
		if (uk >= n)
			break;
		int p = lower_bound(edges[v].begin(), edges[v].end(), perm[uk]) - edges[v].begin();
		if (p < edges[v].size() && edges[v][p] == perm[uk])
		{
			uk++;
			dfs(perm[uk - 1]);
		}
		else
		{
			break;
		}
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int q;
	scanf("%d", &q);
	for (int t = 0; t < q; t++)
	{
		best.clear();
		printf("Case #%d: ", t + 1);
		scanf("%d%d", &n, &m);
		int sm = 0;
		for (int i = 0; i < n; i++)
		{
			edges[i].clear();
			scanf("%d", &zip[i]);
			szip[i] = toStr(zip[i]);
			if (zip[i] < zip[sm])
			{
				sm = i;
			}
		}
		for (int i = 0; i < m; i++)
		{
			int x, y;
			scanf("%d%d", &x, &y);
			x--, y--;
			edges[x].push_back(y);
			edges[y].push_back(x);
		}
		for (int i = 0; i < n; i++)
		{
			sort(edges[i].begin(), edges[i].end());
		}
		for (int i = 0; i < n; i++)
		{
			perm[i] = i;
		}
		do {
			cur.clear();
			uk = 1;
			use++;
			dfs(perm[0]);
			if (cur.length() == n * 5 && (best.empty() || cur < best))
			{
				best = cur;
			}
		} while (next_permutation(perm, perm + n));
		printf("%s\n", best.c_str());
	}
	return 0;
}