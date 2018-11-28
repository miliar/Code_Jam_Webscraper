#include<stdio.h>
int main()
{
	int t,a[2][4],x,i,j,k,l,ans;
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		scanf("%d",&x);
		for(j=1;j<=4;j++)
		{
			for(k=0;k<4;k++)
			{
				scanf("%d",&l);
				if(j==x)
					a[0][k]=l;
			}
		}
		scanf("%d",&x);
		for(j=1;j<=4;j++)
		{
			for(k=0;k<4;k++)
			{
				scanf("%d",&l);
				if(j==x)
					a[1][k]=l;
			}
		}
		ans=0;
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				if(a[0][j]==a[1][k])
				{
					if(ans==0)
						ans=a[0][j];
					else
					{
						ans=-1;
					}
				}
			}
		}
		printf("Case #%d: ",i);
		if(ans==-1)
			printf("Bad magician!\n");
		else if(ans==0)
			printf("Volunteer cheated!\n");
		else
			printf("%d\n",ans);
	}
}
