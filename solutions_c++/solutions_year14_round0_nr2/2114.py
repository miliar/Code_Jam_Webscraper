#include <iomanip>
#include <iostream>
#include <string>
#include <vector>

#define PRECISION 7

using namespace std;

int main()
{
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);
	cout << setiosflags(ios::fixed) << setprecision(PRECISION);

	unsigned int T, iter;
	double  C, F, X;
	cin >> T;
	double result;
	iter = 0;
	while (iter++ < T) {
		
		cin >> C >> F >> X;
		double timeToX = X / 2.0;
		double timeToFarm = C / 2.0;
		double rate = 2.0 + F;
		double currentElapseTime = timeToFarm;

		double nextTimeToX = currentElapseTime + (X / rate);
		
		while (nextTimeToX < timeToX) {
			timeToX = nextTimeToX;
			timeToFarm = C / rate;
			currentElapseTime += timeToFarm;
			rate += F;
			nextTimeToX = currentElapseTime + (X / rate);
		}
		
		cout << "Case #" << iter << ": " << timeToX << endl;
	}
	return EXIT_SUCCESS;
}