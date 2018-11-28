#include <cstdio>
#include <cstring>

int p[20];

int main()
{
	int T;
	scanf("%d", &T);

	int n = 4, x, r;

	for (int t = 1; t <= T; ++t)
	{
		memset(p, 0, sizeof(p));
		scanf("%d", &r);
		--r;
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < n; ++j)
			{
				scanf("%d", &x);
				if (i == r)
					++p[x];
			}
		scanf("%d", &r);
		--r;
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < n; ++j)
			{
				scanf("%d", &x);
				if (i == r)
					++p[x];
			}
		printf("Case #%d: ", t);
		int ans = 0;
		for (int i = 1; i <= 16; ++i)
			if (p[i] == 2) 
			{
				if (ans != 0)
				{
					ans = -1;
					break;
				}
				ans = i;
			}
		if (ans == 0)
			printf("Volunteer cheated!\n");
		else if (ans == -1)
			printf("Bad magician!\n");
		else 
			printf("%d\n", ans);
	}

	return 0;
}
