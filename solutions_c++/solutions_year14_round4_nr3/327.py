#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
#define rep(i,n) for (int i=0;i<n;++i)
typedef long long LL;
const int N=2005,u[4]={1,0,-1,0},v[4]={0,1,0,-1};
int Test,Case,n,m,B,G,S,T,l,ans,xl,xr,yl,yr;
int ed[N*N],data[N*N],next[N*N],son[N*N],d[N*N],f[N*N]; bool b[N][N];
void add(int x,int y,int z)
{
	ed[++l]=y,data[l]=z,next[l]=son[x],son[x]=l;
	ed[++l]=x,data[l]=0,next[l]=son[y],son[y]=l;
}
bool build()
{
	int h=0,t=1; rep(i,T+1) d[i]=-1; d[f[1]=S]=0;
	while (h<t){
		int x=f[++h];
		for (int p=son[x];p;p=next[p]) if (data[p]){
			int y=ed[p];
			if (d[y]<0) d[y]=d[x]+1,f[++t]=y;
			if (y==T) return 1;
		}
	}
	return 0;
}
int dinic(int x,int low)
{
	if (x==T) return low; int res,w=0;
	for (int y,p=son[x];p && w<low;p=next[p]) if (data[p] && d[y=ed[p]]==d[x]+1)
		if (res=dinic(y,min(low-w,data[p]))) data[p]-=res,data[p^1]+=res,w+=res;
	if (!w) d[x]=-1; return w;
}
int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	scanf("%d",&Test);
	while (Test--){
		scanf("%d%d%d",&n,&m,&B),G=n*m,S=G+G,T=S+1,l=1,ans=0;
		memset(b,0,sizeof(b)),memset(son,0,sizeof(son));
		rep(k,B){
			scanf("%d%d%d%d",&xl,&yl,&xr,&yr);
			for (int i=xl;i<=xr;++i) for (int j=yl;j<=yr;++j) b[i][j]=1;
		}
		//rep(i,n){rep(j,L) printf("%d ",b[i][j]); puts("b");}
		rep(i,n) add(S,i*m,1),add(i*m+m-1,T,1);
		rep(i,n) rep(j,m) if (!b[i][j]){
			add(i*m+j,G+i*m+j,1);
			rep(k,4){
				int x=i+u[k],y=j+v[k];
				if (x>=0 && x<n && y>=0 && y<m && !b[x][y])
					add(G+i*m+j,x*m+y,1);
			}
		}
		while (build()) ans+=dinic(S,n+1);
		printf("Case #%d: %d\n",++Case,ans);
	}
	return 0;
}

