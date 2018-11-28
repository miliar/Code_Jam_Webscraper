#include <cstdio>

using namespace std;

int T;
double A,S,C,F,X,time;

int main(){
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%d",&T);
	for (int t=1;t<=T;++t){
		scanf("%lf%lf%lf",&C,&F,&X);
		A=time=0,S=2;
		while (A<X-1e-6){
			double t1=(X-A)/S,t2=(C-A)/S+X/(S+F);
			if (t1<t2) A=X,time+=t1;else A=0,time+=(C-A)/S,S+=F;
		}
		printf("Case #%d: %0.7lf\n",t,time);
	}
	return 0;
}
