#include <cstdio>
#include <cstring>
#define MAX(a,b) ((a)>(b)?(a):(b))
char lawn[110][110];
int rmax[110],cmax[110];

int main(){
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;++t){
		int N,M;
		int res=1;
		int a,b;
		scanf("%d%d",&N,&M);
		memset(rmax,0,sizeof(rmax));
		memset(cmax,0,sizeof(cmax));
		memset(lawn,0,sizeof(lawn));
		for(int i=1;i<=N;++i){
			for(int j=1;j<=M;++j){
				scanf("%d",&lawn[i][j]);
			}
		}
		for(int i=1;i<=N;++i){
			for(int j=1;j<=M;++j){
				rmax[i]=MAX(rmax[i],lawn[i][j]);
				cmax[j]=MAX(cmax[j],lawn[i][j]);
			}
		}
		for(int i=1;i<=N;++i){
			for(int j=1;j<=M;++j){
				if(rmax[i]>lawn[i][j]&&cmax[j]>lawn[i][j]){
					res=0;
					goto result;
				}
			}
		}
result:
		printf("Case #%d: %s\n",t,res?"YES":"NO");
	}
	return 0;
}