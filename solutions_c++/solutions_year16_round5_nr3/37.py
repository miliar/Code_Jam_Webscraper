#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef pair<int,int> PII;
#define MP make_pair
#define PB push_back
#define AA first
#define BB second
#define OP begin()
#define ED end()
#define SZ size()
#define cmin(x,y) x=min(x,y)
#define cmax(x,y) x=max(x,y)
const LL MOD = 1000000007;
const double PI = acos(-1.);
const double eps = 1e-9;
const int MXN = 1005;
int fa[MXN];
int getfa(int u){
	return fa[u]==u?u:fa[u]=getfa(fa[u]);
}
int n,leap;
int x[MXN],y[MXN],z[MXN];
int dx[MXN],dy[MXN],dz[MXN];
double cal(int p,int q,int t){
	LL fx=x[p]-x[q]+t*(dx[p]-dx[q]);
	LL fy=y[p]-y[q]+t*(dy[p]-dy[q]);
	LL fz=z[p]-z[q]+t*(dz[p]-dz[q]);
	return sqrt(fx*fx+fy*fy+fz*fz);
}
void solvesmall(){
	int i,j,k;
	scanf("%d%d",&n,&leap);
	for(i=1;i<=n;i++)
		scanf("%d%d%d%d%d%d",&x[i],&y[i],&z[i],&dx[i],&dy[i],&dz[i]);
	vector<pair<double,PII> >L;
	for(i=1;i<=n;i++)
		for(j=i+1;j<=n;j++)
			L.PB(MP(cal(i,j,0),MP(i,j)));
	sort(L.OP,L.ED);
	for(i=1;i<=n;i++)fa[i]=i;
	for(i=0;i<L.SZ;i++){
		int u=L[i].BB.AA,v=L[i].BB.BB;
		int fu=getfa(u),fv=getfa(v);
		fa[fu]=fv;
		int f1=getfa(1),f2=getfa(2);
		if(f1==f2){
			printf("%.16f\n",L[i].AA);
			return;
		}
	}
}
int main(){
	int i,j,k,_T;
	scanf("%d",&_T);
	for(int CA=1;CA<=_T;CA++){
		printf("Case #%d: ",CA);
		solvesmall();
	}
	return 0;
}