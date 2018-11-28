#include<cstring>
#include<algorithm>
#include<iostream>
#include<vector>
#include<cstdio>

using namespace std;

const int maxl = 10;

string s[maxl];
int res,cnt,m,n;
int to[maxl];
bool vis[maxl];

vector<string> v;
void check()
{
	int tp = 0;
	for(int i=1;i<=n;i++)
	{
		v.clear();
		for(int j=1;j<=m;j++)
		{
			if(to[j]==i)
				v.push_back(s[j]);
		}
		sort(v.begin(),v.end());
		tp += v[0].size();
		for(int j=1;j<v.size();j++)
		{
			int flag = 0;
			for(int k=0;k<v[j].size()&&k<v[j-1].size();k++)
			{
				if(v[j][k]!=v[j-1][k])
					break;
				else
					flag++;
			}
			tp += v[j].size()-flag;
		}
	}
	if(tp>res)
	{
		res = tp;cnt = 1;
	}
	else if(tp==res)
		cnt++;
}
void dfs(int p)
{
	//printf("p=%d\n",p);
	if(p>m)
	{
		memset(vis,0,sizeof(vis));
		for(int i=1;i<=m;i++)
			vis[to[i]] = 1;
		for(int i=1;i<=n;i++)
			if(!vis[i])
				return ;
		check();
		return ;
	}
	for(int i=1;i<=n;i++)
	{
		to[p] = i;
		dfs(p+1);
	}
}
int main()
{
	int t,cas=0;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d",&m,&n);
		for(int i=1;i<=m;i++)
			cin>>s[i];
		res=cnt=0;dfs(1);
		printf("Case #%d: %d %d\n",++cas,res+n,cnt);
	}
}
