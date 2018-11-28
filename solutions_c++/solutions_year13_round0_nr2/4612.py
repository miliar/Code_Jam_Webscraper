#include <cstdio>
#include <algorithm>
#define REP(i,n) for (int i=1;i<=n;++i)
using namespace std;

const int INF=999999999;
int T,n,m,a[110][110];
bool flag;

int main(){
	freopen("B-large.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&T);
	REP(T_T,T) {
		scanf("%d%d",&n,&m);
		REP(i,n) REP(j,m) scanf("%d",&a[i][j]);
		flag=false;
		REP(i,n) REP(j,m) {
			int tmp1=-INF,tmp2=-INF;
			REP(k,m) tmp1=max(tmp1,a[i][k]);
			REP(k,n) tmp2=max(tmp2,a[k][j]);
			if((a[i][j]!=tmp1)&&(a[i][j]!=tmp2)) flag=true;
		}
		printf("Case #%d: ",T_T);
		puts(flag?"NO":"YES");
	}
	return 0;
}

