#include <cstdio>
#include <cstring>
#include <algorithm>
#define fr(i,a,b) for(int i=a;i<b;i++)
#define rep(i,b) fr(i,0,b)
using namespace std;

int g[120][120];
bool mk[120][120];

int main(){
	int cas;
	scanf("%d",&cas);
	rep(u,cas){
		int n, m;
		scanf("%d %d",&n,&m);
		int qtd=0;
		rep(i,n) rep(j,m) scanf("%d",&g[i][j]), mk[i][j] = false;
		rep(i,n){
			int mm = -1;
			rep(j,m) mm = max(mm,g[i][j]);
			rep(j,m) if(g[i][j] == mm && !mk[i][j]) mk[i][j] = true, qtd++;
		}
		rep(i,m){
			int mm = -1;
			rep(j,n) mm = max(mm,g[j][i]);
			rep(j,n) if(g[j][i] == mm && !mk[j][i]) mk[j][i] = true, qtd++;
		}
		
		printf("Case #%d: ",u+1);
		if(qtd==n*m) printf("YES");
		else printf("NO");
		printf("\n");
	}
	return 0;
}

