#include<cstdio>

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, k,c,s;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		printf("Case #%d:", t);
		scanf("%d %d %d", &k, &c, &s);
		if (c == 1)
		{
			if (s < k) printf(" IMPOSSIBLE\n");
			else
			{
				for (int i = 1; i <= s; i++) printf(" %d", i);
				printf("\n");
			}
		}
		else
		{
			if (s < (k + 1) / 2) printf(" IMPOSSIBLE\n");
			else
			{
				long long p = 2;
				for (int i = 0; i < k / 2; i++)
				{
					printf(" %lld", p);
					p += 2 * k + 2;
				}
				if (k % 2) printf(" %lld", (long long)k*k);
				printf("\n");
			}
		}
	}
}