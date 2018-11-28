#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	int k, c;
	long long s;
	scanf("%d", &t);
	for (int tc = 1; tc <= t; ++tc)
	{
		scanf("%d %d %lld", &k, &c, &s);
		long long x = 0;
		long long tmp = 1;
		for (int i = 0; i < c; ++i)
		{
			tmp *= k;
		}
		printf("Case #%d:", tc);
		for (int i = 1; i <= k; ++i)
		{
			printf(" %d", i);
		}
		printf("\n");
	}
}