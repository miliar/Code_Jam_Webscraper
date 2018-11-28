#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
	int testCases;

	cin>>testCases;
	for(int i=0;i<testCases;i++){
		double C;
		double F;
		double X;
		double rate=2;
		double totalCookies=0;
		double time=0;
		cin>>C>>F>>X;
		cin.get();

		if(X<=C){
			printf("Case #%d: %lf\n",i+1,X/rate);
			continue;
		}

		while(X/rate>(C/rate+X/(rate+F))){
			time+=C/rate;
			rate+=F;
		}
		time+=X/rate;
		printf("Case #%d: %lf\n",i+1,time);
	}
}
