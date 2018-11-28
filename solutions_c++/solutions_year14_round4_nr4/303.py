#include <set>
#include <cmath>
#include <stack>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <numeric>
#include <vector>
#include <ctime>
#include <queue>
#include <list>
#include <map>
#define pi acos(-1.0)
#define INF 0x3f3f3f3f
#define clr(x)  memset(x,0,sizeof(x));
#define clrto(x,siz,y)  for(int xx=0;xx<=siz;xx++)  x[xx]=y;
#define clrset(x,siz)  for(int xx=0;xx<=siz;xx++)  x[xx]=xx;
#define clr_1(x) memset(x,-1,sizeof(x));
#define clrmax(x) memset(x,0x3f,sizeof(x));
#define clrvec(x,siz) for(int xx=0;xx<=siz;xx++)  x[xx].clear();
#define fop2   freopen(".in","r",stdin); //freopen(".out","w",stdout);
#define fop   freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
#define myprogram By_135678942570
#define clrcpy(x,siz,y)  for(int xx=0;xx<siz;xx++)  x[xx]=y[xx];
#define pb push_back
using namespace std;
string s[10];
int color[11]={0};
int ans1,ans2;
int n,m;
struct node
{
	int nxt[33];
}N[5][100];
int siz[5];
void insert(int id,int pos,int from,int now)
{
	if(pos==s[id].size())
		return;
	if(N[from][now].nxt[s[id][pos]-'A']==0)
	{
		siz[from]++;
		N[from][now].nxt[s[id][pos]-'A']=siz[from];
	}
	insert(id,pos+1,from,N[from][now].nxt[s[id][pos]-'A']);
}
void dfs(int dep)
{
	if(dep==n)
	{
		clr(N);
		clr(siz);
		for(int i=0;i<n;i++)
			insert(i,0,color[i],0);
		int sum=0;
		for(int i=0;i<m;i++)
		{
			if(siz[i]==0)
				return;
			sum+=siz[i]+1;
		}
		if(sum>ans1)
		{
			ans1=sum;
			ans2=1;
		}
		if(sum==ans1)
		{
			ans2++;
		}
		return;
	}
	for(int i=0;i<m;i++)
	{
		color[dep]=i;
		dfs(dep+1);
	}
	return;
}
int main()
{
	fop;
	int T,cas=0;
	scanf("%d",&T);
	while(T--)
	{
		clr(N);
		clr(siz);
		ans1=0,ans2=0;
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;i++)
			cin>>s[i];
		clr(color);
		dfs(0);
		printf("Case #%d: %d %d\n",++cas,ans1,ans2-1);
	}
}