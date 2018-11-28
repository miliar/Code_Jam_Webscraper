#include<stdio.h>
int main() {
	int t,T;
	double c,f,x,nowc,nowt,nowr;
	scanf("%d",&T);
	for(t=1;t<=T;t++) {
		scanf("%lf%lf%lf",&c,&f,&x);
		nowc=nowt=0;
		nowr=2;
		while(1) {
			if(x-nowc<=c) {
				nowt=(x-nowc)/nowr;
				break;
			}
			if((x-nowc)/nowr<=(x-nowc)/(nowr+f)+c/nowr) {
				nowt+=(x-nowc)/nowr;
				break;
			}
			else {
				nowt+=c/nowr;
				nowr+=f;
			}
		}
		printf("Case #%d: %.7lf\n",t,nowt);
	}
	return 0;
}
