#include<stdio.h>
int main()
{
	int t,a[4][4],n,b[4][4],i,j,m,k;
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
		int c=0,ans;
		scanf("%d",&n);
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				scanf("%d",&a[i][j]);
			}
		}
		
		scanf("%d",&m);
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				scanf("%d",&b[i][j]);
			}
		}
		
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(a[n-1][i]==b[m-1][j])
			{
				ans=a[n-1][i];
				c++;
			}
		    }
		}
		
		if(c==0)
		{
			printf("Case #%d: Volunteer cheated!\n",k);
		}
		if(c>1)
		{
			printf("Case #%d: Bad magician!\n",k);
		}
		if(c==1)
		{
			printf("Case #%d: %d\n",k,ans);
		}
	}
	return 0;
}
