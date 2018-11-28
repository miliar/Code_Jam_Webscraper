#include<stdio.h>
int main()
{
	int t,n,i,k;
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	char str[10000];
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
		scanf("%d",&n);
		scanf("%s",str);
		int ans=0,sum=0;
		for(i=0;i<=n;i++)
		{
			
			if(sum<i)
			{
				ans+=i-sum;
				sum+=i-sum;
			}
			
			sum+=str[i]-'0';
		}
		printf("Case #%d: %d\n",k,ans);
		
	}
}
