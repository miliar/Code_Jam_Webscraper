#include <iostream>
#include <iomanip>
using namespace std;

int T;
double C, F, X;

int main() {
	cin >> T;
	for (int I = 1; I <= T; I++) {
		cin >> C >> F >> X;
		double result = X / 2;
		double speed = 2;
		double timeSpent = 0;
		while (timeSpent + C / speed + X / (speed + F) < result) {
			result = timeSpent + C / speed + X / (speed + F);
			timeSpent += C / speed;
			speed += F;
		}

		cout.setf(ios::fixed | ios::showpoint);
		cout.precision(7);
		cout << "Case #" << I << ": " << result << endl;
	}
}