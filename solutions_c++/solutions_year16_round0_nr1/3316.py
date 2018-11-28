#include <bits/stdc++.h>
using namespace std;
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("outlarge", "w", stdout);
	int tt;
	scanf("%d", &tt);
	for(int q = 1; q <= tt; q++)
	{
		bitset<10> ok;
		long long n;
		scanf("%lld", &n);
		printf("Case #%d: ", q);
		bool k = 0;
		for(int i = 1; i<= 1e6; i++)
		{
			long long x = n*i;
			long long y = x;
			if(x< 0) break;
			while(x)
			{
				ok[x%10] = 1;
				x/= 10;
			}
			if(ok.all())
			{
				printf("%lld\n", y);
				k = 1;
				break;
			}
		}
		if(!k)
		{
			printf("INSOMNIA\n");
		}
	}
}