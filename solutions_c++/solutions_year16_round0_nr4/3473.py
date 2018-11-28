#include <stdio.h>
#include <string>
#include <algorithm>
#include <stdlib.h>
#include <vector>
#include <iostream>
#define mod 1000000007
#define INT_MAX 2147483647
using namespace std;
int t, ans, n, k,c,s;
long long one;
long long cal(int a, int b)
{
	long long ret = 1;

	while (b--)
	{
		ret *= a;
	}
	return ret;
}
char str[50];
int main() {
	freopen("D-small-attempt2.in", "r", stdin);
	freopen("d.out", "w", stdout);
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++)
	{
		int cnt = 0;
		printf("Case #%d: ", tt);
		scanf("%d%d%d", &k,&c,&s);
		if (k == 1)
		{
			printf("1\n");
			continue;
		}
		if (c == 1)
		{
			if (k > s) printf("IMPOSSIBLE");
			else
				for (int i = 1; i <= k; i++)
					printf("%d ", i);
			printf("\n");
		}
		else
		{
			one = cal(k, c-1);
			if ((k + 1) / 2 >s) printf("IMPOSSIBLE");
			else
				for (long long i = 1; i <= (k)/2; i++)
					printf("%lld ", i*2+2*one*(i-1));
			if (k % 2)printf("%lld",  one*k);
			printf("\n");
		}
	}
	return 0;
}