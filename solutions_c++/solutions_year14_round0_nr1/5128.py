#include<stdio.h>
int main()
{
	int i,j,k,l,n,t,m,a[10][10],b[10][10],c[20],d[20],f=0,z;
	scanf("%d",&t);
	for(k=0;k<t;k++)
	{
		f=0;
		scanf("%d",&m);
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			scanf("%d",&a[i][j]);
		}
		scanf("%d",&n);
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			scanf("%d",&b[i][j]);
		}
		for(i=1;i<=4;i++)
		{
			c[i]=a[m][i];
		}
		for(i=1;i<=4;i++)
		{
			d[i]=b[n][i];
		}
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				if(c[i]==d[j])
				{
					f++;
					z=c[i];
					
				}
			}
		}
		if(f==1)
		{
		printf("Case #%d: %d\n",k+1,z);	
		}
		else if(f>1)
		{
		printf("Case #%d: Bad magician!\n",k+1);		
		}
		else if(f==0)
		printf("Case #%d: Volunteer cheated!\n",k+1);	
	}
	return 0;
}
