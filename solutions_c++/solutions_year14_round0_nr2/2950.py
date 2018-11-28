#include <stdio.h>

int main(){
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;++t){
		double C,F,X;
		scanf("%lf %lf %lf",&C,&F,&X);
		double ans = 1e10;
		double ft = 0;
		double speed = 2.0;
		while( ft<ans ){
			//printf("ft = %f\n", ft);
			if( ft + X/speed < ans )
				ans = ft + X/speed;
			ft += C / speed;
			speed += F;
		}
		printf("Case #%d: %.7f\n", t, ans);
	}
	return 0;	
}
