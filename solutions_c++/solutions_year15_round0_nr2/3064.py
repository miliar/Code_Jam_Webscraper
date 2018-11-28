#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>

using namespace std;
int T,n,ans,a[2000];
int dq;
int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d",&T);
	for (int z=1;z<=T;++z)
	{
		scanf("%d",&n);
		for (int i=1;i<=n;++i) scanf("%d",&a[i]);
		ans=199509200;
		for (int i=1;i<=1000;++i)
		{
			dq=0;
			for (int j=1;j<=n;++j)
			{
				if (a[j]%i==0) dq+=-1+a[j]/i;else dq+=a[j]/i;
			}
			dq+=i;
			ans=min(ans,dq);
		}
		printf("Case #%d: %d\n",z,ans);
	}
	return 0;
}
