#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
const int MAXSMAX = 1000;
char s[MAXSMAX + 2];
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, i, smax, j, c, result;
	scanf("%d", &t);
	for (i = 1; i <= t; i++)
	{
		scanf("%d%s", &smax, s);
		c = 0;
		result = 0;
		for (j = 0; j <= smax; j++)
		{
			if (c < j)
			{
				result += j - c;
				c = j;
			}
			c += s[j] - '0';
		}
		printf("Case #%d: %d\n", i, result);
	}
	return 0;
}