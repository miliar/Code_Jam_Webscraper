#include<cstdio>
#include<cassert>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<set>
#include<map>
#include<vector>
#include<queue>
#include<functional>

using namespace std;

#define mp make_pair
#define pb push_back
#define fi first
#define se second

typedef long long llint;

char s[30][30];
int c[30],d[30];
int cnt,ans,n;

bool calc(int k)
{
	if (k==n)
		return true;
	int tmp=0;
	for(int i=0;i<n;i++) if (c[i]==0&&s[d[k]][i]=='1')
	{
		c[i]=1;
		if (!calc(k+1)) return false;
		c[i]=0;
		tmp++;
	}
	if (!tmp) return false;
	return true;
}

void dfs(int x,int y)
{
	if (cnt>=ans)
		return;
	if (y==n)
	{
		x++;y=0;
	}
	if (x==n)
	{
		/*
		int flag=1;
		for(int i=0;i<3;i++)
			for(int j=0;j<3;j++) if (s[i][j]!='1')
				flag=0;
		if (flag)
		{
			puts("!!");
		}
		*/
		for(int i=0;i<n;i++) c[i]=0;
		for(int i=0;i<n;i++) d[i]=i;
		do
		{
			if (!calc(0)) return;
		} while(next_permutation(d,d+n));
		ans=cnt;
		return;
	}
	dfs(x,y+1);
	if (s[x][y]=='0')
	{
		s[x][y]='1';
		cnt++;
		dfs(x,y+1);
		cnt--;
		s[x][y]='0';
	}
}

int main()
{
	freopen("D.in","r",stdin);
	int T;
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++)
	{
		scanf("%d",&n);
		for(int i=0;i<n;i++) scanf("%s",s[i]);
		ans=n*n+1;
		cnt=0;
		dfs(0,0);
		assert(ans!=n*n+1);
		printf("Case #%d: %d\n", tt,ans);
	}
	
	return 0;
}