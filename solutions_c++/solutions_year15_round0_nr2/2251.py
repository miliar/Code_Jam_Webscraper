#include <iostream>
#include <cstdio>

using namespace std;

#define fd 10000
using namespace std;
int a[fd];
int main()
{
	int t;
	scanf("%d",&t);
	for(int z = 1 ; z <= t ; z++)
	{

		int maxss = 0,n;

		scanf("%d",&n);

		for(int i=1 ; i<=n;i++)
		{
			scanf("%d",&a[i]);
			maxss=max(maxss,a[i]);
		}

		int ans1=maxss;

		for(int i = 1 ; i <= maxss ; i++)
		{
			int ans = 0 , ma = 0;
			for(int j = 1 ; j <= n; j++)
			{
				if(a[j] > i)
				{
					ans += (a[j] / i) + ((a[j]%i==0)?0:1)-1;
					ma=max(ma,i);
				}
				else ma=max(ma,a[j]);
			}
			ans += ma;
			if(ans < ans1)
				ans1 = ans;
		}
		printf("Case #%d: %d\n", z , ans1);
	}
	return 0;
}