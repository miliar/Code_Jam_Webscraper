#include <stdio.h>
int tcase,n,ans,sum;
char str[1100];
int main()
{
	int i,k;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&tcase);
	for(k=1;k<=tcase;k++)
	{
		scanf("%d %s",&n,str);
		ans=sum=0;
		for(i=0;i<=n;i++)
		{
			str[i]-=48;
			if(sum<i && str[i]>0)
			{
				ans+=(i-sum);
				sum=i;
			}
			sum+=str[i];
		}
		printf("Case #%d: %d\n",k,ans);
	}
	return 0;
}