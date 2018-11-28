// Cookie Clicker Alpha in Google CodeJam 2014
#include <iostream>
#include <iomanip> 
#include <cmath>
using namespace std;

double C, F, X;

double dowork() {
	
	cin >> C >> F >> X;
	double production_rate = 2.0f;
	double time_by_produce = X / production_rate;
	double time_by_addfarm = (C / production_rate) + (X / (production_rate + F));
	
	if (time_by_produce < time_by_addfarm) {
		return time_by_produce;
	} else {
		production_rate += F;
	}
	while(true) {
		time_by_produce = time_by_addfarm;
		time_by_addfarm = time_by_addfarm - (X / (production_rate)) + (C / production_rate) + (X / (production_rate + F));
		if (time_by_produce < time_by_addfarm) {
			return time_by_produce;
		} else {
			production_rate += F;
		}
	}
}

int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		double result = dowork();
		cout << "Case #" << (i+1) << ": " << fixed << showpoint << setprecision (7) << result << endl;
	}
}