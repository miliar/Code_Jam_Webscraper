#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<vector>
#define max 10001
using namespace std;
int main()
{
	int a[4][4],b[4][4],n1,n2,i,j,k,t,c,p;
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
		c=0;
		scanf("%d",&n1);
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				scanf("%d",&a[i][j]);
		scanf("%d",&n2);
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				scanf("%d",&b[i][j]);
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(a[n1-1][i]==b[n2-1][j])
				{
					c++;
					p=a[n1-1][i];
				}
			}
		}
		if(c==1)
			printf("Case #%d: %d\n",k,p);
		else if(c>1)
			printf("Case #%d: Bad magician!\n",k);
		else if(c==0)
			printf("Case #%d: Volunteer cheated!\n",k);
			
	}
return 0;
}

