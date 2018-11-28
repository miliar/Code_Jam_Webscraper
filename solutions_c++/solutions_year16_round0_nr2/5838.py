#include <stdio.h>
#include <string.h>

int n;
char lin[110];

int main()
{
	scanf("%d", &n);
	int k;
	for(k = 0; k < n; k++)
	{
		scanf(" %s", lin);
		int i, ans = 0, l = strlen(lin);
		for(i = 0; i < l; i++)
			if(lin[i] == '-')
				ans = 1, lin[i] = '+';
			else
				break;
		int cur = 0;
		for(i = 0; i < l; i++)
		{
			if(lin[i] == '+')
			{
				if(cur)
					cur = 0, ans += 2;
			}
			else
				if(cur == 0)
					cur = 1;
		}
		if(cur)
			ans += 2;
		printf("Case #%d: %d\n", k + 1, ans);
	}
	return 0;
}
