#include<stdio.h>
int a[1111];
int main()
{
	//freopen("A-small-attempt0.in.txt","r",stdin);
	//freopen("ans.txt","w",stdout);
	int i,sum,ans,t,tt=0,n;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n);
		for(i=0;i<=n;i++)
			scanf("%1d",a+i);
		sum=ans=0;
		for(i=0;i<=n;i++)
		{
			if(sum<i)
			{
				ans+=i-sum;
				sum+=i-sum;
			}
			sum+=a[i];
		}
		printf("Case #%d: %d\n",++tt,ans);
	}
	//fclose(stdin);
	//fclose(stdout);
	return 0;
}
/*
99
4 11111
1 09
5 110011
0 1

Case #1: 0
Case #2: 1
Case #3: 2
Case #4: 0
*/
