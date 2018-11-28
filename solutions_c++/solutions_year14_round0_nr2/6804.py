#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

int main() {
	int T;
	cin >> T;

	cout << fixed << setprecision(7);

	for (int i = 1; i <= T; ++i) {
		double tiem = 0, C, F, X, rate = 2; 
		cin >> C >> F >> X;

		double flatTime = X/rate;
		double timeWithNew = X/(rate+F);
		double timeToNew = C/rate;

		while (flatTime > (timeWithNew + timeToNew)) {
			tiem += timeToNew;
			rate += F;

			flatTime = X/rate;
			timeWithNew = X/(rate+F);
			timeToNew = C/rate;
		}

		cout << "Case #" << i << ": " << tiem + flatTime << endl;
	}
}