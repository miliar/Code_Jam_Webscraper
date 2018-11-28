#include <stdio.h>


int main()
{
	int t, c, i, j;
	int n, x, possible[16], ans;
	
	scanf("%d", &t);
	for (c = 1; c <= t; c++)
	{
		for (i = 0; i < 16; i++) possible[i] = 0;
		ans = -1;
		scanf("%d", &n);
		for (i = 0; i < 4; i++)
			for (j = 0; j < 4; j++)
			{
				scanf("%d", &x);
				if (n == i + 1)
					possible[x-1] = 1;
			}
		scanf("%d", &n);
		for (i = 0; i < 4; i++)
			for (j = 0; j < 4; j++)
			{
				scanf("%d", &x);
				if (n == i + 1 && possible[x-1])
				{
					if (ans != -1) ans = -2;
					else ans = x;
				}
			}
	
		printf("Case #%d: ", c);
		if (ans >= 0) printf("%d\n", ans);
		else if (ans == -1) puts("Volunteer cheated!");
		else puts("Bad magician!");
	}
	return 0;
}
