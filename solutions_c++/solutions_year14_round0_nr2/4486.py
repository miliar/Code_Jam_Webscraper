#include <iostream>
#include <cstdio>
using namespace std;
double EPSILON = 10e-9;
int main(){
	int T; cin >> T;
	for (int test = 1; test <= T; test++){
		double ans = 0; double C, F, X; 
		cin >> C >> F >> X;
		//printf("%0.5f %0.5f %0.5f", C, F, X);
		double rate = 2;
		double dont = X / rate;// cost to wait ; watch out for doubles
		double buy = C / rate + (X / (F+rate)); // cost to wait for farm and then cost to buy
		//ans = 0;
		while (1){
			if ((dont - buy) > EPSILON){ // time for buying is less than not buying
				rate += F;
				// next buy
				dont = buy;
				buy += C / rate + (X / (F+rate)) - (X / (rate));

			} else {
				ans = dont;
				break;
			};
		}

		printf("Case #%d: %0.7f\n", test, ans);
	}


	return 0;
}