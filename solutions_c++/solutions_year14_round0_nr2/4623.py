#include<iostream>
#include<stdio.h>
using namespace std;

int main(){
	int t;
	cin>>t;
	int test = 1;
	while(t--){
		 double cost,extra,goal;
		scanf("%lf %lf %lf",&cost, &extra, & goal);

		double rate = 2.0;	
		double t = goal/rate;
		
		while(true){
		
			double gain = (goal)/(rate);
			gain = gain - (goal)/(rate+extra);
			gain = gain - (cost/rate);
			if( gain > 0 - 1e-8){
				t = t - gain;
				rate = rate + extra;
			}
			else{
				break;
			}

		};
		printf("Case #%d: %.7lf\n",test,t);
		test++;
	}	
}

