#include <iostream>
#include <iomanip>
#include <cstdio>
using namespace std;

// c = costo en cookes de una granja
// f = cantidad de cookies generadas por granja por segundo
// x = a que cantidad de cookies quiero llegar

double c,x,f;

double cookie(double times, double rate){
	double var1 = x/rate;
//	cout<<times<<endl;
	while( var1 > (x/(rate+f))+c/rate ){
		
		times+=(c/rate);
		rate+=f;
		var1 = x/rate;
	}
	return var1 + times;
}

int main(int argc, char *argv[]) {
	int n;
	scanf("%d",&n);

	for(int i = 1; i <= n; i++){
		scanf("%lf",&c);
		scanf("%lf",&f);
		scanf("%lf",&x);
		printf("Case #%d: %.7f\n",i,cookie(0.0,2.0));
	} 
	return 0;
}

