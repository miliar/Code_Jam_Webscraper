#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	int a[4][4],count,b,c,i,j,k,p,t,r1,r2;
	scanf("%d",&t);
	for(p=1;p<=t;p++)
	{
		count=0;
		scanf("%d",&r1);
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				scanf("%d",&a[i][j]);
			}
		}
		scanf("%d",&r2);
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				scanf("%d",&b);
				if(r2-1==i)
				{
					for(k=0;k<4;k++)
						if(a[r1-1][k]==b)
						{
							count++;
							c=b;
						}
				}
			}
		}
		if(count==1)
			printf("Case #%d: %d\n",p,c);
		else if(count==0)
			printf("Case #%d: Volunteer cheated!\n",p);
		else
			printf("Case #%d: Bad magician!\n",p);
	}
	return 0;
}