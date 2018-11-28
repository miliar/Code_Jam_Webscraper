#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <math.h>
#include <memory.h>


using namespace std;
#define MAX 1100000
int salaries[MAX];
int parent[MAX];
int mins[MAX], maxs[MAX];
vector<int> adj[MAX];
int N, D;
bool was[MAX];

void f(int v, int mn, int mx)
{
	if (was[v])
		throw 0;
	was[v] = true;
	mins[v] = min(mn, salaries[v]);
	maxs[v] = max(mx, salaries[v]);
	for (int i = 0; i < adj[v].size(); i++)
	{
		f(adj[v][i], mins[v], maxs[v]);
	}
}

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		
		cin >> N >>D;
		for (int i = 0; i < N; i++)
			adj[i].clear();
		long long s0, as, cs, rs;
		long long m0, am, cm, rm;
		cin >> s0 >> as >> cs >> rs;
		cin >> m0 >> am >> cm >> rm;
		salaries[0] = s0;
		parent[0] = 0;
		for (int i = 1; i < N; i++)
		{
			s0 = (s0 * as + cs) % rs;
			m0 = (m0 * am + cm) % rm;
			salaries[i] = s0;
			parent[i] = m0 % i;
		}
		for (int i = 1; i < N; i++)
		{
			adj[parent[i]].push_back(i);
		}
		memset(was, 0, sizeof(was));
		f(0, salaries[0], salaries[0]);
		int res = 0;
		vector<pair<int, int>> v;
		for (int i = 0; i < N; i++)
			v.push_back(make_pair(maxs[i], mins[i]));
		sort(v.begin(), v.end());
		set<pair<int, int>> s;
		for (int i = 0; i < N; i++)
		{
			s.insert(make_pair(v[i].second, i));
			while (s.size() > 0)
			{
				if (s.begin()->first >= v[i].first - D)
					break;
				else
					s.erase(s.begin());
			}
			res = max(res, (int)s.size());
		}
		printf("Case #%d: %d\n", t+1, res);
	}

	return 0;
}