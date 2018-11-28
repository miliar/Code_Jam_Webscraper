#include <stdio.h>
#include <string.h>

long long int t, n, vis[20];

int main()
{
	scanf("%lld", &t);
	long long int k, i;
	for(k = 0; k < t; k++)
	{
		memset(vis, 0, sizeof vis);
		scanf("%lld", &n);
		if(n == 0)
		{
			printf("Case #%lld: INSOMNIA\n", k + 1);
			continue;
		}
		int ct = 10;
		for(i = 1; ct; i++)
		{
			long long int a = i * n;
			while(a)
			{
				if(vis[a % 10] == 0)
					vis[a % 10] = 1, ct--;
				a /= 10;
			}
		}
		printf("Case #%lld: %lld\n", k + 1, (i - 1) * n);
	}
	return 0;
}
