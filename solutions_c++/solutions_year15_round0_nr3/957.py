#include <stdio.h>


int opans[4][4] = {
	{ 0, 1, 2, 3, },
	{ 1, 0+4, 3, 2+4, },
	{ 2, 3+4, 0+4, 1, },
	{ 3, 2, 1+4, 0+4, },
};

int op(int a, int b)
{
	int ret = opans[a & 3][b & 3] ^ (a & 4) ^ (b & 4);
	return ret;
}

int op(int a, char *first, char *last)
{
	int ret = a;
	for (; first != last; ++first)
		ret = op(ret, *first - 'i' + 1);
	return ret;
}

int n; // Called L in the problem description
char str[10001];

bool search(int &pos, long long &x, int start, int to_find)
{
	int val = start;
	for (int i = 0; i < 16 && x > 0; ++i, --x) // Should repeat within 4 cycles, use more than 8 to be certain
	{
		for (; pos < n; ++pos)
		{
			val = op(val, str+pos, str+pos+1);
			if (val == to_find)
			{
				++pos;
				if (pos == n)
				{
					pos = 0;
					--x;
				}
				return true;
			}
		}
		pos = 0;
	}
	return false;
}

bool doit()
{
	long long x;
	scanf("%d %lld %s", &n, &x, str);
	// Start from beginning to find i
	int pos = 0;
	if (!search(pos, x, 0, 1)) // i
		return false;
	// printf("%lld %d\n", x, pos);
	if (!search(pos, x, 0, 2)) // j
		return false;
	// printf("%lld %d\n", x, pos);
	if (!search(pos, x, 0, 3)) // k
		return false;
	// printf("%lld %d\n", x, pos);
	x %= 16; // Remove multiples of 16. Not useful anyway.
	while (x > 0 || pos != 0)
	{
		if (!search(pos, x, 3, 3)) // Just append digits to k so that the whole string is used
			return false;
	}
	return true;
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; ++i)
	{
		bool ret = doit();
		printf("Case #%d: %s\n", i+1, (ret ? "YES" : "NO"));
	}
	return 0;
}
