#include<iostream>
#include<cstdlib>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<ctime>
#include<algorithm>
#include<list>
#include<queue>
#include<stack>
#include<vector>
#include<set>
#include<map>
#include<string>
#define REP(it,end) for (int it = 1; it <= (end); it++)
#define FOR(it,begin,end) for (int it = (begin); it <= (end); it++)
#define ROF(it,begin,end) for (int it = (begin); it >= (end); it--)
using namespace std;
char mp[120][120];
int ans;
int r,c;
bool find(int i,int j)
{
	int x,y;
	for(x=i+1;x<r&&mp[x][j]=='.';x++);
	if(x<r)return true;
	for(x=i-1;x>=0&&mp[x][j]=='.';x--);
	if(x>=0)return true;
	for(y=j+1;y<c&&mp[i][y]=='.';y++);
	if(y<c)return true;
	for(y=j-1;y>=0&&mp[i][y]=='.';y--);
	if(y>=0)return true;
}
bool solve()
{
	int i,j,x,y;
	ans=0;
	for(i=0;i<r;i++)
		for(j=0;j<c;j++)
		{
			if(mp[i][j]=='^')
			{
				for(x=i-1;x>=0&&mp[x][j]=='.';x--);	
				if(x==-1)
				{
					if(!find(i,j))return false;
					else ans++;
				}
			}
			else if(mp[i][j]=='v')
			{
				for(x=i+1;x<r&&mp[x][j]=='.';x++);
				if(x==r)
				{
					if(!find(i,j))return false;
					else ans++;
				}
			}
			else if(mp[i][j]=='<')
			{
				for(y=j-1;y>=0&&mp[i][y]=='.';y--);
				if(y==-1)
				{
					if(!find(i,j))return false;
					else ans++;
				}
			}
			else if(mp[i][j]=='>')
			{
				for(y=j+1;y<c&&mp[i][y]=='.';y++);
				if(y==c)
				{
					if(!find(i,j))return false;
					else ans++;
				}
			}
		}
	return true;
}
int main()
{
	int T,i,j,x,y;
	scanf("%d",&T);
	for(int cas=1;cas<=T;cas++)
	{
		scanf("%d %d",&r,&c);
		for(i=0;i<r;i++)
			scanf("%s",mp[i]);
		if(solve())printf("Case #%d: %d\n",cas,ans);
		else printf("Case #%d: IMPOSSIBLE\n",cas,ans);
	}
	return 0;
}
