#include <iostream>
#include <fstream>

int main()
{
	freopen("input","r",stdin);
	freopen("output","w",stdout);
	int t,n,m,a[100][100],i,j,k,c,f,flag;
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		scanf("%d%d",&n,&m);
		for(j=0;j<n;j++)
		{
			for(k=0;k<m;k++)
			{
				scanf("%d",&a[j][k]);
			}
		}
		f=1;
		for(j=0;j<n;j++)
		{
			for(k=0;k<m;k++)
			{
				flag=0;
				if(a[j][k]==1)
				{
					for(c=0;c<m;c++)
					{
						if(a[j][c]==2)
						{
							flag=1;
							break;
						}
					}
					if(flag==1)
					{
						for(c=0;c<n;c++)
						{
							if(a[c][k]==2)
							{
								flag=2;
								break;
							}
						}
					}
				}
				if(flag==2)
				{
					f=0;
					break;
				}
			}
			if(f==0)
			break;
		}
		if(f==1)
		printf("Case #%d: YES\n",i);
		if(f==0)
		printf("Case #%d: NO\n",i);							
	}
	return 0;
}
	
