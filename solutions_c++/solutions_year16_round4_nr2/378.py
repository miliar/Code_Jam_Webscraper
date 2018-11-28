#include <cstdio>
#include <cstring>
#include <algorithm>
#define REP(i,n) for (int i=1;i<=n;++i)
using namespace std;

double f[220][220];
double p[220];
double a[220];
double ans;
int T,n,m;

double work(int num) {
		sort(p+1,p+n+1);
		int nn=0;
		for (int i=1;i<=num;++i) a[++nn]=p[i];
		for (int i=1;i<=m-num;++i) a[++nn]=p[n-i+1];
		memset(f,0,sizeof(f));
		f[0][0]=1.0;
		for (int i=0;i<nn;++i)
			for (int j=0;j<=i;++j) {
				f[i+1][j]+=f[i][j]*(1-a[i+1]);
				f[i+1][j+1]+=f[i][j]*a[i+1];
			}
		return f[nn][nn/2];
}

int main() {
	freopen("b.in","r",stdin);
	freopen("b.ans","w",stdout);
	scanf("%d",&T);
	REP(T_T,T) {
		scanf("%d%d",&n,&m);
		REP(i,n) {
			scanf("%lf",&p[i]);
		}
		ans=0;
		for (int i=0;i<=m;++i)
			ans=max(ans,work(i));
		printf("Case #%d: %.9lf\n",T_T,ans);
	}
	return 0;
}