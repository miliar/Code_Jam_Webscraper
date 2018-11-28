#include<cstdio>
#include<cstdlib>
#include<ctime>
#include<algorithm>
#include<cstring>
using namespace std;
const int N = 52005 ;
int R,C,M,fr,ck;
int c[8][2]={1,0,0,1,-1,0,0,-1,1,1,-1,-1,1,-1,-1,1},t[10][10];
char s[10][10];
bool u[10][10];
void ddfs(int i,int j)
{
	u[i][j]=true;
	ck++;
	for(int h=0;h<8;h++)
	{
		int x=i+c[h][0];
		int y=j+c[h][1];
		if(x>=0&&y>=0&&x<R&&y<C&&s[x][y]!='*'&&!t[x][y]&&!u[x][y])
		{
			ddfs(x,y);
		}
	}
}
bool check()
{
	int i,j,h;
	if(R*C-M==1)
	{
		for(i=0;i<R;i++)
		{
			for(j=0;j<C;j++)
			{
				if(s[i][j]!='*')s[i][j]='c';
			}
		}
		return true;
	}
	for(i=0;i<R;i++)
	{
		for(j=0;j<C;j++)if(s[i][j]!='*')
		{
			t[i][j]=0;
			for(h=0;h<8;h++)
			{
				int x=i+c[h][0];
				int y=j+c[h][1];
				if(x>=0&&y>=0&&x<R&&y<C&&s[x][y]=='*')t[i][j]++;
			}
		}
	}
	for(i=0;i<R;i++)
	{
		for(j=0;j<C;j++)if(s[i][j]!='*'&&t[i][j]>0)
		{
			int f=0;
			for(h=0;h<8;h++)
			{
				int x=i+c[h][0];
				int y=j+c[h][1];
				if(x>=0&&y>=0&&x<R&&y<C&&s[x][y]!='*'&&!t[x][y])f=1;
			}
			if(!f)return false;
		}
	}
	int tt=0;
	for(i=0;i<R;i++)for(j=0;j<C;j++)if(s[i][j]!='*'&&!t[i][j])tt++;
	memset(u,0,sizeof(u));
	for(i=0;i<R;i++)
	{
		for(j=0;j<C;j++)if(s[i][j]!='*'&&!t[i][j])
		{
			ck=0;
			ddfs(i,j);
			if(ck!=tt)return false;
			i=R;
			j=C;
		}
	}
	/*puts("-------");
	for(i=0;i<R;i++)
	{
		for(j=0;j<C;j++)putchar(s[i][j]);
		puts("");
	}
	for(i=0;i<R;i++)
	{
		for(j=0;j<C;j++)printf("%d ",t[i][j]);
		puts("");
	}
	puts("-------");*/
	for(i=0;i<R;i++)
	{
		for(j=0;j<C;j++)if(s[i][j]!='*'&&!t[i][j])
		{
			s[i][j]='c';
			return true;
		}
	}
}
void dfs(int x,int y,int k)
{
	if(fr)return ;
	if(x==R)
	{
		if(!k&&check())fr=1;
		return ;
	}
	if(y==C)dfs(x+1,0,k);
	else
	{
		if(k)
		{
			s[x][y]='*';
			dfs(x,y+1,k-1);
		}
		if(fr)return ;
		s[x][y]='.';
		dfs(x,y+1,k);
	}
}
int main(){
	int T,h,i,j;
	scanf("%d",&T);
	for(h=1;h<=T;h++)
	{
		scanf("%d%d%d",&R,&C,&M);
		fr=0;
		dfs(0,0,M);
		printf("Case #%d:\n",h);
		if(!fr)puts("Impossible");
		else
		{
			for(i=0;i<R;i++)
			{
				for(j=0;j<C;j++)putchar(s[i][j]);
				puts("");
			}
		}
	}
	return 0;
}
