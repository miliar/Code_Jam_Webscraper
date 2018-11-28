#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
#include<set>
#include<memory.h>
#include<map>
#include<string>
#include<time.h>
using namespace std;

int n, j;

long long conv(long long s, int a)
{
	long long p = 1;
	long long d = 0;
	while (s) d += (s % 10)*p, p *= a, s/=10;
	return d;
}

long long mul(long long x, long long y, long long m)
{
	if (!y) return 0;
	if (y % 2) return (x + mul(x, y - 1, m)) % m;
    long long k = mul(x, y / 2, m);
	return (k + k) % m;
}

long long power(long long x, long long y, long long m)
{
	if (!y) return 1;
	if (y % 2) return mul(x, power(x, y - 1, m), m);
	long long k = power(x, y / 2, m);
	return mul(k, k, m);
}

bool prime(long long n)
{
	if (n == 1) return false;
	if (n == 2) return true;

	for (long long i = 2; i < 10000000 && i*i <= n; ++i) if (n%i == 0) return false;

	long long t = n - 1;
	int s = 0;
	while (t % 2 == 0) t /= 2, s++;

	for (int i = 0; i < 200; ++i)
	{
		long long a = (((long long)rand()*(long long)rand()*(long long)rand()*(long long)rand()*(long long)rand()*(long long)rand()) % (n - 3) + (n-3))%(n-3)+2;
		long long x = power(a, t, n);
		if (x == 1 || x == n - 1) continue;
		bool pr = true;
		for (int j = 1; j < s; ++j)
		{
			x = mul(x, x, n);
			if (x == 1) return false;
			if (x == n - 1)
			{
				pr = false;
				break;
			}
		}
		if (pr) return false;
	}
	return true;
}

long long gcd(long long x, long long y)
{
	return y ? gcd(y, x%y) : x;
}

long long pollard_rho(long long n, unsigned iterations_count = 30000)
{

	for (int i = 2; i < 10000000;++i)
	if (n%i==0) return i;



	long long
		b0 = (((long long)rand()*(long long)rand()*(long long)rand()*(long long)rand()*(long long)rand()*(long long)rand()) % n + n) % n,
		b1 = b0,
		g;
	mul(b1, b1, n);
	if (++b1 == n)
		b1 = 0;
	g = gcd(abs(b1 - b0), n);
	for (unsigned count = 0; count<iterations_count && (g == 1 || g == n); count++)
	{
		mul(b0, b0, n);
		if (++b0 == n)
			b0 = 0;
		mul(b1, b1, n);
		++b1;
		mul(b1, b1, n);
		if (++b1 == n)
			b1 = 0;
		g = gcd(abs(b1 - b0), n);
	}
	return g;
}


set<long long> used;

void solve()
{
	srand(123123);
	cin >> n >> j;
	//printf("%d\n", prime(n));
	//return;
	while (j)
	{
		long long x = 1;
		for (int i = 0; i < n - 2; ++i)
			x = x * 10 + (rand() % 2);
		x = x * 10 + 1;
		bool good = true;
		for (int i = 2; i <= 10; ++i)
		if (prime(conv(x, i)))
		{
			good = false;
			break;
		}
		if (!good) continue;
		if (used.find(x) != used.end()) continue;
		printf("%lld", x);
		for (int i = 2; i <= 10; ++i)
		{
			long long cv = conv(x, i);
			long long y = pollard_rho(cv);
			if (cv%y || y == 1 || y == cv)
			{
				printf(" [ ");
				printf("%lld %lld", cv, y);

				printf(" ] ");
			}
			printf(" %lld", y);
		}
		printf("\n");
		j--;
		used.insert(x);
	}
}

int main()
{
	ios::sync_with_stdio(0);
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int test = 1; test <= t; ++test)
	{
		printf("Case #%d:\n", test);
		solve();
	}
	return 0;
}