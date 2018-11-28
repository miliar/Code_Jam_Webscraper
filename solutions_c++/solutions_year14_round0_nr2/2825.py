#include <cstdio>

using namespace std;

double ans;
double tmp,time,k;
double c,f,x;

int main() {
	int tt,t,i;
	scanf("%d",&t);
	for (tt=1;tt<=t;tt++) {
		scanf("%lf%lf%lf",&c,&f,&x);
		time=0;k=2;ans=tmp=x/k;
		i=0;
		while (1) {
			i++;
			time+=c/k;
			k+=f;
			tmp=time+x/k;
			//printf("%lf %lf\n",time,tmp);
			if (tmp<ans) ans=tmp;
			else break;
		}
		printf("Case #%d: %.7lf\n",tt,ans);
	}
	return 0;
}
