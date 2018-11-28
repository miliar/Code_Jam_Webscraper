#include <iostream>
#include <cstdio>
int main(){
	double c, f, x;
	int T;
	scanf("%d", &T);
	for(int tt=1; tt<=T; tt++){
		scanf("%lf%lf%lf", &c, &f, &x);
		double t=0, tnow=x/2, r=2;
		do{
			double tnew=c/r+t+x/(f+r);
			if(tnew<tnow){
				tnow=tnew;
				t+=c/r;
				r+=f;
			} else break;
		}while(1);
		printf("Case #%d: %.8lf\n", tt, tnow);
	}
}
