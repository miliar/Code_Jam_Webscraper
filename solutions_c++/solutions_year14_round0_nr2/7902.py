/* Solution to CodeJam Problem B
@file PB-CookieClickerAlpha.c++
@author Kaleb Goering
@date April 11, 2014 */

#include <iostream>
#include <iomanip>

using namespace std;

double solve(double C, double F, double X) {
	double rate = 2;
	double time = 0;
	bool done = false;
	
	while(!done) {
		double finish = X / rate;
		if(finish < ((C / rate) + (X / (rate + F)))) {
			time += finish; 
			done = true;
		} else {
			time += C / rate;
			rate += F;
		}
	}

	return time;
}

int main() {
	int T = 0;
	cin >> T;

	for(int i = 1; i <= T; i++) {
		double C, F, X;
		cin >> C;
		cin >> F; 
		cin >> X;

		if(X < C) {
			cout << "Case #" << i << ": " << fixed << setprecision(7) << (X / 2) << endl;
		} else {
			cout << "Case #" << i << ": " << fixed << setprecision(7) << solve(C, F, X) << endl;
		}
	}

	return 0;
}
