#include<bits/stdc++.h>
using namespace std;
int a[1100];
int main()
{
	int t,cas=0;
	scanf("%d",&t);
	for(cas=0;cas<t;)
	{
		int maxi=0,n;
		scanf("%d",&n);
		for(int i=1;i<=n;i++)
		{
			scanf("%d",&a[i]);
			maxi=max(maxi,a[i]);
		}
		int ans=maxi;
		for(int i=1;i<=maxi;i++)
		{
			int now=0,maxx=0;
			for(int j=1;j<=n;j++)
			{
				if(a[j]>i)
				{
					now+=(a[j]/i);
					now+=((a[j]%i==0)?0:1)-1;
					maxx=max(maxx,i);
				}
				else 
					maxx=max(maxx,a[j]);
			}
			now+=maxx;
			if(now<ans)
				ans=now;
		}
		printf("Case #%d: %d\n",++cas,ans);
	}
	return 0;
}
