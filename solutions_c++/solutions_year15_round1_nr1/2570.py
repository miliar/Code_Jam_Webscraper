#include<stdio.h>
#include<math.h>
int main()
{
	freopen ("dd.in", "r", stdin);
        freopen ("output.txt", "w", stdout);
	long long int t,n,m,a[10001],ans,res=0,max,temp,i,sum,v=0;
	scanf("%lld",&t);
	while(t--)
	{
		
		v++;
		scanf("%lld",&n);
		for(i=0;i<n;i++)
		{
			scanf("%lld",&a[i]);
		}
		temp=-1;res=0,ans=0;sum=0;max=0;
		for(i=1;i<n;i++)
		{
			if(a[i]-a[i-1]<0)
			{
				res=abs(a[i]-a[i-1]);
				if(res>temp)
				{
					max=res;
					temp=res;
				}
				sum=sum+res;
			}
		}
		for(i=0;i<n-1;i++)
		{
			if(a[i]>=max)
			{
				ans=ans+max;
			}
			else
			{
				ans=ans+a[i];
			}
			
		}
		printf("Case #%lld: %lld %lld\n",v,sum,ans);
	}
	return 0;
}
