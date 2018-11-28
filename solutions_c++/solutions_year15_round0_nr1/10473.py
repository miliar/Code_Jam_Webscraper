#include<stdio.h>
int main()
{
	int t;
	long int sum=0,people;
	int n,i,y=1;
	scanf("%d",&t);
	while(t--)
	{
				char ch[1005];
		scanf("%d %s",&n,ch);
		int ar[n+1];
		for(i=0;i<=n;i++)
		{
		ar[i]=ch[i]-48;
		}
		//for(i=0;i<=n;i++)
		//printf("%d\n",ar[i]);
		sum=0;
		people=0;
		for(i=0;i<=n;i++)
		{
			if(sum>=i)
			{
				sum=sum+ar[i];
				people=people+0;
			}
			else if(sum<i && ar[i]!=0)
			{
				people=people+(i-sum);
				sum=sum+ar[i]+(i-sum);
			}
		}
		printf("Case #%d: %ld\n",y,people);
		y++;
		sum=0;
		people=0;
		
	}
	return 0;
}
