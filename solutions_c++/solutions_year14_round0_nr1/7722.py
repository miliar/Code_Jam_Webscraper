#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	int t,a,b,temp;
	scanf("%d",&t);
	for(int k=1;k<=t;k++)
	{
		int ma[17]={0};
		scanf("%d",&a);
		for(int i=1;i<=4;i++)
		{
			for(int j=1;j<=4;j++)
			{
				scanf("%d",&temp);
				if(i==a)
				{
					ma[temp]=1;
				}
			}
		}
		scanf("%d",&b);
		int ans=-1;
		int n=0;
		for(int i=1;i<=4;i++)
		{
			for(int j=1;j<=4;j++)
			{
				scanf("%d",&temp);
				if(i==b)
				{
					if(ma[temp]==1)
					{
						n++;
						ans=temp;
					}
				}
			}
		}
		if(n==1)
		{
			
			printf("Case #%d: %d\n",k,ans);
		}
		else if(n!=0)
		{
			printf("Case #%d: Bad magician!\n",k);
		}
		else
		{
			printf("Case #%d: Volunteer cheated!\n",k);
		}
	}
	return 0;
}		
