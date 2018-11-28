#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int map[102][102];
int n,m;
bool check(int x,int y)
{
	int ans=0;
	for(int i=0;i<m;++i)
	{
		if(map[x][i]>map[x][y]){++ans;break;}
	}
	for(int i=0;i<n;++i)
	{
		if(map[i][y]>map[x][y]){++ans;break;}
	}
	if(ans<2)return true;
	return false; 
}
int main()
{
	int cas,c;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	while(~scanf("%d",&cas))
	{
		c=1;
		while(cas--)
		{
			scanf("%d%d",&n,&m);
			for(int i=0;i<n;++i)
			{
				for(int j=0;j<m;++j)
				{
					scanf("%d",&map[i][j]);
				}
			}
			bool ans=true;
			for(int i=0;i<n;++i)
			{
				for(int j=0;j<m;++j)
				{
					ans=check(i,j);
					if(ans==false)break;
				}
				if(ans==false)break;
			}
			if(ans==true){printf("Case #%d: YES\n",c);}
			else{printf("Case #%d: NO\n",c);}
			++c;
		}
	}
	return 0;
}
