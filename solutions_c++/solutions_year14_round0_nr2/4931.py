#include <iostream>
#include <iomanip>
using namespace std;

double process(const double C, const double F, const double X, double r, double y) {
	double nomoreC = X/r, contC = C/r + X/(r+F);
	return ((nomoreC > contC) ? process(C, F, X, r+F, y+C/r) : (y+nomoreC));
}

int main() {
	int T;	cin >> T;
	double C, F, X, y;
	cout << setprecision(7) << fixed;
	for (int x = 1; x <= T; x++) {
		cin >> C >> F >> X;
		cout << "Case #" << x << ": " << process(C, F, X, 2, 0) << endl;
	}
}
