#include <cstdio>
#include <cstring>
int T, N,cnt,temp;
int visited[10];
int main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	for (int testcase = 1; testcase <= T; testcase++)
	{
		memset(visited, 0, sizeof(visited));
		scanf("%d", &N);
		printf("Case #%d: ", testcase);
		if (N == 0)
		{
			puts("INSOMNIA");
			continue;
		}
		temp = N;
		cnt = 0;
		while (temp)
		{
			int here = temp % 10;
			temp /= 10;
			if (visited[here]) continue;
			cnt++;
			visited[here]=1;
		}
		int cur = N;
		while (cnt != 10)
		{
			cur += N;
			temp = cur;
			while (temp)
			{
				int here = temp % 10;
				temp /= 10;
				if (visited[here]) continue;
				cnt++;
				visited[here] = 1;
			}
		}
		printf("%d\n", cur);
	}
}