#include<stdio.h>
#include<math.h>
int main()
{
	int c,t,i,j,k,l,r,m,n,max,f;
	//float p;
	int a[150][150],b[150][150];
	//char a[5][5],junk;
	freopen("in3.in","r",stdin);
	freopen("test_out.txt","w",stdout);
	
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{   	scanf("%d %d",&n,&m);
			for(j=1;j<=n;j++)
			{
				for(k=1;k<=m;k++)
				{
					scanf("%d",&a[j][k]);
				}
			}
			for(j=1;j<=n;j++)
			{
				for(k=1;k<=m;k++)
				{
					//scanf("%d",&a[j][k]);
					b[j][k]=100;
				}
			}
			for(j=1;j<=n;j++)
			{
				max=0;
				for(k=1;k<=m;k++)
				{
					if(a[j][k]>max)
							max=a[j][k];
				}
				for(k=1;k<=m;k++)
				{
					if(b[j][k]>max)
							b[j][k]=max;
				}
			}
			
			for(k=1;k<=m;k++)
			{
				max=0;
				for(j=1;j<=n;j++)
				{
					if(a[j][k]>max)
							max=a[j][k];
				}
				for(j=1;j<=n;j++)
				{
					if(b[j][k]>max)
							b[j][k]=max;
				}
			}
			
			f=1;
		for(j=1;j<=n;j++)
			{
				for(k=1;k<=m;k++)
				{
					//scanf("%d",&a[j][k]);
					if(b[j][k]!=a[j][k])
					{
							f=0;
					}
				}
			}
			
			
			if(f==1)
					printf("Case #%d: YES\n",i);
			else
					
					printf("Case #%d: NO\n",i);			
		
	}							
		//printf("%d\n",w);
	
	return 0;
}
