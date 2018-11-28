#include <bits/stdc++.h>
using namespace std;

char str[1111];

int main()
{
	int T, N, K, ans;
	bool pos;
	deque<int> dq;

	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		scanf("%s%d", str, &K);
		
		N = strlen(str);
		dq.clear();
		ans = 0;
		pos = true;

		for (int i = 0; i < N; i++)
		{
			while (!dq.empty() && dq.front() <= i - K)
				dq.pop_front();
			if (dq.size() & 1)
				str[i] = (str[i] == '+' ? '-' : '+');
			if (i <= N - K && str[i] == '-')
			{
				dq.push_back(i);
				str[i] = '+';
				ans++;
			}
			if (str[i] == '-')
				pos = false;
		}
		printf("Case #%d: ", t);
		if (pos)
			printf("%d\n", ans);
		else
			printf("IMPOSSIBLE\n");
	}

	return 0;
}