#include <iostream>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <algorithm>
#include <queue>
using namespace std;

int get_count(int x)
{
	int cnt = 0;
	for (int i = 0; i < 30; i++)
	{
		if ((x >> i) & 1) cnt++;
	}
	return cnt;
}

int main()
{
#if !ONLINE_JUDGE
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
#endif

	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int t;
	cin >> t;


	for (int z = 1; z <= t; z++)
	{
		int n;
		cin >> n;
		vector <pair <string, string> > v(n);
		set <string> uf, us;

		for (int i = 0; i < n; i++)
		{
			cin >> v[i].first >> v[i].second;
			uf.insert(v[i].first);
			us.insert(v[i].second);
		}
		int res = v.size();
		for (int i = 0; i < (1 << v.size()) - 1; i++)
		{
			set <string> ufo, uso;
			for (int j = 0; j < v.size(); j++)
			{
				if ((i >> j) & 1)
				{
					ufo.insert(v[j].first);
					uso.insert(v[j].second);
				}
			}

			if (ufo.size() == uf.size() && uso.size() == us.size())
			{
				int ans = get_count(i);
				res = min(res, ans);
			}

			
		}

		cout << "Case #" << z << ": " << v.size() - res << endl;
	}
	return 0;
}