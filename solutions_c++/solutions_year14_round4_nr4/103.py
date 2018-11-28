#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cstring>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;

#define SIZE(x) (int((x).size()))
#define rep(i,l,r) for (int i=(l); i<=(r); i++)
#define repd(i,r,l) for (int i=(r); i>=(l); i--)
#define rept(i,c) for (typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)

#ifndef ONLINE_JUDGE
#define debug(x) { cerr<<#x<<" = "<<(x)<<endl; }
#else
#define debug(x) {}
#endif

#define maxn 10

int pool[100000][30];

int m,n; 
int tot, root;

int allocate()
{
	tot++; 
	rep(i,0,25) pool[tot][i]=0;
	return tot;
}

void ins(string s)
{
	int cur=root;
	rep(i,0,s.length()-1)
	{
		int z=s[i]-'A';
		if (pool[cur][z]==0) pool[cur][z]=allocate();
		cur=pool[cur][z];
	}
}
	
string s[maxn];
int belong[maxn];

int maxv, way;

void solve()
{
	int cans=0;
	rep(i,1,n)
	{
		tot=0; root=allocate(); int flag=0;
		rep(j,1,m)
			if (belong[j]==i) flag=1, ins(s[j]);
		
		if (!flag) return;
		cans+=tot;
	}
	if (cans>maxv)
	{
		maxv=cans; way=1;
	}
	else  if (cans==maxv) way++;
}

void dfs(int k)
{
	if (k>m) 
	{
		solve();
		return;
	}
	rep(i,1,n) 
	{
		belong[k]=i;
		dfs(k+1);
	}
}

void lemon()
{
	cin>>m>>n;
	rep(i,1,m) cin>>s[i];
	maxv=0; way=0;
	dfs(1);
	printf("%d %d\n",maxv,way);
}

int main()
{
	ios::sync_with_stdio(true);
	#ifndef ONLINE_JUDGE
		freopen("D.in","r",stdin);
	#endif
	int tcase; scanf("%d",&tcase);
	rep(nowcase,1,tcase) 
	{
		printf("Case #%d: ",nowcase);
		lemon();
	}
	return 0;
}

