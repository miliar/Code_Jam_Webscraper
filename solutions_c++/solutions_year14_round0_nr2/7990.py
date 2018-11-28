#include<cstdio>
#include<iostream>
using namespace std;

int main() {
	int ntc;
	scanf("%d ", &ntc);
	double rate = 2.0;
	double time;
	double C = 0, F = 0, X = 0;
	for(int t=1;t<=ntc;t++){
		rate = 2.0;
		scanf("%lf %lf %lf", &C, &F, &X);
		if(C>X){
			time = X/rate;
		}
		else{
			time = C/rate;
			//decision
			while(true)
			{	
				double reqTime1 = (X-C)/rate;
				double reqTime2 = X/(rate+F);
				//printf("time:%lf, reqTime1:%lf, reqTime2:%lf\n", time, reqTime1, reqTime2);
				if(reqTime1 <= reqTime2) {
					//continue with clicking cookies
					time += (X-C)/rate;
					break;
				}
				else{
					//buy farm
					rate = rate + F;
					time += C/rate;
				}
			}
		}
		printf("Case #%d: %.7f\n", t, time);
	}
}