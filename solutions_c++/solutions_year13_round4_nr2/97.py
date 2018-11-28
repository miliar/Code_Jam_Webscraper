#include <stdio.h>

int n;
long long p;

long long solve1 (long long x, long long n)
{
	if (!x) return 1;
	return solve1 ((x-1)/2, n/2) + n/2;
}

long long solve2 (long long x, long long n)
{
	if (x+1==n) return n;
	return solve2 ((x+1)/2, n/2);
}

int main()
{
	int t, tt=0;

	freopen ("b.in", "r", stdin);
	freopen ("b.out", "w", stdout);

	scanf ("%d", &t);
	while (t--) {
		scanf ("%d%lld", &n, &p);

		long long a1=0, a2=0;
		long long low=0, high=(1LL<<n)-1;
		long long mid;

		while (low<=high) {
			mid = (low+high)/2;
			if (solve1(mid, 1LL<<n) <= p) {
				a1 = mid;
				low=mid+1;
			}
			else 
				high=mid-1;
		}

		low=0, high=(1LL<<n)-1;
		while (low<=high) {
			mid = (low+high)/2;
			if (solve2(mid, 1LL<<n) <= p) {
				a2 = mid;
				low=mid+1;
			}
			else high=mid-1;
		}

		printf ("Case #%d: %lld %lld\n", ++tt, a1, a2);
	}

	return 0;
}
