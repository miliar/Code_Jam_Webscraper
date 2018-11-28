#include<stdio.h>

int map[30][30];
int n,m;
int pair[50];
int tmp[30];
int ans[30][30];
int dy[4]={1,0,0,-1}, dx[4]={0,-1,1,0};
int anscheck;

void test(void)
{
	int i,j,x=0,y,sy,sx,fy,fx,sd;
	for(i=1;i<=n;i++)
	{
		for(j=1;j<=m;j++)
			map[i][j]=tmp[++x];
	}

	for(i=0;i<=n+1;i++)
	{
		for(j=0;j<=m+1;j++)
		{
			if(i<1 || i>n || j<1 || j>m)
				map[i][j]=-1;
		}
	}


	for(i=1;i<=n+m;i++)
	{
		x=pair[2*i-1];
		y=pair[2*i];
		
		if(x<=m)
		{
			sy=0;
			sx=x;
			sd=0;
		}
		else if(x<=n+m)
		{
			sy=x-m;
			sx=m+1;
			sd=1;
		}
		else if(x<=n+2*m)
		{
			sy=n+1;
			sx=n+2*m-x+1;
			sd=3;
		}
		else
		{
			sy = 2*(n+m)-x+1;
			sx = 0;
			sd = 2;
		}

		if(y<=m)
		{
			fy=0;
			fx=y;
		}
		else if(y<=n+m)
		{
			fy=y-m;
			fx=m+1;
		}
		else if(y<=n+2*m)
		{
			fy=n+1;
			fx=n+2*m-y+1;
		}
		else
		{
			fy = 2*(n+m)-y+1;
			fx = 0;
		}

		while(1)
		{
			y = sy + dy[sd];
			x = sx + dx[sd];
			if(map[y][x]==-1)
				break;
			sd = sd ^ map[y][x];
			sy=y;
			sx=x;
		}

		if(fy!=y || fx!=x)
		{
			return;
		}
	}

	anscheck=1;

	for(i=1;i<=n;i++)
	{
		for(j=1;j<=m;j++)
			ans[i][j]=map[i][j];
	}

}

void recall(int lev)
{
	if(anscheck==1)
		return;
	if(lev>n*m)
	{
		test();
		return;
	}
	tmp[lev]=1;
	recall(lev+1);
	tmp[lev]=2;
	recall(lev+1);
	tmp[lev]=0;
}

int main(void)
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	int i,t,j,k;
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		scanf("%d %d",&n,&m);
		for(j=1;j<=2*(n+m);j++)
			scanf("%d",&pair[j]);
		printf("Case #%d:\n",i);
		anscheck=0;
		recall(1);
		if(anscheck==0)
			printf("IMPOSSIBLE\n");
		else
		{
			for(k=1;k<=n;k++)
			{
				for(j=1;j<=m;j++)
				{
					if(ans[k][j]==1)
						printf("/");
					else
						printf("\\");
				}
				printf("\n");
			}
		}
	}

}