#include<iostream>
#include<stdio.h>
using namespace std;

int T;
double C,F,X;
int critical;

double func(int n){
	if(n == 0){
		return(X/2);
	}
	else{
		double mid = (C-X)/((1.0*n - 1.0)*F + 2) + X/(1.0*n*F + 2.0);
		return (func(n-1) + mid);
	}
}
int main(){
	freopen("B-small-attempt (2).in","r",stdin);
	freopen("B-small-attempt (2).out","w",stdout);

	scanf(" %d",&T);
	for(int i = 0;i < T;i ++){
		double cost1 = 0.0,cost2 = 0.0;
		scanf(" %lf%lf%lf",&C,&F,&X);
		if(C >= X){
			cost1 = X/2;
			cost2 = X/2 + 2.0;
		}
		else{
			critical = (int)(X*F -2*C)/(C*F); // …Ë÷√¡ŸΩÁµ„
			if (critical == 0){
				cost1 = X/2;
				cost2 = X/2 + 2.0;
			}
			else {
				cost1 = func(critical-1);
				int m = critical;
				cost2 = cost1 + (C-X)/((1.0*m - 1.0)*F + 2) + X/(1.0*m*F + 2.0);
			}
		}
		if(cost1 < cost2)
			printf("Case #%d: %f\n",i+1,cost1);
		else
			printf("Case #%d: %f\n",i+1,cost2);
	}
	return 0;
}