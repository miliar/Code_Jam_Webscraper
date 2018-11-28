#include <stdio.h>

int main()
{
	int n,t,m,i,j,p,a[4][4],b[4],c[4],num,k;
	scanf("%d",&t);
	p=1;
	while(t--)
	{
		k=0;
		num=0;
		scanf("%d",&n);
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				scanf("%d",&a[i][j]);
				if(i==n-1)
					b[j]=a[i][j];
			}
		}
		scanf("%d",&m);
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				scanf("%d",&a[i][j]);
				if(i==m-1)
					c[j]=a[i][j];
			}
		}
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(b[i]==c[j])
				{
					k=b[i];
					num++;
				}
			}
		}
		if(num==1)
			printf("Case #%d: %d\n",p,k);
		else if(num==0)
		{
			printf("Case #%d: Volunteer cheated!\n",p);
		}
		else
			printf("Case #%d: Bad magician!\n",p);
		p++;
	}
	return 0;
}
