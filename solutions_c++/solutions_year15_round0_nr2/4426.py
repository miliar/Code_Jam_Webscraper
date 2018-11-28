#include <iostream>
#include <cstdio>
#include <queue>
using namespace std;

priority_queue<int> q;

int main(int argc, char *argv[])
{
	freopen(argv[1], "r", stdin);
	freopen(argv[2], "w", stdout);

	int T, D, P, m;
	cin >> T;
	for (int k = 1; k <= T; ++k)
	{
		priority_queue<int> qq;
		cin >> D;
		for (int i = 0; i < D; ++i)
		{
			cin >> P;
			qq.push(P);
		}

		for (int m = 1; m <= 1000; ++m)
		{
			bool done = false;
			for (int t = 0; t < m; ++t)
			{
				bool ok = false;
				q = qq;
				for (int i = 0; i <= t; ++i)
				{
					int x = q.top();
					q.pop();
					if (x <= m - t)
					{
						ok = true;
						break;
					}
					q.push(m - t);
					q.push(x - m + t);
				}
				if (ok)
				{
					done = true;
					break;
				}
			}
			if (done)
			{
				printf("Case #%d: %d\n", k, m);
				break;
			}
		}
	}

	return 0;
}
