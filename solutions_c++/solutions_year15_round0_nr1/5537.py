#include <stdio.h>

int n, num[1010];
char lin[1010];

int main()
{
	int k, l;
	scanf("%d", &k);
	for(l = 0; l < k; l++)
	{
		scanf("%d", &n);
		scanf(" %s", lin);
		int i;
		for(i = 0; i <= n; i++)
			num[i] = lin[i] - '0';
		int ct = num[0], sol = 0;
		if(n == 0)
		{
			printf("Case #%d: 0\n", l + 1);
			continue;
		}
		for(i = 1; i <= n; i++)
		{
			if(num[i])
				while(ct + sol < i)
					sol++;
			ct += num[i];
		}
		printf("Case #%d: %d\n", l + 1, sol);
	}
	return 0;
}
