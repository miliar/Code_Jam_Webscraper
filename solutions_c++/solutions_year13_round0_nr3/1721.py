#include <cstdio>

bool CheckIfPal(long long v)
{
	int j, tab[20], vp;

	vp = 0;
	while (v)
	{
		tab[vp++] = v % 10;
		v /= 10;
	}

	for (j = 0; j < vp / 2; j++)
	{
		if (tab[j] != tab[vp-j-1])
		{
			return false;
		}
	}

	return true;
}

int main()
{
	int t, test, count;
	int i, j, pal[11000], palp;
	long long A, B, l;

	for (i = 1, palp = 0; i <= 10000000; i++)
	{
		if (CheckIfPal(i))
		{
			pal[palp++] = i;
		}
	}

	scanf("%d", &t);
	for (test = 1; test <= t; test++)
	{
		scanf("%lld", &A);
		scanf("%lld", &B);

		for (j = 0, count = 0; j <= palp; j++)
		{
			l = ((long long)pal[j]) * ((long long)pal[j]);
			if (l >= A && l <= B && CheckIfPal(l))
			{
				count++;
			}
			else if (l > B)
			{
				break;
			}
		}

		printf("Case #%d: %d\n", test, count);
	}

	return 0;
}
