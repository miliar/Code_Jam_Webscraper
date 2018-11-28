#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <iostream>
#include <cstdlib>
#include <sstream>

using namespace std;
int nx[100][26];
int pt;
int newnode()
{
	memset(nx[pt],0,sizeof(nx[pt]));
	return pt++;
}
void init()
{
	pt=0;
	newnode();
}
void insert(string s)
{
	int now=0;
	for(int i=0;i<s.size();i++)
	{
		if(!nx[now][s[i]-'A'])nx[now][s[i]-'A']=newnode();
		now=nx[now][s[i]-'A'];
	}
}
int n,m;
string s[10];
int be[10];
int cal()
{
	int ans=0;
	for(int i=0;i<m;i++)
	{
		init();
		for(int j=0;j<n;j++)if(be[j]==i)insert(s[j]);
		ans+=pt;
	}
	return ans;
}
int ans;
void dfs(int now,int sta)
{
	if(now==n)
	{
		if(sta==(1<<m)-1)
		{
			ans=max(ans,cal());
		}
	}
	else
	{
		for(int i=0;i<m;i++)
		{
			be[now]=i;
			dfs(now+1,sta|(1<<i));
		}
	}
}
int ans1;
void dfs1(int now,int sta)
{
	if(now==n)
	{
		if(sta==(1<<m)-1)
		{
			if(cal()==ans)ans1++;
		}
	}
	else
	{
		for(int i=0;i<m;i++)
		{
			be[now]=i;
			dfs1(now+1,sta|(1<<i));
		}
	}
}

void solve()
{
	scanf("%d %d",&n,&m);
	for(int i=0;i<n;i++)cin>>s[i];
	ans=0;
	dfs(0,0);
	ans1=0;
	dfs1(0,0);
	printf("%d %d\n",ans,ans1);
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int cas=1;cas<=T;cas++)
	{
		printf("Case #%d: ",cas);
		solve();
	}
}
