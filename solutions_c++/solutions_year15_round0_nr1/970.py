#include <stdio.h>

int doit()
{
	int smax;
	char ss[1024];
	scanf("%d %s", &smax, ss);
	int ret = 0;
	int sum = 0;
	for (int i = 0; i <= smax; ++i)
	{
		if (ss[i] != '0')
		{
			if (sum < i)
			{
				ret += i - sum;
				sum = i;
			}
			sum += ss[i] - '0';
		}
	}
	return ret;
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; ++i)
	{
		int ret = doit();
		printf("Case #%d: %d\n", i+1, ret);
	}
	return 0;
}
