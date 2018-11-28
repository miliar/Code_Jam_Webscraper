
#include <cstdio>
#include <cstring>
using namespace std;

int T;
double ans;
double C,X,F;

int main() {
	freopen("inL.txt","r",stdin);
	freopen("outL.txt","w",stdout);
	scanf("%d",&T);
	for (int ww=1;ww<=T;ww++) {
		printf("Case #%d: ",ww);
		scanf("%lf%lf%lf",&C,&F,&X);
		ans=X/2.0;
		double now=0;
		double p=2;
		for (;now<=ans;) {
			now+=C/p;
			p+=F;
			if (now+X/p<ans) ans=now+X/p;
		}
		printf("%.10f\n",ans);
	}
	return 0;
}
