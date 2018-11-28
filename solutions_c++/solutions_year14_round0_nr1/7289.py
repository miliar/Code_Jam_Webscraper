#include<cstdio>
#include<cmath>
#include<iostream>
#include<cstring>
#include<cstdlib>
using namespace std;

int main()
{
	int i,t,n,j,k,found=0,y;
	int arr[4][4];
	int a[2][4];
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		y=found=0;
		scanf("%d",&n);
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				scanf("%d",&arr[j][k]);
			}
		}
		for(j=0;j<4;j++)
		{
			a[0][j]=arr[n-1][j];
		}
		scanf("%d",&n);
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				scanf("%d",&arr[j][k]);
			}
		}
		for(j=0;j<4;j++)
		{
			a[1][j]=arr[n-1][j];
		}
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				if(a[0][j]==a[1][k])
				{
					y = a[0][j];
					found++;
				}
			}	
		}
		if(found==1)
		{
			printf("Case #%d: %d",i,y);
		}
		else if(found > 1)
		{
			printf("Case #%d: Bad magician!",i);
		}
		else if(found==0)
		{
			printf("Case #%d: Volunteer cheated!",i);
		}
		printf("\n");
	}
	return 0;
}
