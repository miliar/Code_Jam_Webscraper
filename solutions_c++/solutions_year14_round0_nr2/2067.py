#include <iostream>
#include <iomanip>
#include <cstdio>
using namespace std;

const double eps = 1e-10;

double solve(double C, double F, double X) {
	double min_time = X / 2.0;
	double f_time = C / 2.0; // time used to build first farm
	for (int f = 1; ; f++) {
		double rate = 2.0 + F * f; 
		double total_time = f_time + X / rate;
		//cout << f << " " << total_time << endl;
		if (total_time > min_time) {
			break;
		} else {
			min_time = total_time;
		}
		f_time += C / (2.0 + F * f); // time used to build next farm 
	}
	return min_time;
}

int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		double C, F, X;
		cin >> C >> F >> X;
		double ans = solve(C, F, X);
		cout << "Case #" << (i + 1) << ": ";
		cout << fixed;
		cout << setprecision(7) << ans << "\n"; 
	}
	return 0;
}
