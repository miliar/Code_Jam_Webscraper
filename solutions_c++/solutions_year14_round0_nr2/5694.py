#include <cstdio>

using namespace std;


// C - cookies per farm
// F - farm income
// X - target Value

double getMin(double a, double b){
	return (a>b)?b:a;
}
double solve(double income,double score,double C,double F,double X){

	double buildFarm = C / income;
	double getToTarget = X / income;
	if(buildFarm + X/(income+F) >= getToTarget){
		return getToTarget;
	}
	return getMin(solve(income+F,0,C,F,X) + buildFarm, getToTarget);
}

int main(){
	int T;
	scanf("%d",&T);
	for(int i =0 ; i < T; i++){
		double C,F,X;
		scanf("%lf %lf %lf",&C,&F,&X);
		printf("Case #%d: %.7lf\n",(i+1),solve(2,0,C,F,X));
	}
	return 0;
}

