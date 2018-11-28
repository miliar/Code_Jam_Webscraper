#include<stdio.h>
int main()
{
	freopen("cook.txt","r",stdin);
	freopen("bro.txt","w",stdout);
	long long int sm,t,i,j,fa,su,co;
	char s[2000];
	scanf("%lld",&t);
	for(i=1;i<=t;i++)
	{
		su=0;
		fa=0;
		co=0;
		scanf("%lld",&sm);
		scanf("%s",s);
		for(j=0;j<=sm;j++)
		{
			if(su<fa)
			{
				++su;
				++co;
			}
			su=su+s[j]-'0';
			++fa;
		}
		printf("Case #%lld: %lld\n",i,co);
	}
	return 0;
}
