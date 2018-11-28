#include <cstdio>
#define N 101
using namespace std;
int p[N][N],c[N][N];
bool v[N][N];
int main(){
	int t,cas,n,m,i,j,k,tot;
	bool cut;
	scanf("%d",&t);
	for(cas=1;cas<=t;cas++){
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++){
			for(j=0;j<m;j++){
				scanf("%d",&p[i][j]);
				c[i][j]=100;
				v[i][j]=false;
			}
		}
		tot=0;
		for(i=0;i<n;i++){
			k=p[i][0];//((p[i][0]>p[i][m-1])?p[i][0]:p[i][m-1]);
			//cut=true;
			for(j=1;j<m;j++) if(p[i][j]>k) k=p[i][j];//cut=false;
			for(j=0;j<m;j++) if(c[i][j]>k) c[i][j]=k;
		}
		for(j=0;j<m;j++){
			k=p[0][j];//p[0][j]>p[n-1][j]?p[0][j]:p[n-1][j];
			//cut=true;
			for(i=1;i<n;i++) if(p[i][j]>k) k=p[i][j];//cut=false;
			for(i=0;i<n;i++) if(c[i][j]>k) c[i][j]=k;
		}
		cut=true;
		for(i=0;i<n;i++){
			for(j=0;j<m;j++){
				//printf("%d ",c[i][j]);
				if(p[i][j]!=c[i][j]) cut=false;
			}
			//printf("\n");
		}
		printf("Case #%d: %s\n",cas,cut?"YES":"NO");
	}
	return 0;
}
