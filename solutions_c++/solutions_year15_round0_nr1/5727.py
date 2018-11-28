#include<stdio.h>
int sum[1005];
char s[1005];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int k=1;k<=t;k++)
	{
		int n;
		scanf("%d ",&n);
		gets(s);
		for(int i=0;i<=n;i++)
		{
			if(i==0)
				sum[i]=s[i]-'0';
			sum[i]=sum[i-1]+s[i]-'0';
		}
		int x=0;
		for(int i=1;i<=n;i++)
			if(sum[i-1]+x < i)
				x+=i-(sum[i-1]+x);
		printf("Case #%d: %d\n",k,x);
	}
}
