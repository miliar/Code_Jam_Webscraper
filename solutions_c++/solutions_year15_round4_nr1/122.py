#include<bits/stdc++.h>
using namespace std;
const int N=110,M=110,L=110;
char buf[L]={},ch[N][M]={};
int n,m;
bool exist(int x,int y,char dir)
{
	int dx=0,dy=0;
	switch(dir)
	{
		case '<' : dx=0,dy=-1; break;
		case '>' : dx=0,dy=1; break;
		case '^' : dx=-1,dy=0; break;
		case 'v' : dx=1,dy=0; break;
	}
	int nx=x+dx,ny=y+dy;
	while(1<=nx && nx<=n && 1<=ny && ny<=m)
	{
		if(ch[nx][ny]!='.')
			return true;
		nx+=dx,ny+=dy;
	}
	return false;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	gets(buf);
	int T;
	sscanf(buf,"%d",&T);
	for(int t=1;t<=T;++t)
	{
		gets(buf);
		sscanf(buf,"%d %d",&n,&m);
		for(int i=1;i<=n;++i)
			gets(ch[i]+1);
		printf("Case #%d: ",t);
		int ans=0;
		for(int i=1;i<=n;++i)
			for(int j=1;j<=m;++j)
				if(ch[i][j]!='.' && !exist(i,j,ch[i][j]))
				{
					++ans;
					bool flag=false;
					flag|=exist(i,j,'<');
					flag|=exist(i,j,'>');
					flag|=exist(i,j,'^');
					flag|=exist(i,j,'v');
					if(!flag)
					{
						ans=-1;
						goto out;
					}
				}
		out:
		if(ans==-1)
			puts("IMPOSSIBLE");
		else
			printf("%d\n",ans);
	}
	return 0;
}
