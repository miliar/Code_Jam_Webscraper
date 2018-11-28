#include <bits/stdc++.h>

using namespace std;

int n, J;

vector<int> prime;
bitset<100000000> bs;

int factor(long long x)
{
	for (int i = 0; i < prime.size() && (long long) prime[i] * prime[i] <= x; ++i)
	{
		if (x % prime[i] == 0) return prime[i];
	}
	return -1;
}

long long power[11][32];
int fact[11];

int main()
{
	prime.push_back(2);
	for (int i = 3; i < 100000000; i += 2)
		if (!bs[i])
		{
			prime.push_back(i);
			for (long long j = (long long) i * i; j < 100000000; j += i + i)
				bs[j] = 1;
		}

	for (int i = 2; i < 11; ++i)
	{
		power[i][0] = 1;
		for (int j = 1; j < 32; ++j)
		{
			power[i][j] = power[i][j - 1] * i;
		}
	}

	int t;
	scanf("%d", &t);
	for (int tc = 1; tc <= t; ++tc)
	{
		scanf("%d %d", &n, &J);
		printf("Case #%d:\n", tc);
		n--;
		for (int i = (1 << (n - 1)); J && i < (1 << n); ++i)
		{
			long long val[11] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1};
			for (int j = 0; j < n; ++j)
			{
				if (i & (1 << j))
				{
					for (int k = 2; k < 11; ++k)
					{
						val[k] += power[k][j + 1];
					}
				}
			}

			bool can = true;
			for (int k = 2; can && k < 11; ++k)
			{
				if ((fact[k] = factor(val[k])) == -1)
				{
					can = false;
				}
			}

			if (can)
			{
				--J;
				for (int j = n - 1; j >= 0; --j)
				{
					printf("%c", (i & (1 << j)) ? '1' : '0');
				}
				printf("1");
				for (int j = 2; j < 11; ++j)
					printf(" %d", fact[j]);
				printf("\n");
			}
		}
	}
	return 0;
}