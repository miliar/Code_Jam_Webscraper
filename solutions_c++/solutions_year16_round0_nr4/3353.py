#define _SCL_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS
#include <stdlib.h>
#include <conio.h>
#include <stdio.h>
#include <string.h>

#define SOLVE_LARGE

#define IN_FILE_NAME "D-small-attempt0.in"
#define OUT_FILE_NAME "D-small-attempt0.out"

//#define IN_FILE_NAME "D-large.in"
//#define OUT_FILE_NAME "D-large.out"

void SolveLarge(int t, int k, int c, int s)
{
	int need = (k - c + 1);

	if (need < 1)
		need = 1;

	if (s < need)
	{
		printf("Case #%d: IMPOSSIBLE\n", t + 1);
		return;
	}

	if (c > k)
		c = k;

	unsigned long long pos = 0;
	unsigned long long pow = 1;

	for (int i = 1; i <= c - 2; i++)
	{
		pow *= k;
	}

	for (int i = c - 2; i >= 1; i--)
	{
		pos += pow * (c - i - 1);
		pow /= k;
	}

	pos += c;

	printf("Case #%d: ", t + 1);
	for (int i = 0; i < need; i++)
	{
		printf("%llu ", pos + i);
	}
	printf("\n");
}

// Good only for s == k
void SolveSmall(int t, int k, int c, int s)
{
	printf("Case #%d: ", t + 1);
	for (int i = 1; i <= k; i++)
	{
		printf("%d ", i);
	}
	printf("\n");
}

int main()
{
	freopen(IN_FILE_NAME, "r", stdin);
	freopen(OUT_FILE_NAME, "w", stdout);

	int t, tests;
	scanf("%d", &tests);

	for (t = 0; t < tests; t++)
	{
		int k, c, s;

		scanf("%d %d %d", &k, &c, &s);

#ifdef SOLVE_LARGE
		SolveLarge(t, k, c, s);
#else
		SolveSmall(t, k, c, s);
#endif
	}


	return 0;
}