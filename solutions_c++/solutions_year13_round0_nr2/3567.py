#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int lawn[101][101];
bool vis[101][101];
int findmin(int (*a)[101],int n, int m)
{
	int minv = 101;
	for(int i = 0; i < n; ++i)
		for(int j = 0; j < m; ++j)
		{
			if(!vis[i][j])
				minv = min(minv,a[i][j]);
		}
	return minv;
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,n,m,curmin;
	bool hflag,vflag,flag,end;
	scanf("%d",&T);
	for(int cas = 1; cas <= T; ++cas)
	{
		scanf("%d%d",&n,&m);
		for(int i = 0; i < n; ++i)
			for(int j = 0; j < m; ++j)
				scanf("%d",lawn[i]+j);
		memset(vis,false,sizeof(vis));
		flag = true;
		end = false;
		while(!end && flag)
		{
			curmin = findmin(lawn,n,m);
			for(int i = 0; i < n && flag; ++i)
			{
				for(int j = 0; j<m; ++j)
				{
					if(lawn[i][j] == curmin)
					{
						hflag = vflag = true;
						for(int k =0; k<m; ++k)
						{
							if(lawn[i][k] > curmin)
							{
								hflag = false;
								break;
							}
						}
						for(int k = 0; k<n && !hflag; ++k)
						{
							if(lawn[k][j] > curmin)
							{
								vflag = false;
								break;
							}
						}
						vis[i][j] = true;
						if(!vflag && !hflag)
						{
							flag = false;
							break;
						}
					}
				}
			}
			end = true;
			for(int i = 0; i < n && end;++i)
				for(int j = 0; j<m; ++j)
				{
					if(vis[i][j] == false)
						end = false;
				}
		}
		if(flag) printf("Case #%d: YES\n",cas);
		else printf("Case #%d: NO\n",cas);
	}
}