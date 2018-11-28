#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	int x;
	for(int tc=1;tc<=t;++tc)
	{
		int maxi=0,tot=0,ans=0;
		scanf("%d",&maxi);
		for(int i=0;i<=maxi;++i)
		{
			scanf("%1d",&x);
			if(tot<i)
			{
				ans+=i-tot;
				tot+=i-tot;

			}
			tot+=x;
		}
		printf("Case #%d: %d\n",tc,ans);
	}
	return 0;
}
