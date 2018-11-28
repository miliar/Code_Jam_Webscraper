#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t,tt,n,i,ans;
	int a[1005],b[1005];
	char ch;
	scanf("%d",&t);
	for(tt=1;tt<=t;tt++)
	{
		scanf("%d",&n);
		ans=0;
		for(i=0;i<=n;i++)
		{
			scanf(" %c",&ch);
			a[i]=ch-'0';
			if(!i)
				b[i]=a[i];
			else
			{
				if(i>b[i-1])
				{
					ans+=i-b[i-1];
					b[i-1]+=i-b[i-1];
				}
				b[i]=a[i]+b[i-1];
			}
		}
		printf("Case #%d: %d\n",tt,ans);
	}
	return 0;
}