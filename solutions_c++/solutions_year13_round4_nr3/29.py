/*
	Author : ChnLich
*/
#include<cstdio>
#include<cmath>
#include<iomanip>
#include<cstring>
#include<cstdlib>
#include<ctime>
#include<iostream>
#include<sstream>
#include<fstream>
#include<algorithm>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<deque>
#include<set>
#include<map>
#include<string>
#include<bitset>
#include<functional>
#include<utility>

using namespace std;

typedef long long llint;
typedef pair<int,int> ipair;
typedef unsigned int uint;
#define pb push_back
#define fi first
#define se second
#define mp make_pair

const int MOD=1000000007,dx[]={0,1,0,-1},dy[]={1,0,-1,0};
const double eps=1e-8;

void read(int &k)
{
	k=0; char x=getchar();
	while(x<'0'||x>'9') x=getchar();
	while(x>='0'&&x<='9') { k=k*10-48+x; x=getchar(); }
}

int n,ans[2010],len,lis[2010],A[2010],B[2010];

struct graph
{
	int a[2010][2010],l[2010],vis[2010];
	void clear()
	{
		memset(a,0,sizeof a);
		memset(l,0,sizeof l);
		memset(vis,0,sizeof vis);
	}
	void addedge(int x,int y)
	{
		//printf("%d %d\n",x,y);
		if (!a[x][y])a[x][y]=1,l[y]++;
	}
	void topsort()
	{
		len=0;
		for(int P=n;P;P--)
		{
			for(int i=1;i<=n;i++) if (!l[i]&&!vis[i])
			{
				vis[i]=1; lis[++len]=i;
				for(int j=1;j<=n;j++) if (a[i][j]) l[j]--;
				break;
			}
		}
	}
} g;

int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	
	int T;
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++)
	{
		scanf("%d",&n);
		g.clear();
		for(int i=1;i<=n;i++) scanf("%d",A+i);
		for(int i=1;i<=n;i++) scanf("%d",B+i);
		for(int i=1;i<=n;i++)
			for(int j=i+1;j<=n;j++)
			{
				if (A[i]>=A[j]) g.addedge(j,i);
				if (B[i]<=B[j]) g.addedge(i,j);
			}
		for(int i=1;i<=n;i++) if (A[i]>1)
			for(int j=i-1;j;j--) if (A[j]==A[i]-1)
			{
				g.addedge(j,i);
				break;
			}
		for(int i=1;i<=n;i++) if (B[i]>1)
			for(int j=i+1;j<=n;j++) if (B[j]==B[i]-1)
			{
				g.addedge(j,i);
				break;
			}
		g.topsort();
		for(int i=1;i<=n;i++) ans[lis[i]]=i;
		printf("Case #%d:",tt);
		for(int i=1;i<=n;i++) printf(" %d",ans[i]); puts("");
	}
	
	return 0;
}
