#include<cstdio>
#include<iostream>

double cook(double C, double F, double X){
	double ret = X/2;
	double cost = 0;
	double ans = X/2;
	int tr = 0;
	while(ret >= ans){
		ret = ans;
		cost += C/(tr*F+2);
		tr++;
		ans = cost + X/(tr*F+2); 
	}
	return ret;
}

int main(){
//	freopen("b.in","r", stdin);
//	freopen("b.out","w", stdout);
	int T;
	scanf("%d", &T);
	double C, F, X;
	for(int i = 1;i <= T;i++){
		scanf("%lf %lf %lf", &C, &F, &X);
		printf("Case #%d: %.7f\n", i, cook(C, F, X));
	}
	return 0;
} 
