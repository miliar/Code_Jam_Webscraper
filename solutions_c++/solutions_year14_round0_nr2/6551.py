#include<stdio.h>

int main(){
	int i,j,t,cases=0;
	double C,x,X,F;
	scanf("%d",&t);
	while(cases++<t){
		double sum=0.0,x=2.0;
		int i=0;
		scanf("%lf %lf %lf",&C,&F,&X);
		while((X/(x+F))<((X-C)/x)){
			//printf("X/(x+F)=%.7lf\t(X-C)/x=%.7lf\n",X/(x+F),(X-C)/x);
			sum+=(C/x);
			x+=F;
			//printf("Loop #%d:Sum=%.7lf\t x=%.7lf\n",i++,sum,x);
		}
		sum+=(X/x);
	printf("Case #%d: %.7lf\n",cases,sum);
	}
return 0;
}
