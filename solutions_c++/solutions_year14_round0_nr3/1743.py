#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iostream>
using namespace std;

const int walk[8][2]={{-1,-1},{-1,0},{-1,1},{0,1},{1,1},{1,0},{1,-1},{0,-1}};

int N, M, C, clx, cly, num[10][10];
bool mine[10][10], flag[10][10];

void floodFill(int x, int y)
{
	if (flag[x][y]) return;
	flag[x][y]=true;
	if (!x || !y || x>N || y>M || num[x][y] || mine[x][y]) return;
	for (int k=0;k<8;k++)
		floodFill(x+walk[k][0],y+walk[k][1]);
}

bool check()
{
	memset(num,0,sizeof num);
	for (int i=1;i<=N;i++)
		for (int j=1;j<=M;j++)
			for (int k=0;k<8;k++) if (mine[i+walk[k][0]][j+walk[k][1]])
				num[i][j]++;
	memset(flag,0,sizeof flag);
	bool once(false);
	for (int i=1;i<=N;i++)
	{
		for (int j=1;j<=M;j++)
			if (!mine[i][j] && !num[i][j])
			{
				floodFill(i,j);
				clx=i, cly=j;
				once=true;
				break;
			}
		if (once) break;
	}
	for (int i=1;i<=N;i++)
		for (int j=1;j<=M;j++)
			if (!mine[i][j] && !flag[i][j])
				if (once)
					return false;
				else
					clx=i, cly=j, once=true;
	return true;
}

bool Dfs(int x, int t)
{
	if (N*M-x+1<C-t) return false;
	if (t==C)
	{
		if (!check()) return false;
		for (int i=1;i<=N;i++)
		{
			for (int j=1;j<=M;j++)
				if (mine[i][j]) putchar('*'); else if (i==clx && j==cly) putchar('c'); else putchar('.');
			putchar('\n');
		}
		return true;
	}
	for (int i=x;i<=N*M;i++)
	{
		mine[(i-1)/M+1][(i-1)%M+1]=true;
		if (Dfs(i+1,t+1)) return true;
		mine[(i-1)/M+1][(i-1)%M+1]=false;
	}
	return false;
}

int main()
{
	freopen("mine.in","r",stdin);
	freopen("mine.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int TT=1;TT<=T;TT++)
	{
		cerr<<TT<<endl;
		printf("Case #%d:\n",TT);
		scanf("%d%d%d",&N,&M,&C);
		memset(mine,0,sizeof mine);
		if (!Dfs(1,0)) printf("Impossible\n");
	}
	return 0;
}

