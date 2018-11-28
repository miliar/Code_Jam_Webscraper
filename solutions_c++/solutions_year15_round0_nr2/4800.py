#include<bits/stdc++.h>
using namespace std;
int a[1234];
int main()
{
	int t;
	scanf("%d",&t);
	for(int cas=1;cas<=t;cas++)
	{
		int max_x=0,n,ans;
		scanf("%d",&n);
		for(int i=1;i<=n;i++)
		{
			scanf("%d",&a[i]);
			max_x=max(max_x,a[i]);
		}
		ans=max_x;
		for(int i=1;i<=max_x;i++)
		{
			int now=0,maxx=0;
			for(int j=1;j<=n;j++)
			{
				if(a[j]>i)
				{
					now += (a[j] / i)+((a[j]%i==0)?0:1)-1;
					maxx=max(maxx,i);
				}
				else maxx=max(maxx,a[j]);
			}
			now+=maxx;
			if(now<ans)
			ans=now;
		}
		printf("Case #%d: %d\n",cas,ans);
	}
}