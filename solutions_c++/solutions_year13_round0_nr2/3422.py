#include<stdio.h>
int c[110][110];
int main()
{
	//freopen("B-large.in","r",stdin);
    //freopen("B-large.out","w",stdout);
	int i,j,n,m,T,k,h,f,cnt;
	while(scanf("%d",&T)!=EOF)
	{
		cnt=0;
		while(T--)
		{
			scanf("%d%d",&n,&m);
			f=1;
			cnt++;
			for(i=0;i<n;i++)
			{
				for(j=0;j<m;j++)
				{
					scanf("%d",&c[i][j]);
				}
			}
			for(i=0;i<n;i++)
			{
				for(j=0;j<m;j++)
				{
					for(k=0;k<m;k++)
					{
						if(c[i][j]<c[i][k])
						{
							for(h=0;h<n;h++)
							{
								if(c[i][j]<c[h][j])
								{
									f=0;
									goto loop;
								}
							}
						}
					}
					
				}
			}
			loop:if(f) printf("Case #%d: YES\n",cnt);
			else printf("Case #%d: NO\n",cnt);
		}
	}
	return 0;
} 
