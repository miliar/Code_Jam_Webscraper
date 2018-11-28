#include <cstdio>
int T,cas,x,n,m;

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	scanf("%d", &T);
	for (cas=1; cas<=T; ++cas)
	{
		printf("Case #%d: ", cas);
		scanf("%d%d%d", &x, &n, &m);
		if (n*m%x != 0)
		{
			printf("RICHARD\n");
			continue;
		}
		if (x <= 2)
		{
			printf("GABRIEL\n");
			continue;
		}
		if (x == 3)
		{
			if (n==1 || m==1)
			{
				printf("RICHARD\n");
				continue;
			}
			printf("GABRIEL\n");
			continue;
		}
		if (x == 4)
		{
			if (n<=2 || m<=2)
			{
				printf("RICHARD\n");
				continue;
			}
			printf("GABRIEL\n");
			continue;
		}
	}
	return 0;
}
			
