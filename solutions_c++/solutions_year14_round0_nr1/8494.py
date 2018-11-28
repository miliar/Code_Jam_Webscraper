#include<stdio.h>
int main()
{
	int t,r1,r2,a[4][4],b[4][4],i,j,k,res,ans=0;
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
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
				scanf("%d",&b[i][j]);
			}
		}
		res=0;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(a[r1-1][i]==b[r2-1][j])
				{
					res++;
					ans=b[r2-1][j];
				}
			}
		}
		if(res==0)
		{
			printf("Case #%d: Volunteer cheated!\n",k);
			continue;
		}
		if(res==1)
		{
			printf("Case #%d: %d\n",k,ans);
			continue;
		}
		else
		{
			printf("Case #%d: Bad magician!\n",k);
			continue;
		}
	}
	return 0;
}
		
				
				
				
		
		
		
		
		
		
		
		
		
		
		
