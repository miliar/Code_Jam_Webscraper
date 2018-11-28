#include<cstdio>
#include<iostream>
using namespace std;
int main()
{
	int t,i,j,f,a[100][100],k,l,n,m;
	scanf("%d",&t);
	for(l=1;l<=t;l++)
	{
		f=0;
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				scanf("%d",&a[i][j]);
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				if(a[i][j]==1)
				{
					for(k=0;k<m;k++)
						if(a[i][k]!=1)
						{
							f=1;break;
						}
					if(f)
					{       f=0;
						for(k=0;k<n;k++)
						{
							if(a[k][j]!=1)
							{
								f=1;break;
							}
						}
					}
				}
				if(f) goto label;
			}
		}
label: if(f) printf("Case #%d: NO\n",l);
   else printf("Case #%d: YES\n",l);
	}
	return 0;
}
