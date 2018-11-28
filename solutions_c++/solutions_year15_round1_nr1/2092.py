#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define MAXN 2000

int time[MAXN];

int max(int x, int y)
{
	return x > y ? x : y;
}

int min(int x, int y)
{
	return x < y ? x : y;
}

int main()
{
	int T;
	scanf("%d", &T);

	for (int test = 1; test <= T; test++)
	{
		int n;
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
			scanf("%d", &time[i]);

		// method 1
		int ans = 0;
		for (int i = 1; i < n; i++)
			ans += max(0, time[i - 1] - time[i]);
		
		printf("Case #%d: %d ", test, ans);

		//method 2
		double speed = 0;
		for (int i = 1; i < n; i++)
			if (time[i - 1] > time[i])
			{
				double newspeed = (time[i - 1] - time[i]) / 10.0;
				speed = newspeed > speed ? newspeed : speed;
			}

		ans = 0;
		for (int i = 0; i < n - 1; i++)
			ans += min(time[i], speed * 10);
		printf("%d\n", ans);
	}

	return 0;
}
