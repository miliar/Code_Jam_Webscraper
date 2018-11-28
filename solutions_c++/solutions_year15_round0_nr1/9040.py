#include <cstdio>

int main()
{
	int ncases, max, invited, sum;
	char s[1010];
	scanf("%d", &ncases);
	for (int t = 1; t <= ncases; t++)
	{
		invited = 0;
		sum = 0;
		scanf("%d %s", &max, &s);
		for (int i = 0; i <= max; i++)
		{
			if (sum < i)
			{
				invited += i - sum;
				sum += i - sum;
			}
			sum += s[i] - '0';

		}
		printf("Case #%d: %d\n", t, invited);
	}
	return 0;
}