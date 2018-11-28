#include<cstdio>
#include<algorithm>
#include<string>
int main()
{
	long long int r,t,ans,i,T,c;
	scanf("%lld",&T);
	for(t=1;t<=T;t++)
	{
		scanf("%lld%lld",&r,&c);
		ans=0;
		while(c)
		{
			if(2*r+1<=c)
			{
				ans++;
				c=c-(2*r+1);
				r+=2;
			}
			else
				break;
		}
		printf("Case #%lld: %lld\n",t,ans);
	}
	return 0;
}

