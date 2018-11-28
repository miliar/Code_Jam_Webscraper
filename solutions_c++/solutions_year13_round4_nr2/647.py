#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
using namespace std;

long long power(long long t)
{
	long long res = 1;
	for (long long i = 0; i < t; ++i) res *= 2;
	return res;
}

void run(int asdf)
{
	long long n, p;
	cin >> n >> p;
	printf("Case #%d: ", asdf);
	
	long long tot = power(n);
	{
		long long r = tot - p + 1;
		long long x = (long long)(log((double)(tot) / (double)(r)) / log(2.0));
		long long res1 = 0;
		for (long long i = 0; i < x; ++i) res1 = (res1 + 1) * 2;
		if (res1 > tot - 1) res1 = tot - 1;
		cout << res1 << ' ';
	}
	
	{
		long long x = n - (long long)(log((double)(p)) / log(2.0));
		long long res2 = tot - power(x);
		cout << res2 << '\n';
	}	
}

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		run(i);
	}
	return 0;
}