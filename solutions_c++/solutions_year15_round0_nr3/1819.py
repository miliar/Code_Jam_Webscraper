#include <cstdio>
#include <cstring>

const int a[4][4] = {
	{1, 2, 3, 4},
	{2, -1, 4, -3},
	{3, -4, -1, 2},
	{4, 3, -2, -1}};

char s[10001], ss[10001];

int main()
{
	int T;
	scanf("%d", &T);

	for (int t = 1; t <= T; ++t)
	{
		int l, x;
		scanf("%d %d", &l, &x);
		scanf("%s", ss);

		s[0] = 0;
		for (int i = 0; i < x; ++i)
		{
			strcat(s, ss);
		}

		int value = 1;
		bool flag = false;
		int target = 2;
		int len = l * x;
		for (int i = 0; i < len; ++i)
		{
			value = a[value - 1][s[i] - 103 - 1];
			if (value < 0)
			{
				value = -value;
				flag = !flag;
			}

			if (value == target && !flag)
			{
				++target;
				value = 1;
			}
		}

		printf("Case #%d: ", t);
		if (target == 5 && value == 1 && !flag)
		{
			printf("YES\n");
		}
		else
		{
			printf("NO\n");
		}
	}

	return 0;
}
