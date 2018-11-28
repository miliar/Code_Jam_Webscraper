#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t, n, a;
	scanf("%d", &t);
	for (int tc = 1; tc <= t; ++tc)
	{
		scanf("%d", &n);
		priority_queue<pair<int, int> > pq;
		for (int i = 0; i < n; ++i)
		{
			scanf("%d", &a);
			pq.push({a, i});
		}
		printf("Case #%d:", tc);
		while (!pq.empty())
		{
			pair<int, int> u = pq.top();
			pq.pop();
			if (u.first == 1)
			{
				if (pq.size() == 2)
				{
					printf(" %c", u.second + 'A');
				}
				else
				{
					pair<int, int> v = pq.top();
					pq.pop();
					printf(" %c%c", u.second + 'A', v.second + 'A');
				}
			}
			else
			{
				pq.push({u.first - 1, u.second});
				pair<int, int> v = pq.top();
				pq.pop();
				if (v.first == 1 && pq.size() == 1)
				{
					printf(" %c", u.second + 'A');
					pq.push(v);
				}
				else
				{
					printf(" %c%c", u.second + 'A', v.second + 'A');
					if (v.first > 1)
					{
						pq.push({v.first - 1, v.second});
					}
				}
			}
		}
		printf("\n");
	}
	return 0;
}