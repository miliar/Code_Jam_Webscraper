#include <iostream>
#include <stdio.h>
#include <string.h>
#include <math.h>

using namespace std;

int main() {
	int t;
	cin>>t;
	double c,f,x;
	for(int i=1;i<=t;i++) {
		c = f = x = 0.00;
		int j=0;
		double min=1e19;
		double inc=0.00;
		scanf("%lf%lf%lf",&c,&f,&x);
		while(1) {
			double temp=0.0000;
			temp = x/(2+f*j);
			temp += inc;
			if(inc > min) {
				break;
			}
			if(temp < min) {
				min = temp;
			}
			inc += c/(2+f*j);
			j++;
		}
		printf("Case #%d: %.7lf\n",i,min);
	}
	return 0;
}
