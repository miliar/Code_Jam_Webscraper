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

#define maxn 1000010

struct atype
{
	int s,parent,which;
};

atype a[maxn];
vector<int> e[maxn];

int cmp(const atype &a, const atype &b)
{
	if (a.s!=b.s) return a.s<b.s;
	if (a.parent!=b.parent) return a.parent<b.parent;
	return a.which<b.which;
}

int p[maxn], sz[maxn];

int find(int x)
{
	if (p[x]==x) return x;
	p[x]=find(p[x]);
	return p[x];
}

void merge(int x, int y)
{
	x=find(x); y=find(y);
	if (x==y) return;
	sz[y]+=sz[x]; p[x]=y;
}

int removed[maxn], alive[maxn], parent[maxn];
int wc;

void dfs(int cur, int val)
{
	if (removed[cur]) return;
	if (alive[cur]) wc+=val; 
	removed[cur]=1; alive[cur]=0;
	rept(it,e[cur]) dfs(*it,val*alive[*it]);
}

void insert(int which)
{
	if (removed[which]) return;
	alive[which]=1;
	merge(which,parent[which]);
}

void remove(int which)
{
	if (removed[which]) return;
	wc=0;
	dfs(which,alive[which]);
	sz[find(which)]-=wc;
}

void lemon()
{
	int n, dmax; scanf("%d%d",&n,&dmax);
	int va,vc,vr;
	scanf("%d%d%d%d",&a[1].s,&va,&vc,&vr);
	rep(i,2,n) a[i].s=(LL(a[i-1].s)*va+vc)%vr;
	scanf("%d%d%d%d",&a[1].parent,&va,&vc,&vr);
	rep(i,2,n) a[i].parent=(LL(a[i-1].parent)*va+vc)%vr;
	a[1].parent=0; rep(i,2,n) a[i].parent=a[i].parent%(i-1)+1;
	rep(i,1,n) parent[i]=a[i].parent;
	rep(i,1,n) a[i].which=i;
	rep(i,1,n) e[i].clear();
	rep(i,2,n) e[a[i].parent].push_back(i);
	rep(i,0,n) p[i]=i, sz[i]=1; sz[0]=0;
	memset(alive,0,sizeof alive);
	memset(removed,0,sizeof removed);
	
	sort(a+1,a+n+1,cmp);
	//[head, tail) is the interval
	int tail=1, final=0;
	rep(head,1,n)
	{
		if (head>1) remove(a[head-1].which);
		while (tail<=n && a[tail].s-a[head].s<=dmax) 
		{
			insert(a[tail].which); tail++;
		}
		final=max(final,sz[0]);
	}
	printf("%d\n",final);
}

int main()
{
	ios::sync_with_stdio(true);
	#ifndef ONLINE_JUDGE
		freopen("A.in","r",stdin);
	#endif
	int tcase; scanf("%d",&tcase);
	rep(nowcase,1,tcase)
	{
		printf("Case #%d: ",nowcase);
		lemon();
	}
	return 0;
}

