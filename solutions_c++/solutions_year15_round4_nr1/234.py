#include <stdio.h>

int a[110][110];
int ddx[]={0,-1,1,0,0};
int ddy[]={0,0,0,-1,1};
int main(void)
{
	int tt ,ii;
	int n ,m ,i ,j;
	char s[10] ,c;
	int ans;
	int dx ,dy ,x ,y;
	int aa;
	int jj;
	int temp;
	
	scanf("%d" ,&tt);
	for (ii=1 ; ii<=tt ; ii++)
	{
		scanf("%d %d" ,&n ,&m);
		for (i=1 ; i<=n ; i++)	
		{
			gets(s);
			for (j=1 ; j<=m ; j++)	
			{
				scanf("%c" ,&c);
				if (c=='.')
				{
					a[i][j]=0;
				}
				else if (c=='^')
				{
					a[i][j]=1;	
				}
				else if (c=='v')
				{
					a[i][j]=2;	
				}
				else if (c=='<')
				{
					a[i][j]=3;	
				}
				else if (c=='>')
				{
					a[i][j]=4;	
				}
			}
		}
		ans=0;
		for (i=1 ; i<=n ; i++)
		{
			for (j=1 ; j<=m ; j++)	
			{
				aa=a[i][j];
				if (a[i][j])
				{
					dx=ddx[aa];
					dy=ddy[aa];
					x=i+dx;
					y=j+dy;
					temp=0;
					while (x>=1&&x<=n&&y>=1&&y<=m)
					{
						if (a[x][y])
						{
							temp=1;
							break;	
						}
						x+=dx;
						y+=dy;
					}
					if (!temp)
					{
						for (jj=1 ; jj<=4 ; jj++)
						{
							dx=ddx[jj];
							dy=ddy[jj];
							x=i+dx;
							y=j+dy;
							while (x>=1&&x<=n&&y>=1&&y<=m)
							{
								if (a[x][y])
								{
									temp=1;
									break;	
								}
								x+=dx;
								y+=dy;
							}	
							if (temp)						
							{
								break;	
							}
						}
						if (temp)
						{
							ans++;
						}
						else
						{
							ans=-1;
							break;
						}
					}
				}
			}
			if (ans==-1)
			{
				break;	
			}
		}
		if (ans==-1)
		{
			printf("Case #%d: IMPOSSIBLE\n" ,ii);
		}
		else
		{
			printf("Case #%d: %d\n" ,ii ,ans);			
		}
	}

	return 0;
}
