#include <stdio.h>

int g[110][110];
int f[510];
int sta[510];
int sx[510] ,sy[510] ,se[510];
int np;
int main(void)
{
	int tt ,ii;
	int i ,j ,j2;
	int r ,c ,n;
	int ta ,tb;
	int p;
	int x ,y ,e ,e2;
	int ex ,ey ,ee;
	int ans;
	int a1 ,a2;
	
	scanf("%d" ,&tt);
	for (ii=1 ; ii<=tt ; ii++)
	{
		scanf("%d %d" ,&r ,&c);
		n=2*(r+c);
		for (i=1 ; i<=n ; i+=2)
		{
			scanf("%d %d" ,&ta ,&tb);
			f[ta]=tb;
			f[tb]=ta;
		}
		np=0;
		for (i=1 ; i<=n ; i++)
		{
			sta[++np]=i;
			if (np>1)
			{
				if (f[sta[np]]==sta[np-1])
				{
					np-=2;	
				}
			}
		}
		printf("Case #%d:\n" ,ii);
		if (np==0)
		{
			ans=1;
			for (i=1 ; i<=r ; i++)
			{
				for (j=1 ; j<=c ; j++)
				{
					g[i][j]=0;
					/*for (j2=0 ; j2<=3 ; j2++)
					{
						w[i][j][j2]=0;
					}*/
				}
			}
			p=0;
			for (j=1 ; j<=c ; j++)
			{
//				w[1][j][0]=++p;
				++p;
				sx[p]=1;
				sy[p]=j;
				se[p]=0;
			}
			for (i=1 ; i<=r ; i++)
			{
//				w[i][c][1]=++p;
				++p;
				sx[p]=i;
				sy[p]=c;
				se[p]=1;				
			}			
			for (j=c ; j ; j--)
			{
//				w[r][j][2]=++p;
				++p;
				sx[p]=r;
				sy[p]=j;
				se[p]=2;				
			}
			for (i=r ; i ; i--)
			{
//				w[i][1][3]=++p;
				++p;
				sx[p]=i;
				sy[p]=1;
				se[p]=3;				
			}						
			np=0;
			for (i=1 ; i<=n ; i++)
			{
				sta[++np]=i;
				if (np>1)
				{
					if (f[sta[np]]==sta[np-1])
					{
						a1=sta[np-1];
						a2=sta[np];
						x=sx[a1];
						y=sy[a1];
						e=se[a1];
						ex=sx[a2];
						ey=sy[a2];
						ee=se[a2];
						while (1)
						{
							if (g[x][y]==1)	
							{
									if (e==1||e==3)
									{
										e2=(e+1)%4;
									}
									else
									{
										e2=(e+3)%4;
									}
									
									if (x==ex&&y==ey&&e2==ee)
									{
										break;	
									}
									if (e2==1)
									{
										x=x;
										y=y+1;
										e=3;
									}
									else if (e2==3)
									{
										x=x;
										y=y-1;
										e=1;
									}
									else if (e2==2)
									{
										x=x+1;
										y=y;
										e=0;
									}
									else if (e2==0)
									{
										x=x-1;
										y=y;
										e=2;
									}
									if (y<1||y>c)
									{
										ans=0;
										break;
									}									
									if (x<1||x>r)
									{
										ans=0;
										break;
									}	
							}
							else if (g[x][y]==2)
							{
									if (e==2||e==0)
									{
										e2=(e+1)%4;
									}
									else
									{
										e2=(e+3)%4;
									}
									if (x==ex&&y==ey&&e2==ee)
									{
										break;	
									}
									if (e2==1)
									{
										x=x;
										y=y+1;
										e=3;
									}
									else if (e2==3)
									{
										x=x;
										y=y-1;
										e=1;
									}
									else if (e2==2)
									{
										x=x+1;
										y=y;
										e=0;
									}
									else if (e2==0)
									{
										x=x-1;
										y=y;
										e=2;
									}
									if (y<1||y>c)
									{
										ans=0;
										break;
									}
									if (x<1||x>r)
									{
										ans=0;
										break;
									}
							}
							else
							{
								if (e==0||e==2)
								{
									g[x][y]=2;
									e2=(e+1)%4;
									if (x==ex&&y==ey&&e2==ee)
									{
										break;	
									}
									if (e2==1)
									{
										x=x;
										y=y+1;
										e=3;
									}
									else if (e2==3)
									{
										x=x;
										y=y-1;
										e=1;
									}
									if (y<1||y>c)
									{
										ans=0;
										break;
									}
								}
								else
								{
									g[x][y]=1;								
									e2=(e+1)%4;
									if (x==ex&&y==ey&&e2==ee)
									{
										break;	
									}
									if (e2==2)
									{
										x=x+1;
										y=y;
										e=0;
									}
									else if (e2==0)
									{
										x=x-1;
										y=y;
										e=2;
									}
									if (x<1||x>r)
									{
										ans=0;
										break;
									}									
								}	
							}
						}
						if (!ans)
						{
							break;	
						}
						np-=2;	
					}
				}
			}
			if (ans)
			{
				for (i=1 ; i<=r ; i++)
				{
					for (j=1 ; j<=c ; j++)	
					{
						if (g[i][j]==1)	
						{
							printf("/");
						}
						else
						{
							printf("\\");
						}
					}
					printf("\n");
				}
			}
			else
			{
				printf("IMPOSSIBLE\n");				
			}
		}
		else
		{
			printf("IMPOSSIBLE\n");
		}
	}
	
	
	
	return 0;
}
