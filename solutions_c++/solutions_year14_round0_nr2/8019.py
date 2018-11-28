#include <stdio.h>
#define eps 1e6
int main(){
	freopen("B-large.in","r",stdin);
	freopen("out1.txt","w",stdout);
	int T;
	double c,f,x;
	int aa=0;
	scanf("%d",&T);
	while(T--){
		scanf("%lf %lf %lf",&c,&f,&x);
		double min=x/2;
		double t=0;
		double cl,fl=2,xl;
		for(int i=1;i<=100000;++i){
			double zzz=x/(fl+f);
			t=t+c/fl+zzz;
			//printf("%lf\n",t);
			if(min>t) min=t;
			t-=(zzz);
			fl+=f;
		}
		printf("Case #%d: %.6lf\n",++aa,min);
	}
	return 0;
}
