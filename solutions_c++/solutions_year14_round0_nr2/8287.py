#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<algorithm>

using namespace std;

int main(){
	double c, f, x, r;
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++){
		scanf("%lf %lf %lf", &c, &f, &x);
		r = 2.0;
		double calc = x/r;
		double time = 0.0;
		double result; 
		int n = 0;
		do{	
			result = calc;
			time += (c/(r + f*n));
			n++;
			calc = time + (x/(r + f*n));
		}while(calc <= result);
		printf("Case #%d: %.7f\n", i, result);
	}
	return 0;
}
