#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <bitset>
#include <vector>
using namespace std;
const int N = 1e4;
int f[N];
vector<int> P;
long long mpow(long long x, long long n, long long mod)
{
	long long res = 1;
	while (n)
	{
		if (n & 1) res = (res * x) % mod;
		n >>= 1;
		x = (x * x) % mod;
	}
	return res;
}
long long vise(long long x, int b)
{
	long long tmp = 0, bit = 1;
	while (x)
	{
		tmp += (x & 1) * bit;
		x >>= 1;
		bit = bit * b;
	}
	return tmp;
}
long long is_prime(long long n, int b)
{
	for (int i : P)
	{
		//if (1LL * i * i > n) return -1;
		if ((n % i + mpow(b, 31, i)) % i == 0) return i;
	}
	return -1;
}
bool check(long long n)
{
	for (int i = 2; i <= 10; ++ i)
	{
		if (is_prime(vise(n, i), i) == -1) return 0;
	}
	return 1;
}
int main()
{
	puts("Case #1:");
	for (int i = 2; i < N; ++ i)
	{
		if (!f[i])
		{
			P.push_back(i);
			for (long long j = 1LL * i * i; j < N; j += i) f[j] = i;
		}
	}
	int cnt = 0;
	for (int i = 0; i < (1 << 30); ++ i)
	{
		int tmp = (i << 1) + 1;
		if (check(tmp))
		{
			cnt ++;
			putchar('1');
			for (int j = 30; j >= 0; -- j) putchar((tmp >> j & 1) ? '1' : '0');
			for (int j = 2; j <= 10; ++ j)
			{
				printf(" %d", (int) is_prime(vise(tmp, j), j));
			}
			puts("");
			if (cnt == 500) break;
		}
	}
	return 0;
}

