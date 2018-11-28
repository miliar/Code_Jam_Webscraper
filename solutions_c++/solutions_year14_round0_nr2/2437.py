#include <stdio.h>



int main(){
	double C, F, X;
	int i, j, k;
	int cas;
	
	freopen("input.txt","r",stdin);
	freopen("output.txt","w", stdout);
	
	scanf("%d", &cas);


	for (k=1; k<=cas; k++){
		scanf("%lf %lf %lf", &C, &F, &X);

		int cnt=1;
		double pp = 2;
		double min = X/2;
		int i = 1;
		double tt = 0;

		while(1){
			tt = tt + C/pp;
			pp = pp + F;
			if (min > tt+X/pp){
				min = tt + X/pp;
			}else{
				break;
			}
		}
		printf("Case #%d: %.7lf\n", k, min);
	}

	return 0;
}