#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <cmath>
#include <utility>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <sstream>
using namespace std;
const int BASE = 1000002013;

int main()
{
	freopen("alarge.in", "r", stdin); 
	freopen("alarge.out", "w", stdout);
	int test, x, y, z, n, m;
	cin >> test;
	for (int itest = 1; itest <= test; itest++)
	{
		long long initialCost = 0;
		vector < pair< pair<int,int>,int> > a;
		cin >> n >> m;
		for (int i = 0; i < m; i++)
		{
			cin >> x >> y >> z;
			a.push_back(make_pair(make_pair(x, 0), z));
			a.push_back(make_pair(make_pair(y, 1), z));
			int dist = y - x;
			initialCost += (2LL * n - dist + 1) * dist / 2 % BASE * z % BASE;
			initialCost %= BASE;
		}
		
		long long bestCost = 0;
		int last = 0;
		pair <int,int> st[1010];
		sort(a.begin(), a.end());
		
		for (int i = 0; i < m * 2; i++)
			if (!a[i].first.second) st[++last] = make_pair(a[i].first.first, a[i].second);
			else
			{
				int xx = a[i].first.first, zz = a[i].second;
				while (zz)
				{
					int x = st[last].first, z = st[last].second;
					int use = min(z, zz), dist = xx - x;
					bestCost += (2LL * n - dist + 1) * dist / 2 % BASE * use % BASE;
					bestCost %= BASE;
					st[last].second -= use;
					zz -= use;
					if (!st[last].second) last--;
				}
			}
			
		printf("Case #%d: ", itest);
		cout << (initialCost - bestCost + BASE) % BASE << endl;
	}
}
