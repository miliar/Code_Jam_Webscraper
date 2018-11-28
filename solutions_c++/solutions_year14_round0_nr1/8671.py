#include<stdio.h>
int search(int a,int *ar)
{
	for(int k=0;k<4;k++)
	{
		if(ar[k]==a)
		{return 1;}
	}
	return 0;
}
int main() 
{
	int test;
	int ar1[4][4],ar2[4][4],r1,r2,i,j,ans,count,a2[4];
	scanf("%d",&test);
	
	for(int t=1;t<=test;t++)
	{
		
		scanf("%d",&r1);
		for(i=0;i<4;i++)
		{
			scanf("%d %d %d %d",&ar1[i][0],&ar1[i][1],&ar1[i][2],&ar1[i][3]);
		}
		scanf("%d",&r2);
		for(i=0;i<4;i++)
		{
			scanf("%d %d %d %d",&ar2[i][0],&ar2[i][1],&ar2[i][2],&ar2[i][3]);
		}
		for(i=0;i<4;i++ )
		{a2[i]=ar2[r2-1][i];}
		count=0;
		for(i=0;i<4;i++)
		{
			if(search(ar1[r1-1][i],a2)==1)
			{
				count++;
				ans=i;
			}
		}
		
		if(count==0)
		{printf("Case #%d: Volunteer cheated!\n",t);}
		if(count>1&&count<=4)
		{printf("Case #%d: Bad magician!\n",t);}
		if(count==1)
		{printf("Case #%d: %d\n",t,ar1[r1-1][ans]);}
	}
	return 0;
}