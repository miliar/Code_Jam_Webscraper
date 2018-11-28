#include<stdio.h>
#include<iostream>
#include<math.h>

#define max(a, b) ((a) > (b)?(a):(b))
#define min(a, b) ((a) < (b)?(a):(b))

using namespace std;

int main()
{
	freopen("D-small-attempt0.in", "rt", stdin);
	freopen("d.out", "wt", stdout);
	int inp, i, kase, j;
	long long k, c, s;
	scanf("%d", &inp);
	for (kase = 1; kase <= inp; kase++)
	{
		scanf("%lld %lld %lld", &k, &c, &s);
		long long st = 1;
		long long mult = 1;
		for (i = 1; i < c; i++)
		{
			mult *= k;
		}
		printf("Case #%d:", kase);
		for (i = 0; i < s; i++)
		{
			printf(" %lld", st);
			st += mult;
		}
		printf("\n");
	}
	return 0;
}
