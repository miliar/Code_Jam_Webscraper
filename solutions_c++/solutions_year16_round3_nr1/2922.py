#include <bits/stdc++.h>
using namespace std;

int main() {
	int tc;
	scanf("%d", &tc);
	for (int nc = 1; nc <= tc; nc++)
	{
		printf("Case #%d:", nc);
		int n;
		int t = 0;
		scanf("%d", &n);
		priority_queue<pair<int, int> > pq;
		for (int i = 0; i < n; i++)
		{
			int a;
			scanf("%d", &a);
			t += a;
			pq.push(make_pair(a, i));
		}
		while (!pq.empty())
		{
			pair<int, int> x = pq.top(); pq.pop();
			printf(" %c", 'A' + x.second);
			t--;
			if (x.second - 1 > t -1 && t > 2) {
				printf("\t%d %d\n", x.second, t);
				printf(" %c", 'A' + x.second);
				t--;
				pq.push(make_pair(x.first - 2, x.second));
				continue;
			}
			if (!pq.empty() && t != 2) {
				pair<int, int> y = pq.top(); pq.pop();
				printf("%c", 'A' + y.second);
				t--;
				if (y.first > 1)
					pq.push(make_pair(y.first - 1, y.second));
			}
			if (x.first > 1)
				pq.push(make_pair(x.first - 1, x.second));
		}
		printf("\n");
	}
	return 0;
}