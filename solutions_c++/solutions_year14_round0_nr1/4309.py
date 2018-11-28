#include<stdio.h>

int main()
{
	int i,j,k,a[4][4],b[4][4],d=0,m=0,T,A1,A2;
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("A.out","wt",stdout);
	scanf("%d",&T);
	for(i=0;i<T;i++)
	{
		scanf("%d",&A1);
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			scanf("%d",&a[j][k]);
		}
		scanf("%d",&A2);
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			scanf("%d",&b[j][k]);
		}
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				if(a[A1-1][j]==b[A2-1][k])
				{
					m++;
					d=j;
				}
			}
		}
		if(m==0)
		printf("Case #%d: Volunteer cheated!\n",i+1);
		else if(m==1)
		printf("Case #%d: %d\n",i+1,a[A1-1][d]);
		else
		printf("Case #%d: Bad magician!\n",i+1);
		m=0;
		d=0;
    }
	return 0;
}
