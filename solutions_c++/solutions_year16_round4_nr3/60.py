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
int fa[333];
int getfa(int u){
	return fa[u]==u?u:fa[u]=getfa(fa[u]);
}
void merfa(int u,int v){
	int fu=getfa(u),fv=getfa(v);
	fa[fu]=fv;
}
int id[105][105][4];
int wt[405];
int pr[405];
int res[105][105];
void solve(){
	int i,j,k;
	int R,C;
	scanf("%d%d",&R,&C);
	for(i=1;i<=2*(R+C);i++)
		scanf("%d",&wt[i]);
	for(i=1;i<=2*(R+C);i+=2)
		pr[wt[i]]=wt[i+1],pr[wt[i+1]]=wt[i];
	if(R*C<=16&&true){
		int m=R*C;
		for(int mask=0;mask<1<<m;mask++){
			int n=4*m+2*R+2*C;
			int nid=2*R+2*C;
			for(i=0;i<R;i++)
				for(j=0;j<C;j++)
					for(k=0;k<4;k++)
						id[i][j][k]=nid++;
			for(i=0;i<nid;i++)
				fa[i]=i;
			for(i=0;i<R;i++){
				int lid=2*C+2*R-i -1;
				int rid=C+i+1 -1;
				merfa(lid,id[i][0][1]);
				merfa(rid,id[i][C-1][3]);
				for(j=1;j<C;j++)
					merfa(id[i][j-1][3],id[i][j][1]);
			}
			for(j=0;j<C;j++){
				int uid=j+1 -1;
				int did=2*C+R-j -1;
				merfa(uid,id[0][j][0]);
				merfa(did,id[R-1][j][2]);
				for(i=1;i<R;i++)
					merfa(id[i-1][j][2],id[i][j][0]);
			}
			k=0;
			for(i=0;i<R;i++)
				for(j=0;j<C;j++){
					res[i][j]=mask>>k&1;
					if(res[i][j]){//"/"
						merfa(id[i][j][0],id[i][j][1]);
						merfa(id[i][j][3],id[i][j][2]);
					}else {//"\"
						merfa(id[i][j][0],id[i][j][3]);
						merfa(id[i][j][1],id[i][j][2]);
					}
					k++;
				}
			int fail=0;
			for(i=1;i<=2*(R+C);i++){
				int fu=getfa(i-1),fv=getfa(pr[i]-1);
				if(fu!=fv)fail=1;
			}
			if(!fail){
				for(i=0;i<R;i++){
					for(j=0;j<C;j++){
						printf("%s",res[i][j]?"/":"\\");
					}
					printf("\n");
				}
				return;
			}
		}
		printf("IMPOSSIBLE\n");
		return;
	}
}
int main(){
	int _T;
	scanf("%d",&_T);
	for(int CA=1;CA<=_T;CA++){
		printf("Case #%d:\n",CA);
		solve();
	}
	return 0;
}