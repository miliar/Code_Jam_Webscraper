#include <iostream>

using namespace std;

int main()
{
	int T, CCnt = 0;
	double C, F, X;

	cin >> T;

	while (CCnt < T) {
		cin >> C >> F >> X;
		double R = 2, tSum = C / R;
		double answer = X / R;
		while (answer > tSum + X / (R + F)) {
			answer = tSum + X / (R + F);
			R += F;
			tSum += C / R;
		}
		printf("Case #%d: %.7lf\n", ++CCnt, answer);
	}

	return 0;
}
