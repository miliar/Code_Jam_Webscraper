#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	int t,a[4][4],b[4][4],r1,r2,ccase=0,store,c=0;
	scanf("%d",&t);
	while(t--)
	{
		c=0;
		ccase++;
		scanf("%d",&r1);
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				scanf("%d",&a[i][j]);
			}
		}
		scanf("%d",&r2);
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				scanf("%d",&b[i][j]);
			}
		}
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(a[r1-1][i]==b[r2-1][j])
				{
					c++;
					store=a[r1-1][i];
				}
			}
		}
		if(c==1)
			printf("Case #%d: %d\n",ccase,store);
		else if(c>1)
			printf("Case #%d: Bad magician!\n",ccase);
		else
			printf("Case #%d: Volunteer cheated!\n",ccase);
		
	
	}
	return 0;

	
}