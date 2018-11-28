#include<iostream>
using std::cout;
using std::cin;
using std::endl;
int main()
{
	int nTestCases;
	cin >> nTestCases;
	++nTestCases;

	cout.precision(30);

	for (int i = 1; i != nTestCases; ++i) {
		double C, F, X;
		cin >> C >> F >> X;
		double dC = 2;
		double t = 0;
//time to get X cookies at current rate, times dC
		double currentRateTime=X;
// time to get X cookies at current rate +F, times dC
		double newRateTime;

		while (1) {
			//currentRateTime = X;
			//newRateTime = ( (X + C) * dC + C * F) / (F + dC);
			newRateTime = C+X*dC/(dC+F);

			//cout << currentRateTime << "vs"<< newRateTime<<endl;

			if (newRateTime > currentRateTime) break;

			//time spent to get a factory up
			t += C/dC;
			dC += F;
		}

		t += currentRateTime/dC;
		cout << "Case #" << i << ": " << t << endl;
	}
}
