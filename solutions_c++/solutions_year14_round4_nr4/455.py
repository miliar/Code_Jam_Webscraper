#include<cstdio>
#include<iostream>
#include<string>
#include<algorithm>
#include<set>
using namespace std;
int n,m,a[10],ans,cans;
string s[10];
int calc()
{
	int cnt=0;
	set<string> p[5];
	for(int i=1;i<=m;i++)
	{
		for(int j=0;j<=s[i].length();j++)
		{
			if(!p[a[i]].count(s[i].substr(0,j)))
			{
				cnt++;
				p[a[i]].insert(s[i].substr(0,j));
			}
		}
	}
	return cnt;
}
void dfs(int x)
{
	if(x==0)
	{
		int t=calc();
		if(t>ans)
		{
			ans=t;
			cans=1;
		}
		else if(t==ans)cans++;
	}
	else {
		for(int i=1;i<=n;i++)
		{
			a[x]=i;
			dfs(x-1);
		}
	}
}
int main()
{
	int T;
	scanf("%d",&T);
	for(int tcase=1;tcase<=T;tcase++)
	{
		ans=-1;
		scanf("%d%d",&m,&n);
		for(int i=1;i<=m;i++)cin>>s[i];
		dfs(m);
		printf("Case #%d: %d %d\n",tcase,ans,cans);
	}
}