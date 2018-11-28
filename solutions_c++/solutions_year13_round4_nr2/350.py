#include <stdio.h>

int n;
long long p;

long long f1(long long a, int n)
{ return a ? (1LL << (n - 1)) + f1((a + 1) / 2 - 1, n - 1) : 0; }

long long f2(long long a, int n)
{ return a < ((1LL << n) - 1) ? f2((a + 1) / 2, n - 1) : ((1LL << n) - 1); }

long long solve1()
{
	long long l = 0, r = (1LL << n) - 1, mid;
	while (l < r) {
		if (f1(mid = l + ((r - l + 1) >> 1), n) < p) l = mid;
		else r = mid - 1;
	}
	return l;
}

long long solve2()
{
	long long l = 0, r = (1LL << n) - 1, mid;
	while (l < r) {
		if (f2(mid = l + ((r - l + 1) >> 1), n) < p) l = mid;
		else r = mid - 1;
	}
	return l;
}

int main()
{
	int dat;
	scanf("%d", &dat);
	for (int k = 1; k <= dat; ++k) {
		scanf("%d%lld", &n, &p);
		printf("Case #%d: %lld %lld\n", k, solve1(), solve2());
	}
}
