#include <cstdio>
#include <iostream>

using namespace std;


int main(){
	int T;
	scanf("%d ", &T);
	for(int caso=0; caso<T; caso++){
		double R = 2.0;
		double C, F, X;
		scanf("%lf %lf %lf ", &C, &F, &X);
		double time = 0;
		double divisor = R;
		while(true){
			if((X/(divisor+F) + C/(divisor)) < X/divisor){
				time += C/divisor;
				divisor += F;
			}else{
				time += X/divisor;
				break;
			}
		}
		printf("Case #%d: %lf\n", caso+1, time);

		}







}
