#include <iostream>
#include <vector>
#include <float.h>

using namespace std;
double C,F,X;

double abs(double x){
	if(x < 0)
		return -x;
	return x;
}

bool nearlyEqual(double a, double b, double epsilon) {
	double absA = abs(a);
	double absB = abs(b);
	double diff = abs(a - b);

	if (a == b) { // shortcut, handles infinities
		return true;
	} else if (a == 0 || b == 0 || diff < DBL_MIN) {
		// a or b is zero or both are extremely close to it
		// relative error is less meaningful here
		return diff < (epsilon * DBL_MIN);
	} else { // use relative error
		return diff / (absA + absB) < DBL_EPSILON;
	}
}

double calculate_min_time(){
	double t = 0.0, lastT;
	vector<double> times;
	double cps = 2.0;
	t = lastT = X / cps;
	while(nearlyEqual(t, lastT, 0.0000001) || t < lastT){
		lastT = t;
		t = C / cps;
		times.push_back(t);
		cps += F;
		t = X / cps;
		for(vector<double>::iterator it = times.begin(); it != times.end(); ++it){
			t += *it;
		}
	}
	times.clear();
	return lastT; 
}

int main(){
	int T, i;
	double time;
	cin >> T;
	cout.precision(7);
	for(i = 1;i <= T; ++i){
		cin >> C;
		cin >> F;
		cin >> X;
		time = calculate_min_time();
		cout << "Case #" << i << ": " << fixed << time << endl;
	}
	return 0;
}

