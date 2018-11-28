#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main()
{
	ll tt,t,n,s,str,arr[10];
	scanf("%lld",&tt);
	t=0;
	while(t!=tt)
	{
		t++;
		ll count=0;
		for(ll i=0;i<10;i++)
		{
			arr[i]=0;
		}
		scanf("%lld",&s);
		if(s==0)
		printf("Case #%lld: INSOMNIA\n",t);
		else
		{
		
		ll k=1;
		while(count!=10)
		{
			n=s*k;
			str=n;
			k++;
			while(n!=0)
			{
				if(arr[n%10]==0)
				{
					count++;
					if(count==10)
					break;
					arr[n%10]=1;
				}
				n=n/10;
			}
			
		}
		printf("Case #%lld: %lld\n",t,str);
	}
	}
	return 0;
}