#include<iostream>
#include<cstdlib>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<cassert>
using namespace std;
#define rep(i,n) for(int i=1;i<=(n);++i)
#define rep2(i,a,b) for(int i=(a);i<=(b);++i)
int ind[102][102];
int dir[102][102][5];
int nx,ny;
void task()
{
	scanf("%d%d",&nx,&ny);
	memset(dir,0,sizeof dir);
	char ts[102];
	rep(i,nx)
	{
		scanf("%s",ts);
		rep(j,ny)
		{
			if(ts[j-1]=='.')ind[i][j]=0;
			if(ts[j-1]=='^')ind[i][j]=1;
			if(ts[j-1]=='<')ind[i][j]=2;
			if(ts[j-1]=='v')ind[i][j]=3;
			if(ts[j-1]=='>')ind[i][j]=4;
			if(ind[i][j])
			{
				rep(ti,i-1)dir[ti][j][3]=true;
				rep2(ti,i+1,nx)dir[ti][j][1]=true;
				rep(tj,j-1)dir[i][tj][4]=true;
				rep2(tj,j+1,ny)dir[i][tj][2]=true;
			}
		}
	}
	bool die;
	int res=0;
	rep(i,nx)
	{
		rep(j,ny)
		{
			if(ind[i][j])
			{
				if(!dir[i][j][ind[i][j]])
				{
					die=true;
					rep(idir,4)
					{
						if(dir[i][j][idir])die=false;
					}
					if(die)
					{
						printf("IMPOSSIBLE\n");
						return;
					}
					++res;
				}
			}
		}
	}
	printf("%d\n",res);
}

int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	
	int nt;scanf("%d",&nt);
	rep(it,nt){printf("Case #%d: ",it);task();}
}
