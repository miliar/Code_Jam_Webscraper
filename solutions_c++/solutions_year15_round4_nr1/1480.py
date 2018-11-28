#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <queue>
#include <vector>
#include <map>
#include <set>
#include <iostream>
#define maxn 200
using namespace std;
char s[maxn][maxn];
int n,m;
int dx[]={-1,0,1,0};
int dy[]={0,1,0,-1};
int id(char c)
{
	if(c=='^')
		return 0;
	else if(c=='>')
		return 1;
	else if(c=='v')
		return 2;
	else
		return 3;
}
bool in(int x,int y)
{
	return x>=0&&x<n&&y>=0&&y<m;
}
int dfs(int x,int y,int d,int step)
{
	if(!in(x,y))
		return 0;
	if(s[x][y]!='.'&&step!=0)
		return 1;
	return dfs(x+dx[d],y+dy[d],d,step+1);
}
int solve(int x,int y)
{
	bool ok=0;
	for(int i=0;i<4;i++)
	{
		if(dfs(x,y,i,0))
		{
			ok=1;
			break;
		}
	}
	if(!ok)
		return -1;
	if(dfs(x,y,id(s[x][y]),0))
		return 0;
	else
		return 1;
}
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int tt,cot=1;
	scanf("%d",&tt);
	while(tt--)
	{
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;i++)
			scanf("%s",s[i]);
		bool ok=1;
		int ans=0;
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				if(s[i][j]!='.')
				{
					int res=solve(i,j);
					if(res==-1)
					{
						ok=0;
					}
					ans+=res;
				}
			}
		}
		if(!ok)
		{
			printf("Case #%d: IMPOSSIBLE\n",cot++);
		}
		else
		{
			printf("Case #%d: %d\n",cot++,ans);
		}
	}
	//system("pause");
	return 0;
}