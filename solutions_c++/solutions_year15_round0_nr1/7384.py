#include<stdio.h>
#include<string.h>
int main()
{
	char s[1001];
	int t,x,i,n,sum,count,a;
	scanf("%d",&t);
	for(x=1;x<=t;x++)
	{
		sum=0;count=0;
		scanf("%d %s",&n,s);
		for(i=0;i<=n;i++)
		{
			a=0;
			if(sum<i)
			a=i-sum;
			sum=sum+(s[i]-'0');
			count+=a;
			sum+=a;
		}
		printf("Case #%d: %d\n",x,count);
	}
	return 0;
}
