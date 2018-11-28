#include <iostream>
#include <stdio.h>
#include <set>
#include <string.h>
#include <algorithm>
#include <vector>
#include <time.h>
#include <queue>
#include <math.h>
#define ll long long
using namespace std;
const int N=1009;
int n,dis,m;
struct node
{
	int x,y,t;
	bool operator <(node a)const{return t<a.t;}
	void read(){scanf("%d%d%d",&x,&y,&t);}
	void out(){printf("%d %d %d\n",x,y,t);}
}p[N];
int dp[200][200][11];

bool pic[11][20][20];
bool in(int x,int y)
{
	return x>=0&&x<n&&y>=0&&y<n;
}
int cal(int x,int y,int fx,int fy,int t)
{
	if(fx==0&&fy==0)  return in(x,y)&&pic[t][x][y];	
	int c,ans=0;
	if(fx*fy==0) c=fx?fabs(fx):fabs(fy);
	else c=__gcd(abs(fx),abs(fy));
	for(int i=0;;i++)
	{
		
		int nx=x+fx/c*i;
		int ny=y+fy/c*i;
		
		if(!in(nx,ny)) 
		{
			if(nx==x+fx&&ny==y+fy) return ans;
			continue;
		}
		ans+=pic[t][nx][ny];
		if(nx==x+fx&&ny==y+fy) return ans;
	}
}

int dfs(int x,int y,int t)
{
	if(t==11) return  0;
	int &d=dp[x+100][y+100][t];
	if(d+1) return d;
	d=0;
	for(int i=-dis;i<=dis;i++)
	for(int j=-dis;j<=dis;j++)
	if(i*i+j*j<=dis*dis)
	{
		int add=cal(x,y,i,j,t);

		 if(add||in(x,y))d=max(d,cal(x,y,i,j,t)+dfs(x+i,y+j,t+1));
	}
	return d;
}
int main()
{

	while(scanf("%d%d%d",&n,&dis,&m),n+dis+m)
	{
		memset(pic,0,sizeof(pic));
		for(int i=0;i<m;i++) 
		{
			p[i].read();
			pic[p[i].t][p[i].x][p[i].y]=1;
		}
		memset(dp,-1,sizeof(dp)); 
		int ans=0;
		for(int i=0;i<n;i++)
		for(int j=0;j<n;j++) ans=max(ans,dfs(i,j,1));
		printf("%d\n",ans);
	}
	
	return 0;
}