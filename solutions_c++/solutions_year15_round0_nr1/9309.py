#include <cstdio>
#include <cstring>

int main() 
{
	freopen("inputLarge.txt", "r", stdin);
	freopen("outputLarge.txt", "w", stdout);
	int t, i, n, d, c, a;
	char sh[1005];
	scanf("%d", &t);
	for(d = 1; d <= t; d++)
	{
		printf("Case #%d: ", d);
		c = 0;
		a = 0;
		scanf("%d%s", &n, sh);
		for(i = 0; i <= n; i++)
		{
			if(c < i) a += i - c, c = i;
			c += sh[i] - '0';
		}
		printf("%d\n", a);
	}
	return 0;
}
