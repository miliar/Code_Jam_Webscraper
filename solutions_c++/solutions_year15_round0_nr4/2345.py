#include<stdio.h>
int main()
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	long long int t,i=1;
	scanf("%lld",&t);
	while(i<=t)
	{
		long long int x,c,r,ans=0;
		scanf("%lld%lld%lld",&x,&r,&c);
		if(x<3)
		{
			if(((x<=r&&c>=x/2)||(c>=x&&r>=x/2))&&r*c%x==0)
			{
				
			}
			else
			ans=1;
		}
		else if(((x<=r&&c>=x/2)||(c>=x&&r>=x/2))&&r*c%x==0)
		{
			if(c==x/2||r==x/2)
			{
				ans=1;
			}
		}
		else
		ans=1;
		if(ans==1)
		printf("Case #%lld: RICHARD\n",i);
		else
		printf("Case #%lld: GABRIEL\n",i);
		i++;
	}
	return 0;
}
