#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <queue>
#include <vector>
#include <map>

typedef long long LL;

using namespace std;

bool flag,dqflag;
int T,n,m;
char s[105][105];
int ans;
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&T);
	for (int z=1;z<=T;++z)
	{
		scanf("%d%d",&n,&m);
		for (int i=0;i<n;++i) scanf("%s",s[i]);
		ans=0;flag=true;
		for (int i=0;i<n;++i)
			for (int j=0;j<m;++j)
			{
				dqflag=false;
				if (s[i][j]=='.') continue;
				if (s[i][j]=='>')
				{
					for (int k=j+1;k<m;++k) if (s[i][k]!='.') dqflag=true;
				}
				if (s[i][j]=='<')
				{
					for (int k=j-1;k>=0;--k) if (s[i][k]!='.') dqflag=true;
				}
				if (s[i][j]=='v')
				{
					for (int k=i+1;k<n;++k) if (s[k][j]!='.') dqflag=true;
				}
				if (s[i][j]=='^')
				{
					for (int k=i-1;k>=0;--k) if (s[k][j]!='.') dqflag=true;
				}
				if (dqflag) continue;
				for (int k=j+1;k<m;++k) if (s[i][k]!='.') dqflag=true;
				for (int k=j-1;k>=0;--k) if (s[i][k]!='.') dqflag=true;
				for (int k=i+1;k<n;++k) if (s[k][j]!='.') dqflag=true;
				for (int k=i-1;k>=0;--k) if (s[k][j]!='.') dqflag=true;
				if (dqflag)
				{
					ans++;
				}
				else
				{
					flag=false;
				}
			}
		printf("Case #%d: ",z);
		if (!flag)
		{
			printf("IMPOSSIBLE\n");
		}
		else
		{
			printf("%d\n",ans);
		}
	}
	return 0;
}
