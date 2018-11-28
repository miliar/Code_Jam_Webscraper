#include <cstdio>

typedef long long LL;

const int Maxnum = 100000;

int tot;
int digit[32], d[11];
bool flag[Maxnum];
int prime[Maxnum];

int divisor(__int128 x)
{
	for (int i = 0; i < tot && prime[i] * prime[i] <= x; ++i)
		if (x % prime[i] == 0) return prime[i];
	return 1;
}

int main()
{
	int T, n, j;
	scanf("%d%d%d", &T, &n, &j);

	tot = 0;
	for (LL i = 2; i * i < Maxnum; ++i)
		if (!flag[i])
			for (int j = i + i; j < Maxnum; j += i)
				flag[j] = true;
	for (int i = 2; i < Maxnum; ++i)
		if (!flag[i]) prime[tot++] = i;
	//printf("%d\n", tot);
	//for (int i = 0; i < tot; ++i) printf("%d ", prime[i]);
	//printf("\n");

	puts("Case #1:");
	int x = 1;
	for (int i = 1; i < n; ++i)
		x <<= 1;
	x |= 1;
	while (j)
	{
		int y = x;
		for (int i = 0; i < n; ++i)
		{
			digit[i] = y & 1;
			y >>= 1;
		}
		int base = 2;
		while (base <= 10)
		{
			__int128 y = 0;
			for (int i = n - 1; i >= 0; --i)
				y = y * base + digit[i];
			d[base] = divisor(y);
			if (d[base] == 1) break;
			++base;
		}
		if (base > 10)
		{
			for (int i = n - 1; i >= 0; --i)
				printf("%d", digit[i]);
			for (int i = 2; i <= 10; ++i)
				printf(" %d", d[i]);
			printf("\n");
			--j;
		}
		x += 2;
	}
	return 0;
}
