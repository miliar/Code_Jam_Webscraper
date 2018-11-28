#include<bits/stdc++.h>
using namespace std;
long long a[10],last[1000011];
int main()
{
	long long i,j,sum,ans,ans1,rem,f,t,req;
	for(i=1;i<=1000001;i++)
	{	memset(a,0,sizeof(a));
		sum=0;ans=0;f=0;
		while(!(sum==45 && f==1) )
		{
			ans=ans+i;
			ans1=ans;
			while(ans1)
			{
				rem=ans1%10;
				ans1=ans1/10;
				if(a[rem]==0)
				{
				if(rem==0)
				f=1;
				a[rem]=1;
				sum=sum+rem;
				}
			}
		}
		
	
		
		last[i]=ans;
	}
	
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cin>>req;
		if(req==0)
		printf("Case #%lld: INSOMNIA\n",i);
		else
		printf("Case #%lld: %lld\n",i,last[req]);
	}
	
	
}
