/*#include <stdio.h>
#include <string.h>
int main()
{
	int t, test=0;
	double c, f, x, ans, beg, p, sum;
	freopen("B-large.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		printf("Case #%d: ",++test);
		scanf("%lf%lf%lf",&c,&f,&x);
		if( c >= x)
		{
			printf("%.7lf\n",x/2.0);
			continue;
		}
		ans = x/2.0;
		beg = 0;
		p = 2;

		while(1)
		{
			beg += c/p;
			p += f;
			sum = beg + x/p;
			if( sum > ans)
				break;
			ans = sum;
		}
		printf("%.7lf\n",ans);

	}
//	while(1);
	return 0;
}*/


#include <stdio.h>
#include <string.h>

int vis[6][6];
int r, c;
int dx[8]={-1,-1,-1,0,0,1,1,1}, dy[8]={-1,0,1,-1,1,-1,0,1};
int flag[6][6],count;
void dfs(int x,int y)
{
	int xx, yy, i;
	flag[x][y]=1;
	count++;
	if( vis[x][y] > 0 )
		return;
	for( i = 0; i < 8; i ++ )
	{
		xx = x + dx[i], yy = y+dy[i];
		if( xx < 0 || yy < 0 || xx >= r || yy >= c )	continue;
		if( flag[xx][yy] == 0 && vis[xx][yy] >= 0)
		{
				dfs(xx,yy);
		}
	}
}
int init(int m)
{
	int x = 0, y = 0, ok = 0;
	int i, j;
	for( i = 0; i < r; i ++ )
		for( j = 0; j < c; j ++ )
		{
			if( vis[i][j] == -1 )	continue;
			if( i > 0 && vis[i-1][j] == -1)	 vis[i][j]++;
			if( i < r-1 && vis[i+1][j] == -1)	 vis[i][j]++;
			if( j > 0 && vis[i][j-1] == -1)	 vis[i][j]++;
			if( j < c-1 && vis[i][j+1] == -1)	 vis[i][j]++;
			if( i > 0 && j > 0 && vis[i-1][j-1] == -1)	 vis[i][j]++;
			if( i > 0 && j < c -1 && vis[i-1][j+1] == -1)	 vis[i][j]++;
			if( i < r-1 && j > 0 && vis[i+1][j-1] == -1)	 vis[i][j]++;
			if( i < r-1 && j < c - 1 && vis[i+1][j+1] == -1)	 vis[i][j]++;
			
			if(vis[i][j] == 0 )
			{
				//puts("dd");
				ok = 1;
				x = i, y = j;
			}
		}
	if( ok )
	{
		memset(flag,0,sizeof(flag));
		count = 0;
		dfs(x,y);
		if(count+m==r*c)
		{
			vis[x][y] = -2;
			return 1;
		}

	}

	return 0;
}

int cal(int x, int m)
{
	int s = 0, i;
	for( i = 0; i < 25; i ++ )
	{
		if( x>>i&1 )
			s++;
	}
	if( s == m )
	{
		memset(vis,0,sizeof(vis));
		for( i = 0; i < 25; i ++ )
		{
			if( x >>i & 1)
				vis[i/c][i%c] = -1;
		}
		return 1;
	}
	return 0;
}

int main()
{
	int t, test=0;
	int m, i, j, n;
	freopen("C-small-attempt5.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d%d",&r,&c,&m);
		printf("Case #%d:\n",++test);
		if( m == 0 )
		{
			for( i = 0; i < r; i ++)
			{	for( j = 0; j < c; j ++)
				{
					if( i==0 && j==0)
						printf("c");
					else
						printf(".");
				}
				puts("");
			}
			continue;
		
		}
		else if( m == r*c-1)
		{
			for( i = 0; i < r; i ++)
			{	for( j = 0; j < c; j ++)
				{
					if( i==0 && j==0)
						printf("c");
					else
						printf("*");
				}
				puts("");
			}
			continue;

		}

		n = 1<<(r * c);
		for( i = 0; i < n; i ++ )
		{
			if(cal(i, m))
			{
#if 0
				for(int  ii = 0; ii < r; ii ++)
				{
					for( j = 0; j < c; j ++ )
					{
						printf(" %d",vis[ii][j]);
		
					}
					puts("");
				}
#endif
				if(init(m))
					break;
			}
		}
		if( i == n )
			puts("Impossible");
		else
		{
			for( i = 0; i < r; i ++)
			{
				for( j = 0; j < c; j ++ )
				{
					if( vis[i][j] >= 0 )
						printf(".");
					else if(vis[i][j] == -1)
						printf("*");
					else
						printf("c");

				}
				puts("");
			}
		}
	}
	//while(1);
	return 0;
}