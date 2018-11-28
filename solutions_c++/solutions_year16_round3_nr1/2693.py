#include <cstdio>
#include <queue>
#include <algorithm>
#include <vector>
#include <utility>
using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i)
	{
		priority_queue<pair<int, char> > pq;
		vector<char> v;
		int N, n;
		scanf("%d", &N);
		for (int j = 0; j < N; ++j)
		{
			scanf("%d", &n);
			if (n - 1 >0)
				pq.push(make_pair(n - 1, j + 'A'));
		}
		printf("Case #%d: ", i);
		while (!pq.empty())
		{
			pair<int, char> max_f = pq.top();
			pq.pop();
			printf("%c", max_f.second);
			max_f.first--;
			if (max_f.first > 0)
				pq.push(max_f);
			if (!pq.empty())
			{
				max_f = pq.top();
				pq.pop();
				printf("%c", max_f.second);
				max_f.first--;
				if (max_f.first > 0)
					pq.push(max_f);
			}
			printf(" ");
		}
		if (N % 2 == 1)
		{
			printf("%c ", 'A');
			for (int j = 1; j < N; j += 2)
				printf("%c%c ", j + 'A', j + 'A' + 1);
		}
		else
			for (int j = 0; j < N; j += 2)
				printf("%c%c ", j + 'A', j + 'A' + 1);
		printf("\n");
	}

}