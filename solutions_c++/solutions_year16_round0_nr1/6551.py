#include<stdio.h>
#include<string.h>
typedef long long ll;
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("filename.txt", "w", stdout);
	ll t,n,i;
	ll ar[15];
	ll b=0;
	ll ans;
	ll count=0;
	ll g=0;
	ll ans1;
	scanf("%lld",&t);
	while(t--)
	{
		memset(ar,0,sizeof(ar));
		count=0;
		scanf("%lld",&n);
			if(n==0)
		{
			printf("Case #%lld: INSOMNIA\n",++g);
			continue;
		}
		for(i=1;;i++)
		{
		ans=n*i;
		ans1=n*i;
		while(ans!=0)
		{
			ll rem=ans%10;
			if(ar[rem]==0)
			{
				ar[rem]++;
				count++;
			}
			ans=ans/10;
			}	
			if(count==10)
			{
			printf("Case #%lld: %lld\n",++g,ans1);
			break;
		}
		}
	}
	return 0;
}
