#include<cstdio>
#include<algorithm>
#include<cstring>
#include<vector>
#include<queue>
#include<map>
#include<set>
using namespace std;
#define INF (1<<29)
#define min(x,y) (((x)<(y))?(x):(y))
#define max(x,y) (((x)>(y))?(x):(y))
#define FOR(i,x,y) for(int i=(x);i<(y);++i)
#define FOE(i,x,y) for(int i=(x);i<=(y);++i)
#define CLR(i) memset(i,0,sizeof(i))

int T,n,m,a[200][200],ans[200][200];
int col[200],row[200];

int main(){
	scanf("%d",&T);
	FOE(t,1,T){
		FOR(i,0,100){
			FOR(j,0,100) ans[i][j]=100;
			col[i]=row[i]=0;
		}

		scanf("%d%d",&n,&m);
		FOR(i,0,n){
			FOR(j,0,m){
				scanf("%d",&a[i][j]);
				row[i] = max(row[i], a[i][j]);
				col[j] = max(col[j], a[i][j]);
			}
		}

		FOR(i,0,n){
			FOR(j,0,m){
				if (ans[i][j] > row[i]) ans[i][j] = row[i];
				if (ans[i][j] > col[j]) ans[i][j] = col[j];
			}
		}

		bool diff = 0;
		FOR(i,0,n){
			FOR(j,0,m) if (a[i][j] != ans[i][j]) diff = 1;
		}
		printf("Case #%d: %s\n", t, diff?"NO":"YES");
	}
	return 0;
}
