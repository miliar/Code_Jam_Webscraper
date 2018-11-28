#include <stdio.h>
using namespace std;

int tdnum, nowtd;

long long ans;
long long n;

void ri()
{
	ans = -1;
	scanf("%lld", &n);
}

long long solve()
{
	int mask = 0;

	long long i, maxi, j, x;

	if (n == 0) maxi = 1;
	else
	{
		maxi = 10;
		for (i = n; i > 0; i /= 10) maxi *= 10;
	}

	mask = 0;
	x = n;
	for (i = 1; i <= maxi; i++)
	{
		for (j = x; j; j /= 10) mask |= 1 << (j % 10);
		if (mask == 0b1111111111) return x;
		x += n;
	}
	return -1;
}

void print()
{
	printf("Case #%d: ", nowtd);
	if (ans < 0) printf("INSOMNIA\n");
	else printf("%lld\n", ans);
}

int main()
{
	scanf("%d", &tdnum);
	for (nowtd = 1; nowtd <= tdnum; nowtd++)
	{
		ri();
		ans = solve();
		print();
	}
	return 0;
}
