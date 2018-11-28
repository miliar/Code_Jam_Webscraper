#include <bits/stdc++.h>
#define ll long long int
using namespace std;
int main()
{
	ll t,n,arr[10],y,p,flag,fl,x,i;
	scanf("%lld",&t);
	p=t;
	while(p--)
	{
		flag=0;
		scanf("%lld",&n);
		if(n==0)
			printf("Case #%lld: INSOMNIA\n",t-p);
		else
		{
			for(int h=0;h<10;h++)
			{
				arr[h]=0;
			}
			i=1;
			while(flag==0)
			{	//printf("stuti");
				
				x=n*i;
				while(x!=0)
				{
					y=x%10;
					//printf("%d\n",y);
					x=x/10;
					arr[y]=1;
				}
				fl=0;
				for(int h=0;h<10;h++)
				{
					if(arr[h]==0)
						fl=1;
				}
				if(fl==0)
					flag=1;
				i++;
			}
		
		printf("Case #%lld: %lld\n",t-p,n*(i-1));
		}
	}
	return 0;
}