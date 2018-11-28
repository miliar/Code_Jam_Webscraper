#include <cstdio>

int p[1000];

int main()
{
	int T;
	scanf("%d", &T);

	for (int t = 1; t <= T; ++t)
	{
		int d;
		scanf("%d", &d);

		int maxCakes = 0;
		for (int i = 0; i < d; ++i)
		{
			scanf("%d", &p[i]);

			if (p[i] > maxCakes)
			{
				maxCakes = p[i];
			}
		}

		int minMinute = 1001;
		for (int i = 1; i <= maxCakes; ++i)
		{
			int minute = 0;
			for (int j = 0; j < d; ++j)
			{
				int moveTimes = p[j] / i;
				if (moveTimes * i == p[j])
				{
					--moveTimes;
				}

				minute += moveTimes;
			}
			
			minute += i;
			if (minute < minMinute)
			{
				minMinute = minute;
			}
		}

		printf("Case #%d: %d\n", t, minMinute);
	}

	return 0;
}
