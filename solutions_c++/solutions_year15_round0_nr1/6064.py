#include<stdio.h>
int main()
{
	long long i,j,k,c,t,n,m,ans,l;
	//freopen("inp.in","r",stdin);
	//freopen("out.in","w",stdout);
	scanf("%lld",&t);
	for(l=1;l<=t;l++)
	{
		scanf("%lld",&n);
		char s[n+2];
		scanf("%s",s);
		c=s[0]-'0';
		ans=0;
		for(i=1;i<=n;i++)
		{

			if(s[i]!='0')
			{
				m=s[i]-'0';
				if(c>=i)
				{
					c+=m;
				}
				else
				{
					ans+=i-c;
					c+=m+i-c;
				}
			}
			//printf("%lld %lld\n",c,ans);

		}
		printf("Case #%lld: %lld\n",l,ans);
	}
	return 0;
}
