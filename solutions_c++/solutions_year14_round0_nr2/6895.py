#include <iostream>
#include <iomanip>

using namespace std;

double answer(double c, double f, double x) {
	double best = x / 2.0;
	double time = 0.0;
	for(int i = 1; i <= x; i ++) {
		time += c / (2.0 + f * (i-1));
		best = min(best, time + x / (2.0 + f*i));
	}
	return best;
}

int main() {
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++) {
		double c,f,x;
		cin >> c >> f >> x;
		cout << "Case #" << i << ": " << setprecision(10) << answer(c, f, x)
			<<endl;
	}
}
