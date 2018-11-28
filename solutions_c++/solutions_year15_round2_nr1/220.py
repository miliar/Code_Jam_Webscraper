#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>

using namespace std;

unsigned long long p10[1024];
unsigned long long d[1024];

unsigned long long solve(unsigned long long n)
{
	if (n <= 20)
		return n;
	int len = 0;
	unsigned long long t = 0;
	for (len = 0; n >= p10[len]; ++len)
		t = t * 10 + n / p10[len] % 10;
	t %= p10[len >> 1];
	if (t == 1)
		t = 0;
	return d[len] + t + n % p10[(len+1) >> 1];
}

int main()
{
	p10[0] = 1;
	for (int i = 0; ++i < 1024; )
		p10[i] = p10[i-1] * 10;
	d[0] = 0;
	d[1] = 1;
	d[2] = 10;
	for (int i = 2; ++i < 1024; )
		d[i] = d[i-1] + p10[i >> 1] + p10[(i-1) >> 1] - 1;
	int itest, ntest;
	scanf("%d", &ntest);
	for (itest = 0; ++itest <= ntest; )
	{
		unsigned long long n;
		scanf("%llu", &n);
		printf("Case #%d: %llu\n", itest, n % 10? solve(n): solve(n-1) + 1);
	}
	return 0;
}
