#include <cstdio>

int gcd(int a, int b)
{
	if(a == 0)
		return b;
	return gcd(b % a, a);
}

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int casesCount;
	scanf("%d", &casesCount);

	for (int currentCase = 1; currentCase <= casesCount; currentCase++)
	{
		int p, q;
		scanf("%d/%d", &p, &q);
		printf("Case #%d: ", currentCase);
		if(p <= q)
		{
			int d = gcd(p, q);
			p /= d;
			q /= d;
			if(q == (q & -q))
			{
				int k = 1;
				p /= 2;
				while(p > 0)
				{
					q /= 2;
					p /= 2;
				}

				int sol = -1;
				while(q > 0)
				{
					sol++;
					q /= 2;
				}

				printf("%d\n", sol);
				continue;
			}
		}
		printf("impossible\n");
	}

	return 0;
}