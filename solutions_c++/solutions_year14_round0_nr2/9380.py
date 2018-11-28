#include <cstdio>
#include <cstdlib>
#include <string>
#include <algorithm>

using namespace std;

double findTime(double X, double C, double cps, double F);

int main(){
	int n;
	scanf( "%d", &n);
	double C, F, X;
	double cps = 2;
	for(int i = 0; i < n; i++){
		scanf("%lf %lf %lf", &C, &F, &X);
		printf("Case #%d: %0.7f\n", i+1, findTime(X,C,cps,F));
	}
	
	return 0;
}

double findTime(double X, double C, double cps, double F){
	if( C/cps + X/(cps + F) > X/cps){
		return X/cps;
	}
	double time = C/cps;
	return time + findTime(X, C, cps+F, F);
}