#include<cstdio>
#include<cstring>
#include<string>
#include<vector>
#include<algorithm>
#include<iostream>
#include<map>
using namespace std;
const int INF = 1000000005;
const int N = 1005;
typedef __int64 ll;
string s[10];
int n,m,bg[10];
int tri[10][101][26],cnt[10],len[10];
int r1,r2;
void build(string s,int id)
{
	int &k=len[id];
	int n=s.size(),c=0;
	for(int i=0;i<n;i++)
	{
		int j=s[i]-'A';
		if(!tri[id][c][j])
		{
			tri[id][c][j]=++k;
		}
		c=tri[id][c][j];
	}
}
int f=0;
void dfs(int c)
{
	if(c==n)
	{
		memset(cnt,0,sizeof(cnt));
		for(int i=0;i<n;i++)
		{
			cnt[bg[i]]++;
		}
		for(int i=0;i<m;i++)if(!cnt[i])return ;
		memset(len,0,sizeof(len));
		memset(tri,0,sizeof(tri));
		for(int i=0;i<n;i++)
		{
			build(s[i],bg[i]);
		}
		int tot=0;
		for(int i=0;i<m;i++)
		{
			tot+=len[i]+1;
		}
		if(tot>r1)
		{
			r1=tot;
			r2=1;
		}
		else if(tot==r1)
		{
			r2++;
		}
		f++;;
		return ;
	}
	for(int i=0;i<m;i++)
	{
		bg[c]=i;
		dfs(c+1);
	}
}
int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,ca=1;
	scanf("%d",&T);
	while(T--)
	{
		printf("Case #%d: ",ca++);
		int i;
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++)cin >> s[i];
		r1=0;
		dfs(0);
		printf("%d %d\n",r1,r2);
	}
	return 0;
}