#include<bits/stdc++.h>
using namespace std;
#define maxi 1005

int main()
{
	int t,n,a[maxi],m,temp,ans,p;
	scanf("%d",&t);
	for(int k=1;k<=t;k++)
	{
		scanf("%d",&n);
		m=-1;
		for(int i=0;i<n;i++)
		{
			scanf("%d ",&a[i]);
			m=max(m,a[i]);
		}
		p=INT_MAX;
		for(int i=1;i<=m;i++)
		{
			temp=0;
			for(int j=0;j<n;j++)
			{
				if(a[j]>i)
				{
					if(a[j]%i!=0)
					temp+=(a[j]/i);
					else 
					temp+=((a[j]/i)-1);
				}
			}
			p=min(p,temp+i);	
		}
		ans=min(p,m);
		printf("Case #%d: %d\n",k,ans);
	}
	return 0;
}