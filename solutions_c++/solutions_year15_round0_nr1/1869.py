#include <cstdio>
#include <cstring>

char str[2000];

int main()
{
	int T;
	scanf("%d", &T);
	for(int cas = 1; cas <= T; ++cas)
	{
		printf("Case #%d: ", cas);
		int n;
		scanf("%d", &n);
		scanf("%s", str);
		int ans = 0, tot = 0;
		for(int i = 0; i <= n; ++i)
		{
			if(tot < i)
			{
				ans += i - tot;
				tot = i;
			}
			tot += str[i] - '0';
		}
		printf("%d\n", ans);
	}
	return 0;
}
