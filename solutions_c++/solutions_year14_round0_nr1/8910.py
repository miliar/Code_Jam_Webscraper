#include<stdio.h>
int a[101][4][4]={},b[101][4][4]={},c[101]={},d[101]={},f[101]={},y[101]={};
main()
{
	int t,i,j,k;
	scanf("%d",&t);

	for(i=0;i<t;i++)
	{
		scanf("%d",&c[i]);
		for(j=0;j<4;j++)
			for(k=0;k<4;k++)
			scanf("%d",&a[i][j][k]);
			
		scanf("%d",&d[i]);
		for(j=0;j<4;j++)
			for(k=0;k<4;k++)
			scanf("%d",&b[i][j][k]);
	}
	for(k=0;k<t;k++)
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
		if(a[k][c[k]-1][i]==b[k][d[k]-1][j])
		{
			y[k]=a[k][c[k]-1][i];
			f[k]++;
		}
		}
	}
	for(k=0;k<t;k++)
	{
	if(f[k]==0)
	printf("Case #%d: Volunteer cheated!\n",k+1);
	else if(f[k]>1)
	printf("Case #%d: Bad magician!\n",k+1);
	else if(f[k]==1)
	printf("Case #%d: %d\n",k+1,y[k]);
	}
}
