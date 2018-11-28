#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#define rep(i,a,b) for (int i=a;i<=b;i++)
#define drep(i,a,b) for (int i=a;i>=b;i--)
#define INF int(1e8)
#define LL long long
#define D double
#define LD long double
#define pb push_back
#define mp make_pair
#include <cassert>
#define Pi M_PI
using namespace std;
template<class T> inline T min(T &a,T &b) {return a<b?a:b;}
template<class T> inline T max(T &a,T &b) {return a>b?a:b;}
int res[10][10],pre[1000000],nxt[1000000],al,n,m,a[1000000];
char s[100000];
int get(char a)
{
	if (a=='i') return 2;
	if (a=='j') return 3;
	if (a=='k') return 4;
	assert(0);
}
int mul(int x,int y)
{
	int flag=1;
	if (x*y<0) flag=-1;
	return res[abs(x)][abs(y)]*flag;
}
void work(int ti)
{
	res[1][1]=1;
	res[1][2]=2;
	res[1][3]=3;
	res[1][4]=4;
	res[2][1]=2;
	res[2][2]=-1;
	res[2][3]=4;
	res[2][4]=-3;
	res[3][1]=3;
	res[3][2]=-4;
	res[3][3]=-1;
	res[3][4]=2;
	res[4][1]=4;
	res[4][2]=3;
	res[4][3]=-2;
	res[4][4]=-1;
	scanf("%d%d",&n,&m);
	scanf("%s",s+1);
	al=0;
	rep(i,1,min(m,30))
		rep(j,1,n) a[++al]=get(s[j]);
	int p=1;
	rep(i,1,n) p=mul(p,a[i]);
	int k=m-min(m,30),all=1;
	for(;k;k>>=1,p=mul(p,p)) if (k&1) all=mul(all,p);
	pre[1]=a[1];
	rep(i,2,al) pre[i]=mul(pre[i-1],a[i]);
	nxt[al]=a[al];
	drep(i,al-1,1) nxt[i]=mul(a[i],nxt[i+1]);
	int l=-1,r=-1;
	rep(i,1,al) if (pre[i]==2) {l=i;break;}
	drep(i,al,1) if (nxt[i]==4) {r=i;break;}
	if (l==-1 || r==-1) {printf("Case #%d: NO\n",ti);return;}
	int cur=a[l+1];
	rep(i,l+2,r-1) cur=mul(cur,a[i]);
	if (mul(all,cur)!=3) {printf("Case #%d: NO\n",ti);return;}
	if (l+1<r) {printf("Case #%d: YES\n",ti);return;}
	printf("Case #%d: NO\n",ti);
}
int main()
{
	freopen("small.in","r",stdin);
	freopen("me.out","w",stdout);
	int cs,ti=0;
	scanf("%d",&cs);
	while (cs--) work(++ti);
}
