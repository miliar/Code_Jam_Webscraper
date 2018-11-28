#include <bits/stdc++.h>
using namespace std;

int main()
{
	int t,c,s;
	scanf("%d",&t);
	long long k,num,ans;
	for (int i = 1; i <= t; ++i)
	{
		scanf("%lld %d %d",&k,&c,&s);
		num = 0;
		for (int j = 1; j < c; ++j)
		{
			num *= k;
			num += k;
		}
		printf("Case #%d: ",i);
		for (int j = 1; j <= k; ++j)
		{
			ans = num*(j-1) + j;
			printf("%lld ",ans);
		}
		printf("\n");
	}

}