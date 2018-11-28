#include<stdio.h>
main()
{
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		int s;
		scanf("%d",&s);
		char num;scanf("%c",&num);
		int sum=0,ans=0;
		for(int j=0;j<=s;j++)
		{	
			scanf("%c",&num);
			if(sum<j)
			{
				ans+=j-sum;
				sum=j;
			}
			sum+=num-'0';
		}
		printf("Case #%d: %d\n",i,ans);
	}
} 
