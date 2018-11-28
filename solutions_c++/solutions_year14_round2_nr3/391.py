#include <iostream>
#include <string>
#include <vector>
using namespace std;


int n;
string best;
bool rm[8][8];
bool visited[8];
vector<string> strs;
int old[8];


void solve(const string &cur, int k, int mk)
{
	if (visited[k])
		return;
	visited[k] = true;
	int o = old[mk];
	old[mk] = k;
	string s = cur + strs[k];
	if (s.size() == 5 * n)
	{
		if (s < best)
			best = s;
	}
	else
	{
		for (int i = 0; i <= mk; ++i)
		{
			int a = old[i];
			for (int j = 0; j < n; ++j)
			{
				if (rm[a][j])
				{
					solve(s, j, i+1);
				}
			}
		}
	}
	old[mk] = o;
	visited[k] = false;
}

int main(void)
{
	int cases;
	cin >> cases;
	for (int t = 0; t < cases; ++t)
	{
		int m;
		cin >> n >> m;
		strs.resize(n);
		for (int i = 0; i < n; ++i)
			cin >> strs[i];
		vector<vector<int> > routes(n);
		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < n; ++j)
				rm[i][j] = false;
			visited[i] = false;
		}
		for (int i = 0; i < m; ++i)
		{
			int a, b;
			cin >> a >> b;
			--a; --b;
			routes[a].push_back(b);
			routes[b].push_back(a);
			rm[a][b] = true;
			rm[b][a] = true;
		}
		best = string(5*n, '9');
		for (int i = 0; i < n; ++i)
		{
			solve("", i, 0);
		}

		cout << "Case #" << (t + 1) << ": " << best << endl;
	}
	return 0;
}
