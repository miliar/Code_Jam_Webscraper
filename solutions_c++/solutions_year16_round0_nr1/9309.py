#include<bits/stdc++.h>
using namespace std;
int madh=1;
typedef long long int ll;
int hashi[30]={0};
int main()
{
	int i,j,t;
	scanf("%d",&t);
	while(t--)
	{
		ll n;
		for(i=0;i<=10;i++)
			hashi[i]=0;
		scanf("%lld",&n);
		if(n==0)
		{
			printf("Case #%d: INSOMNIA\n",madh++);
			continue;
		}
		int flag=0;
		for(i=1;i<=1000000;i++)
		{
			ll temp=(i*(n));
			while(temp)
			{
				hashi[temp%10]++;
				temp=temp/10;
			}

			for(j=0;j<10;j++)
			{
				if(!hashi[j])
					break;
			}
			if(j==10)
				break;
		}
		
		if(j==10)
		{
			printf("Case #%d: %lld\n",madh++,(ll)(n*i));
		}
	}
	return 0;
}