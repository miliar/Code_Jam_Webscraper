#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <iostream>
#include <queue>
#include <string>
#include <ctime>
#include <map>

using namespace std;

int n, x;
int a[100005];
multiset<int> s;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int t;
	scanf("%d", &t);
	for (int tt = 0; tt < t; tt++)
	{
		s.clear();
		scanf("%d%d", &n, &x);
		for (int i = 0; i < n; i++)
			scanf("%d", &a[i]), s.insert(-a[i]);
		
		int ans = 0;
		while (s.size() > 0)
		{
			int val = *s.begin();
			s.erase(s.begin());
			ans++;

			multiset<int>::iterator it = s.lower_bound(-x - val);
			if (it != s.end())
				s.erase(it);
		}

		printf("Case #%d: %d\n", tt + 1, ans);
	}


	return 0;
}