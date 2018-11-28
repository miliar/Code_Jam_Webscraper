#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
using namespace std;

char map[7][7],mark[7][7];
int dir[8][2]={{1,0},{-1,0},{0,1},{0,-1},{1,1},{-1,-1},{1,-1},{-1,1}};
int n,m,p;
int cnt_blank,flag;
int count(int x,int y)
{
	int res=0;
	for (int i=0;i<8;i++)
	{
		int nx=x+dir[i][0], ny=y+dir[i][1];
		if (nx>=0&&nx<n&&ny>=0&&ny<m&&map[nx][ny]=='*')
			res++;
	}
	return res;
}

void flood(int x,int y)
{
	mark[x][y]=1;
	cnt_blank++;

	if (count(x,y)==0)
	{
		for (int i=0;i<8;i++)
		{
			int nx=x+dir[i][0], ny=y+dir[i][1];
			if (nx>=0&&nx<n&&ny>=0&&ny<m&&mark[nx][ny]==0&&map[nx][ny]!='*')
				flood(nx,ny);
		}
	}
}

int check(int sx,int sy)
{
	memset(mark,0,sizeof(mark));
	cnt_blank=0;
	flood(sx,sy);
	if (cnt_blank==n*m-p)
		return 1;
	else
		return 0;
}

void dfs(int x,int y,int cur)
{
	if (cur==p)
	{
		for (int i=0;i<n&&flag==0;i++)
			for (int j=0;j<m&&flag==0;j++)
				if (map[i][j]!='*' && check(i,j))
				{
					map[i][j]='c';
					flag=1;
				}
		return;
	}

	int nx,ny;
	if (y==m-1) {nx=x+1; ny=0;}
	else {nx=x; ny=y+1;}

	if (nx<n&&ny<m)
	{
		map[x][y]='*';
		dfs(nx,ny,cur+1);
		if (flag) return;
		map[x][y]='.';
		dfs(nx,ny,cur);
	}
}

void output()
{
	for (int i=0;i<n;i++)
	{
		for (int j=0;j<m;j++)
			printf("%c",map[i][j]);
		printf("\n");
	}
}

int main()
{
	int t,cas=0;

	freopen("C-small-attempt0.in","r",stdin);
	freopen("C.out","w",stdout);

	scanf("%d",&cas);
	for (int ca=1;ca<=cas;ca++)
	{
		memset(map,'.',sizeof(map));
		scanf("%d%d%d",&n,&m,&p);
		printf("Case #%d:\n",ca);
		flag=0;
		dfs(0,0,0);
		if (flag)
			output();
		else
			printf("Impossible\n");
	}

	return 0;
}
