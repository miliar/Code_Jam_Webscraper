#include <cstdio>
#include <memory.h>
int a[4][4],b[4][4];
int cnt[17];
int main() {
	int T,Ti;
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	scanf("%d",&T);
	for(Ti=1;Ti<=T;Ti++) {
		double c,f,x;
		scanf("%lf%lf%lf",&c,&f,&x);
		double time=0;
		if(c>=x) {
			printf("Case #%d: %.7lf\n",Ti,x/2.0);
		}
		else {
			double rate=2;
			while(1) {
				time+=c/rate;
				if((x-c)/rate>=x/(rate+f)) {
					rate+=f;
				} else {
					time+=(x-c)/rate;
					break;
				}
			}
			printf("Case #%d: %.7lf\n",Ti,time);
		}
	}
	return 0;
}