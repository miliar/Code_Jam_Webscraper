#include <algorithm>
#include <cstdio>
#include <iostream>
#include <map>
#include <set>
#include <utility>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <queue>

#define mp make_pair
#define pb push_back

using namespace std;

typedef long long big;
const int MOD=1000000007;
struct node
{
	node *c[26];
}mem[200000],*root[2000],*cur;
int belong[200];
int ans1,ans2;
string a[200];
int n,m;
node *newnode()
{
	int i;
	cur++;
	for(i=0;i<26;i++)
		cur->c[i]=0;
	return cur;
}
void ins(node *rt,string str)
{
	int i,c;
	node *now=rt;
	for(i=0;i<str.size();i++)
	{
		c=str[i]-'A';
		if(!now->c[c])now->c[c]=newnode();
		now=now->c[c];
	}
}
int cal()
{
	int i,j;
	for(j=1;j<=m;j++)
	{
		for(i=1;i<=n;i++)
			if(belong[i]==j)
				break;
		if(i==n+1)return 0;
	}
	cur=mem;
	for(i=1;i<=m;i++)
		root[i]=newnode();
	for(i=1;i<=n;i++)
		ins(root[belong[i]],a[i]);
	return cur-mem;
}
void dfs(int dep)
{
	int i;
	if(dep==n+1)
	{
		int t=cal();
		if(t>ans1)ans1=t,ans2=1;
		else if(t==ans1)ans2++;
		return ;
	}
	for(i=1;i<=m;i++)
	{
		belong[dep]=i;
		dfs(dep+1);
	}
}
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.txt","w",stdout);
	int i,cas,cass,j,k,mx,x1,y1,x2,y2,x,y;
	scanf("%d",&cas);
	for(cass=1;cass<=cas;cass++)
	{
		scanf("%d%d",&n,&m);
		for(i=1;i<=n;i++)
			cin>>a[i];
		ans1=-1;ans2=0;
		dfs(1);
		printf("Case #%d: ",cass);
		printf("%d %d\n",ans1,ans2);
	}
}
