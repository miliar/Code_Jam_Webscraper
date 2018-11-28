#include <iostream>
#include <cstdio>

using namespace std;

int main(){
	int TC;
	double C,F,X;
	double rate,cost;
	cin>>TC;
	for (int T=1;T<=TC;T++){
		cin>>C>>F>>X;
		rate = 2;
		cost=0;
		if (C<X){
			double a = (X-C)/rate;
			double b = X/(rate+F);
			while (a>b){
				cost+=C/rate;
				rate+=F;
				a = (X-C)/rate;
				b = X/(rate+F);
			}
			cost+=X/rate;
		}
		else{
			cost=X/rate;
		}
		printf("Case #%d: %.7f\n",T,cost);
	}
	return 0;
}