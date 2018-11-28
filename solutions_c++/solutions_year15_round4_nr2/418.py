#include <stdio.h>
#include <algorithm>

int main(){
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;++t){
		int n;
		double v, c;
		scanf("%d %lf %lf",&n, &v, &c);
		double r[2], x[2];
		for(int i=0;i<n;++i){
			scanf("%lf %lf", r+i, x+i);
		}
		printf("Case #%d: ", t);
		if( n == 1 ){
			if( x[0] != c )
				printf("IMPOSSIBLE\n");
			else
				printf("%.10f\n", v/r[0]);	
		} else {
			if( (x[0] > c && x[1] > c) || (x[0]<c&&x[1]<c) )
				printf("IMPOSSIBLE\n");
			else {
				if( x[0] == c && x[1] == c )
					printf("%.10f\n", v/(r[0]+r[1]));
				else if( x[0] == c && x[1] != c )
					printf("%.10f\n", v/r[0]);
				else if( x[1] == c && x[0] != c )
					printf("%.10f\n", v/r[1]);
				else {
					double tmp = (c-x[1])/(x[0]-c);
					double t1 = v/r[1]/(1+tmp);
					double t0 = tmp*r[1]/r[0]*t1;
					//printf("%f %f\n", t0, t1);
					//printf("%f\n", t0*r[0] + t1*r[1]);
					//printf("%f\n", (t0*r[0]*x[0] + t1*r[1]*x[1])/(t0*r[0] + t1*r[1]));
					printf("%.10f\n", std::max(t0, t1));
				}
			}	
		}
	}
	return 0;	
}
