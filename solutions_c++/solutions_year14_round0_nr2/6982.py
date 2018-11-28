#include <iostream>
#include <stdio.h>
using namespace std;

int main(){
	int T, k=0;
	double C, F, X;
	double ans;
	cin >> T;
	while(k<T){
		cin >> C >> F >> X;
		double v = 2.0, oldv;
		double pretime = 0;
		ans = X/v;
		while(1){
			oldv = v;
			v += F;
			pretime += C/oldv;
			double temp = X/v + pretime;
			if(temp < ans) ans = temp;
			else break;
		}
		k++;
		printf("Case #%d: %.7f\n", k, ans);
	}
	return 0;
}