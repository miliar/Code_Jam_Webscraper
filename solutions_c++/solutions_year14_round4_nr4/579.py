#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

int T,col[10],ans,ans2,n,K,tot,head[10],graph[1100][30];
char str[110][110];

void Insert(char s[110],int x)
{
	int len=strlen(s);
	for (int i=0;i<len;i++)
	{
		int c=s[i]-'A';
		if (graph[x][c]==0) graph[x][c]=++tot;
		x=graph[x][c];
	}
}

void dfs(int x)
{
	if (x>n)
	{
		tot=0;
		memset(head,0,sizeof(head));
		memset(graph,0,sizeof(graph));
		for (int i=1;i<=n;i++)
		{
			if (head[col[i]]==0) head[col[i]]=++tot;
			Insert(str[i],head[col[i]]);
		}
		if (tot>ans) ans=tot,ans2=1;
		else if (tot==ans) ans2++;
		return;
	}
	int maxk=0;
	for (int i=1;i<=n;i++)
	{
		maxk=max(col[i],maxk);
	}
	for (int i=1;i<=K;i++)
	{
		col[x]=i;
		dfs(x+1);
	}
}

int main()
{
	scanf("%d",&T);
	for (int tc=1;tc<=T;tc++)
	{
		ans=0,ans2=0;
		scanf("%d%d",&n,&K);
		for (int i=1;i<=n;i++)
		{
			scanf("%s",str[i]);
		} 
		memset(col,0,sizeof(col));
		dfs(1);
		printf("Case #%d: %d %d\n",tc,ans,ans2);
	}


	return 0;
}