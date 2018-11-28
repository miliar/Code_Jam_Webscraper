#include<stdio.h>

int main(){
	int T;
	int cnt = 0;
	scanf("%d", &T);
	while(T--){
		double C, F, X, S, T ;
		S = 2.0, T = 0.0;
		scanf("%lf %lf %lf", &C, &F, &X);
		if(C > X){
			printf("Case #%d: %lf\n", ++cnt, X/S);
			continue;
		}
		while(1){
	//		printf("%lf %lf\n", T, S);
			if((X-C)/S < X/(S+F)){
				T += X/S;
				break;
			}else{
				T += C/S;
				S += F;
			}
		}
		printf("Case #%d: %.7lf\n", ++cnt, T);
	}

	return 0;
}
