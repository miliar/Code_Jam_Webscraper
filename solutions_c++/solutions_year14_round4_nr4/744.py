#include<iostream>
#include<fstream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<iomanip>
#include<ctime>
#include<cstring>
#include<climits>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<set>
#include<algorithm>
#include<stack>
#include<deque>
#include<list>
#include<vector>
#define LL long long
using namespace std;
int cnt,snt,n,L,m,times;
LL oo=1000000007;
char s[1010][12];
int a[1010][1010],ans,maxn;
bool vis[1010];
int sum[1010];
struct node
{
	node *next[26];
	node()
	{
		memset(next,0,sizeof(next));
	}
}*ROOT;
void insert(char *s,int len)
{
	node *p=ROOT;
	for (int i=0;i<len;i++)
	{
		if (p->next[s[i]-'A']) p=p->next[s[i]-'A'];
		else 
		{
			p->next[s[i]-'A']=new node();
			p=p->next[s[i]-'A'];
			cnt++;
		}
	}
}
void clear(node *p)
{
	if (!p) return;
	for (int i=0;i<26;i++) clear(p->next[i]);
	delete p;
}
void calc(int x)
{
	ROOT=new node();cnt++;
	for (int i=1;i<=a[x][0];i++)
	{
		insert(s[a[x][i]],strlen(s[a[x][i]]));
	}
	clear(ROOT);
}
void dfs(int x,int y)
{
	if (x==n+1)
	{
		for (int i=1;i<=m;i++) if (!vis[i]) return;
		cnt=0;
		for (int i=1;i<=n;i++) calc(i);
	
		sum[cnt]+=1;
		return;
	}
	if (a[x][0]!=0) dfs(x+1,1);
	for (int i=y;i<=m;i++)
	if (!vis[i])
	{
		vis[i]=true;
		a[x][++a[x][0]]=i;
		dfs(x,i+1);
		a[x][0]--;
		vis[i]=false;
	}	
}
void work(int lab)
{
	scanf("%d%d",&m,&n);
	for (int i=1;i<=m;i++) scanf("%s",s[i]);
	memset(vis,0,sizeof(vis));
	memset(sum,0,sizeof(sum));
	dfs(1,1);
	for (int i=1;i<=1000;i++)
	if (sum[i]>0)
	{
		maxn=i;
		ans=sum[i];
	}
	printf("Case #%d: %d %d\n",lab,maxn,ans);
}
int main()
{
	freopen("data.in","r",stdin);
	freopen("data.out","w",stdout);
	scanf("%d",&times);
	for (int i=1;i<=times;i++)
	work(i);
	return 0;
}


