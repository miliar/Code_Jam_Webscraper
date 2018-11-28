#include<iostream>
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<algorithm>

using namespace std;
int main()
{
    int k,c,y,i,j,a1,a2,t,x=1,b1[4][4],b2[4][4];
	scanf("%d",&t);	
	while(t--)
	{
	int ch1[4]={0},ch2[4]={0};
	c=0;
	
	scanf("%d",&a1);
	
	for(i=0;i<4;i++)
	for(j=0;j<4;j++)
	scanf("%d",&b1[i][j]);
	
	scanf("%d",&a2);
	
	for(i=0;i<4;i++)
	for(j=0;j<4;j++)
	scanf("%d",&b2[i][j]);
	
	j=0;
	
	for(j=0;j<4;j++)
	ch1[j]=b1[a1-1][j];
	
	j=0;
	
	for(j=0;j<4;j++)
	ch2[j]=b2[a2-1][j];
	
	for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{	
			if(ch1[j]==ch2[k])
			{
				c++;
				y=ch1[j];
		}
		}
		}
	if(c==1)
	printf("Case #%d: %d\n",x,y);
	else if(c>1)
	printf("Case #%d: Bad magician!\n",x);
	else
	printf("Case #%d: Volunteer cheated!\n",x);
	x++;
	}
return 0;
}
