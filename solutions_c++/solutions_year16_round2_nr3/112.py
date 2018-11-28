	//     . .. ... .... ..... be name khoda ..... .... ... .. .     \\

#include <bits/stdc++.h>
using namespace std;

inline int in() { int x; scanf("%d", &x); return x; }
const int N = 2002;

int match[N], match2[N];
vector <int> g[N];
bool mark[N];

bool dfs(int v)
{
	if(mark[v])
		return 0;
	mark[v] = 1;
	for(int u : g[v])
		if(match[u] == -1 || dfs(match[u]))
		{
			match[u] = v;
			match2[v] = u;
			return 1;
		}
	return 0;
}

int main()
{
	int tests = in();
	for(int _t = 1; _t <= tests; _t++)
	{
		cout << "Case #" << _t << ": ";
		map <string, int> mp1, mp2;
		int up = 0, down = 0;
		int m;
		for(int n = m =in(); n; n--)
		{
			string x, y;
			cin >> x >> y;
			int idx, idy;
			if(mp1[x])
				idx = mp1[x];
			else
				idx = ++up;
			if(mp2[y])
				idy = mp2[y];
			else
				idy = ++down;
			mp1[x] = idx;
			mp2[y] = idy;
			g[idx].push_back(idy);
		}
		int maximumMatching = 0;
		fill(match, match + down + 1, -1);
		fill(match2, match2 + up + 1, -1);
		while(1)
		{
			fill(mark, mark + up + 1, 0);
			bool done = 0;
			for(int v = 1; v <= up; v++)
				if(!mark[v] && match2[v] == -1)
					if(dfs(v))
					{
						done = 1;
						maximumMatching++;
					}
			if(!done)
				break;
		}
		cout << m - (up + down - maximumMatching) << endl;
		for(int i = 0; i <= up; i++)
			g[i].clear();
	}
}
