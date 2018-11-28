#include <stdio.h>
#include <stdlib.h>
#include <string.h>
using namespace std;

int T,Case,n,m,i,j,k,ans;
int dx[10],dy[10];
char s[105][105];
bool wei;

bool check(int x,int y,int z)
{
	for(;;)
	{
		x+=dx[z];y+=dy[z];
		if(x<=0||x>n||y<=0||y>m)return false;
		if(s[x][y]!='.')return true;
	}
	return false;
}

int main()
{
	freopen("2.in","r",stdin);
	freopen("2.out","w",stdout);
	scanf("%d",&T);
	dx[1]=1;dx[2]=-1;
	dy[3]=1;dy[4]=-1;
	for(;T;--T)
	{
		scanf("%d%d",&n,&m);
		memset(s,0,sizeof(s));
		for(i=1;i<=n;++i)scanf("%s",s[i]+1);
		wei=false;ans=0;
		for(i=1;i<=n;++i)
		for(j=1;j<=m;++j)
		if(s[i][j]!='.')
		{
			if(s[i][j]=='v')k=1;
			if(s[i][j]=='^')k=2;
			if(s[i][j]=='>')k=3;
			if(s[i][j]=='<')k=4;
			if(check(i,j,k))continue;
			for(k=1;k<=4;++k)
			if(check(i,j,k))break;
			if(k<=4)++ans;else wei=true;
		}
		++Case;
		printf("Case #%d: ",Case);
		if(wei)printf("IMPOSSIBLE\n");
		else printf("%d\n",ans);
	}
}
