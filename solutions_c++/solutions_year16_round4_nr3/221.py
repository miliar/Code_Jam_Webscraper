#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <cassert>

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

#define maxn 1010

int vis[70];
int d[100], which[100];
int w[20][20];
int goal;
int n,m; 
vector<int> e[100];

int conv(int i, int j, int k)
{
	int t=(i-1)*m+j;
	return (t-1)*4+k;
}

int addedge(int i1, int j1, int k1, int i2, int j2, int k2)
{
	int t1=conv(i1,j1,k1), t2=conv(i2,j2,k2);
	e[t1].push_back(t2);
	e[t2].push_back(t1);
}

int flood(int x)
{
	if (x==goal) return 1;
	if (vis[x]) return 0; 
	vis[x]=1;
	rept(it,e[x])
		if (flood(*it)) return 1;
	return 0;
}

void lemon()
{
	scanf("%d%d",&n,&m);
	int id=0;
	rep(i,1,m) { id++; which[id]=conv(1,i,1); }
	rep(i,1,n) { id++;  which[id]=conv(i,m,4); }
	repd(i,m,1) { id++; which[id]=conv(n,i,3); }
	repd(i,n,1) { id++;  which[id]=conv(i,1,2); }
	rep(i,1,(n+m)*2) scanf("%d",&d[i]);
	rep(state,0,(1<<(n*m))-1)
	{
		int k=0;
		rep(i,1,n)
			rep(j,1,m)
			{
				k++;
				if (state&(1<<(k-1))) w[i][j]=1; else w[i][j]=0;
			}
		rep(i,1,n*m*4) e[i].clear();
		rep(i,1,n)
			rep(j,1,m)
				if (w[i][j]==1)
				{
					addedge(i,j,1,i,j,4);
					addedge(i,j,2,i,j,3);
				}
				else
				{
					addedge(i,j,1,i,j,2);
					addedge(i,j,3,i,j,4);
				}
		rep(i,1,n-1)
			rep(j,1,m)
				addedge(i,j,3,i+1,j,1);
		rep(i,1,n)
			rep(j,1,m-1)
				addedge(i,j,4,i,j+1,2);
		
		int flag=1;
		rep(i,1,n+m)
		{
			rep(k,1,n*m*4) vis[k]=0;
			goal=which[d[i*2]];
			if (!flood(which[d[i*2-1]])) { flag=0; break; }
		}
		if (flag) 
		{
			rep(i,1,n)
			{
				rep(j,1,m)
					if (w[i][j]==0) printf("/"); else printf("\\");
				printf("\n");
			}
			return;
		}
	}
	printf("IMPOSSIBLE\n");
}

int main()
{
	ios::sync_with_stdio(true);
	#ifndef ONLINE_JUDGE
		freopen("C.in","r",stdin);
	#endif
	int tcase; scanf("%d",&tcase);
	rep(nowcase,1,tcase)
	{
		printf("Case #%d:\n",nowcase);
		lemon();
	}
	return 0;
}

