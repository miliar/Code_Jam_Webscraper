#include <stdio.h>

int main(){
	int T;
	double C, F, X, ans;
	int k;
	scanf("%d", &T);
	for(int t=1; t<=T; ++t){
		scanf("%lf%lf%lf", &C, &F, &X);
		k = (int)((X/C) - (2.0/F));
		if(k<0) k = 0;
		ans = 0.0;
		for(int i=0; i<k; ++i) ans += C/(2.0+i*F);
		ans += X/(2.0+k*F);
		printf("Case #%d: %.7lf\n", t, ans);
	}
	return 0;
}

