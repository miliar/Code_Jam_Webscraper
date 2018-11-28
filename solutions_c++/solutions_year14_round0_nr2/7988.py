#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
	int t;
	scanf("%d", &t);
	
	for(int kase=1; kase<=t; kase++) {
		double c, f, x, F, time, prod;
		
		scanf("%lf %lf %lf", &c, &f, &x);
		
		int n = 0;
		time = x/2;
		
		while(1) {
			prod = (c-x)/(2 + n*f) + x/(2 + (n+1)*f);
			if(prod >= 0)
				break;
			else {
				time += prod;
				n++;
			}
		}
		
		printf("Case #%d: %.7lf\n", kase, time);
	}
	
	return 0;
}