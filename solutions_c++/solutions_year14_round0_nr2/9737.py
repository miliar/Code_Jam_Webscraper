#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

double rec(double time, int farm, double C, double F, double X) {
	// buy 1 more farm
	int n = farm + 1;
	double newTime = 0;
	for (int i = 0; i < n; ++i) {
		newTime += C / (2.0 + (i*F));
	}
	newTime += X / (2.0 + (n*F));

	if (newTime > time)
		return time;
	else return rec(newTime, n, C, F, X);
}

int main()
{
	int T;
	cin >> T;
	cout << fixed;
	cout << setprecision(7);
	for (int t = 1; t <= T; t++) {
		double C, F, X;
		cin >> C >> F >> X;
		cout << "Case #" << t << ": " << rec(X / 2.0, 0, C, F, X) << endl;
	}
	return 0;
}

