/*Senate Evacuation*/

#include<cstdio>
#include<queue>
#include<vector>
#include<utility>
#include<functional>

using namespace std;

int main()
{
	int i, N, P, t, T;
	pair<int, char> current, next;
	priority_queue< pair<int, char>, vector< pair<int, char> > > q;
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &T);
	for (t = 1; t <= T; t++)
	{
		scanf("%d", &N);
		for (i = 0; i < N; i++)
		{
			scanf("%d", &P);
			if (P > 0)
				q.push(make_pair(P, (char)('A' + i)));
		}
		printf("Case #%d:", t);
		while (!q.empty())
		{
			current = q.top();
			q.pop();
			if (current.first == 1)
			{
				q.push(current);
				break;
			}
			if ((q.empty()) || (current.first > q.top().first))
			{
				printf(" %c", current.second);
				if (current.first > 1)
					q.push(make_pair(current.first - 1, current.second));
			}
			else
			{
				next = q.top();
				q.pop();
				printf(" %c%c", current.second, next.second);
				if (current.first > 1)
				{
					q.push(make_pair(current.first - 1, current.second));
					q.push(make_pair(next.first - 1, next.second));
				}
			}
		}
		while (q.size() > 2)
		{
			current = q.top();
			q.pop();
			printf(" %c", current.second);
		}
		current = q.top();
		q.pop();
		next = q.top();
		q.pop();
		printf(" %c%c\n", current.second, next.second);
	}
	return 0;
}