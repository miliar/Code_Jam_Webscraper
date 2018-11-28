#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <queue>
#include <vector>
#include <ctime>
#include <set>
#include <bitset>
#include <map>
#include <utility>
#include <iterator>
using namespace std;
inline int get()
{
    int f=0,v=0;char ch;
    while(!isdigit(ch=getchar()))if(ch=='-')break;
    if(ch=='-')f=1;else v=ch-48;
    while(isdigit(ch=getchar()))v=v*10+ch-48;
    if(f==1)return -v;else return v;
}
const int maxn=103;
int g[maxn][30],root[maxn];
int n,m,s[maxn],ans,cnt,tot=0;
char a[maxn][maxn];
void work()
{
	memset(g,0,sizeof(g));
	memset(root,0,sizeof(root));
	tot=0;
	for(int i=1;i<=n;i++)
	{
		if(!root[s[i]])root[s[i]]=++tot;
		int k=root[s[i]],len=strlen(a[i]+1);
		for(int j=1;j<=len;j++)
		{
			int data=a[i][j]-'A';
			if(!g[k][data])g[k][data]=++tot;
			k=g[k][data];
		}
	}
	if(tot>ans){ans=tot,cnt=1;}
	else if(tot==ans)cnt++;
	
}
void dfs(int x)
{
	if(x>n){work();return;}
	for(int i=1;i<=m;i++)s[x]=i,dfs(x+1);
}
int main()
{
    freopen("D.in","r",stdin);
    freopen("D.out","w",stdout);
    int T=get();
    for(int t=1;t<=T;t++)
    {
		cerr<<t<<endl;
		n=get(),m=get();
		for(int i=1;i<=n;i++)scanf("%s",a[i]+1);
		ans=0,cnt=0;
		dfs(1);
		printf("Case #%d: %d %d\n",t,ans,cnt%1000000007);
	}
    return 0;
}
