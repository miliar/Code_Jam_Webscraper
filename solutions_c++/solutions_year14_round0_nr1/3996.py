#include<iostream>
using namespace std;
#include<cstdio>
int a[5][5],b[5][5],a1,a2,r1,r2;
int main()
{
	int t,count;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		count=0;
		scanf("%d",&a1);
		for(int j=1;j<=4;j++)
		{
			for(int k=1;k<5;k++)
			{
				scanf("%d",&a[j][k]);
			}
		}
		scanf("%d",&a2);
		for(int j=1;j<=4;j++)
		{
			for(int k=1;k<5;k++)
			{
				scanf("%d",&b[j][k]);
			}
		}
		for(int j=1;j<=4;j++)
		{
			for(int k=1;k<5;k++)
			{
				if(a[a1][j]==b[a2][k])
				{
					count++;
					r1=j;
					r2=k;
				}
			}
		}
		printf("Case #%d: ",i);
		if(count==1)
		printf("%d\n",a[a1][r1]);
		else if(count==0)
		printf("Volunteer cheated!\n");
		else
		printf("Bad magician!\n");
		
	}
return 0;
}
