#include <iostream>
#include <stdlib.h>
using namespace std;

int main(){
	int T; cin >> T;
	double C, F, X;
	for(int t = 1; t <= T; t++){
		cin >> C >> F >> X;
		double p = 0.0;
		double rate = 2.0;
		while(true){
			if( (C / rate + X / (rate + F)) < X / rate){
				double tmp = C / rate;
				p += tmp;
				rate += F;
			}
			else{
				double tmp = X / rate;
				p += tmp;
				break;
			}
		}
		printf("Case #%d: %.7lf\n",t,p);
	}
	return 0;
}
