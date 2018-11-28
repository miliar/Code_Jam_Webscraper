#include<stdio.h>
int main()
{
	int a[16][16],b[16][16],i,j,t,r1,r2,l,n,x=0;
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("small.out","wt",stdout);
	scanf("%d",&t);
	for(l=0;l<t;l++)
	{
		scanf("%d",&r1);
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
				scanf("%d",&a[i][j]);
		}
		scanf("%d",&r2);
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
				scanf("%d",&b[i][j]);
		}
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(a[r1-1][i]==b[r2-1][j])
				{
					x++;
					n=i;
				}
			}
		}
		printf("case #%d: ",l+1);
		if(x==0)
			printf("Volunteer cheated!");
		if(x==1)
			printf("%d",a[r1-1][n]);
		if(x>1)
			printf("Bad magician!");
		x=0;
		printf("\n");
	}
	return 0;
}
