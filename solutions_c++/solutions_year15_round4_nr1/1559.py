#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

const int dx[4] = {-1, 0, 1, 0};
const int dy[4] = {0, 1, 0, -1};

char mp[102][102];
int ans;

int T,n,m;

void tjb(int x,int y,int r)
{
	
}

bool check()
{
	for(int i=1;i<=n;++i)
		for(int j=1;j<=m;++j)
		{
			if(mp[i][j]=='.')continue;
			bool flag=false;
			for(int k=0;k<4;++k)
			{
				int nx=i+dx[k];
				int ny=j+dy[k];
				while(nx>0&&ny>0&&nx<=n&&ny<=m)
					{
						if(mp[nx][ny]=='.')
						{
							nx=nx+dx[k];
							ny=ny+dy[k];
						}else break;
					}
				if(nx>0&&ny>0&&nx<=n&&ny<=m)
				{
					flag=true;
					break;
				}
			}
			if(!flag)return false;
		}	
	return true;
}

int main()
{
	//freopen("input.txt","r",stdin);
	//freopen("b.txt","w",stdout);
	
	scanf("%d\n",&T);
	
	for(int ii=1;ii<=T;++ii)
	{
		ans=0;
		scanf("%d%d\n",&n,&m);
		for(int i=1;i<=n;++i)
		{
			for(int j=1;j<=m;++j)
			{
				mp[i][j]=getchar();
			//	printf("%c",mp[i][j]);
			}
			//printf("\n");
			scanf("\n");
		}
		if(!check())
		{
			printf("Case #%d: IMPOSSIBLE\n",ii);
			continue;
		}	
		int s=n*m+1;
		int t=s+1;
		for(int i=1;i<=n;++i)
			for(int j=1;j<=m;++j)
			{
				//tjb(s,i*m-m+j,1);
				int opt=5;
				if(mp[i][j]=='^')opt=0;
				if(mp[i][j]=='>')opt=1;
				if(mp[i][j]=='v')opt=2;
				if(mp[i][j]=='<')opt=3;
				if(opt<4)
				{
					int nx=i+dx[opt];
					int ny=j+dy[opt];
					while(nx>0&&ny>0&&nx<=n&&ny<=m)
					{
						if(mp[nx][ny]=='.')
						{
							nx=nx+dx[opt];
							ny=ny+dy[opt];
						}else break;
					}
					if(nx>0&&ny>0&&nx<=n&&ny<=m);
					else
					{
					//	tjb(i*m-m+j,t,1);
						++ans;
					}
				}
				
			}
		printf("Case #%d: %d\n",ii,ans);
	}
}