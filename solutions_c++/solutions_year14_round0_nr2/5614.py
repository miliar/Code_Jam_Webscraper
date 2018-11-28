#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>

using namespace std;
double EPS  = 1e-9;

int main(void){
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int T;
	double C, F, X;
	cin >> T;
	for(int t = 1; t <= T; t++){
		cin >> C >> F >> X;

		double currentF = 2.0;
		double ans = 0.0;
		while(1){
			double t1 = X / currentF;
			double t2 = (C / currentF) + (X / (currentF+F));
			if(t2 >= t1 - EPS){
				ans += t1;
				break;
			}
			ans += (C / currentF);
			currentF += F;
		}
		//cout.precision(7);
		//cout<<"Case #"<<t<<": "<<ans<<endl;
		printf("Case #%d: %0.7f\n", t, ans);
	}
	return 0;
}