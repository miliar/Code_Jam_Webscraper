#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
#define rep(i,n) for (int i=1;i<=n;++i)
typedef long long LL;
const int inf=1<<28,N=505;
int T,Case,n,x,l,ans,a[N],son[N],ed[N],next[N]; bool b[N];
bool dfs(int x,int fa,int y)
{
	//printf("dfs x=%d fa=%d y=%d\n",x,fa,y);
	if (b[x]) return 0; if (x==y) return 1;
	for (int p=son[x];p;p=next[p]) if (ed[p]!=fa && dfs(ed[p],x,y)) return 1;
	return 0;
}
int cal(int x,int fa,int d,int block)
{
	if (b[x] || x==block) return 0; d+=a[x]; int res=d;
	for (int p=son[x];p;p=next[p]) if (ed[p]!=fa) res=max(res,cal(ed[p],x,d,block));
	return res;
}
int work(int x,int y)
{
	b[x]=1; int res=-inf,z=-1;
	for (int p=son[x];p;p=next[p]) if (dfs(ed[p],x,y)) z=ed[p];
	if (z>=0) res=a[x]-work(y,z); if (x==y) res=a[x];
	//printf("%d %d %d  %d\n",x,y,z,res);
	//rep(i,n) printf("%d ",b[i]); puts("b");
	b[x]=0; int v=a[x]; a[x]=0;
	for (int p=son[x];p;p=next[p]) if (ed[p]!=z && !b[ed[p]])
		res=max(res,v+cal(ed[p],x,0,x)-cal(y,0,0,ed[p]));
		//printf("! %d %d\n",ed[p],v+cal(ed[p],x,0,x)-cal(y,0,0,ed[p]));
	a[x]=v;
	//printf("%d %d %d  %d\n",x,y,z,res);
	return res;
}
int main()
{
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	scanf("%d",&T);
	while (T--){
		scanf("%d",&n),l=1,ans=-inf; rep(i,n) scanf("%d",a+i),son[i]=0;
		rep(i,n-1) scanf("%d",&x),
			ed[++l]=i,next[l]=son[x],son[x]=l,
			ed[++l]=x,next[l]=son[i],son[i]=l;
		rep(i,n){
			int res=inf;
			rep(j,n) memset(b,0,sizeof(b)),res=min(res,work(i,j));
			ans=max(ans,res);
		}
		printf("Case #%d: %d\n",++Case,ans);
	}
	return 0;
}

