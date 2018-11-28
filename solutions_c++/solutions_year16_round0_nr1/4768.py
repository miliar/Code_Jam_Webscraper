#include <stdio.h>
#include <string>
#include <algorithm>
#include <stdlib.h>
#include <vector>
#include <iostream>
#define mod 1000000007
#define INT_MAX 2147483647
using namespace std;
int t, check[10];
long long n, ans, num, now;
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("alarge.out", "w", stdout);
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++)
	{
		scanf("%lld", &n);
		num = 0;
		now = 0;
		memset(check, 0, sizeof(check));
		for (long long i = 1; i <= 1000; i++)
		{
			ans = num = n*i;
			while (num)
			{
				if (!check[num % 10])check[num % 10] = 1, now++;
				num /= 10;
			}
			if (now == 10) break;
		}
		if (now == 10)
		printf("Case #%d: %lld\n", tt, ans);
		else printf("Case #%d: INSOMNIA\n", tt);
	}
	return 0;
}