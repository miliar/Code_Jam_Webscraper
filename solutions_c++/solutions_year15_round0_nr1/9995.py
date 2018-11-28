#include <cstdio>
#include <iostream>
int main()
{
	//freopen("A-small-attempt2.in", "r", stdin);
	//freopen("A-small-attempt2.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		int smax, tmp;
		int s[1005];
		scanf("%d %d", &smax, &tmp);
		for (int k = smax; k >=0; k--)
		{
			s[k] = tmp % 10;
			tmp /= 10;
		}

		int cur = 0;
		int add = 0;
		for (int k = 0; k <= smax; k++)
		{
			if (cur < k)
			{
				add += k - cur;
				cur += k - cur + s[k];
			}
			else
				cur += s[k];
		}

		printf("Case #%d: %d\n", i, add);
	}
	return 0;
}