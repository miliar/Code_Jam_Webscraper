#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;
const int N = 10012;
int ans,a[N],sum[N],T,n;
int main()
{
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	scanf("%d",&T);
	for(int t = 1;t <= T; ++ t)
	{
		memset(sum,0,sizeof(sum));
		ans = 0;
		scanf("%d ",&n);
		for(int i = 0;i <= n; ++ i)
			scanf("%c",&a[i]),a[i] -= '0';
		sum[0] = a[0];
		for(int i = 1;i <= n; ++ i)
		{
			if (sum[i - 1] >= i)
				sum[i] = sum[i - 1] + a[i];
			else
			{
				ans += i - sum[i - 1];
				sum[i] = i + a[i];
			}
		}
		printf("Case #%d: %d\n",t,ans);
	}
}
