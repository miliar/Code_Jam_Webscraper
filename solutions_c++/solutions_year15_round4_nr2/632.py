#include <cstdio>
#include <utility>
#include <cmath>
#include <algorithm>
#define LD long double
#define DOW(i,n) for (int i=n;i>=1;--i)
#define REP(i,n) for (int i=1;i<=n;++i)
using namespace std;

const LD EPS=0.00000001;
int T,n;
double A,B;
LD ans;
LD a[110];
LD b[110];
pair<double,double> tmp[110];

void Test(LD a1,LD b1,LD a2,LD b2) {
	if (a1>a2) {swap(a1,a2);swap(b1,b2);}
	if (a1-EPS<A && a2+EPS>A) {
		if (abs(a2*b1-b2*a1)<EPS) return;
		LD x1=(A*b1-B*a1)/(a2*b1-b2*a1);
		LD x2=(A*b2-B*a2)/(a1*b2-b1*a2);
		ans=min(ans,x1+x2);
	}
}

int main() {
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&T);
	REP(T_T,T) {
		printf("Case #%d: ",T_T);
		scanf("%d%lf%lf",&n,&A,&B);
		REP(i,n) {
			scanf("%lf%lf",&tmp[i].second,&tmp[i].first);
		}
		sort(tmp+1,tmp+n+1);
		REP(i,n) {
			a[i]=tmp[i].second;
			b[i]=tmp[i].first*tmp[i].second;
		}
		if (B>tmp[n].first+EPS || B<tmp[1].first-EPS) {
			puts("IMPOSSIBLE");
			continue;
		}
		ans=199999999999999.0;
		REP(i,n) a[i]+=a[i-1];
		REP(i,n) b[i]+=b[i-1];
		for (int i=0;i<=n;++i) Test(a[i],b[i],a[n],b[n]);
		for (int i=0;i<=n;++i) Test(a[n]-a[i],b[n]-b[i],a[n],b[n]);
		printf("%.20lf\n",(double)ans);
	}
	return 0;
}