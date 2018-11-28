#include <iostream>
#include <iomanip>

using namespace std;

double timeToComplete(const double &rate, const double &X) {
	return X / rate;
}

bool isSmaller(const double &a, const double &b) {
	if ((a-b) < 10e-9)
		return true;
	return false;
}

int main() {
	cout.precision(7);
	cout << fixed;

	int T;
	cin >> T;

	for(int i = 1; i < T+1; ++i) {
	
		double C, F, X;
		double total = 0;
		
		cin >> C >> F >> X;

		//cout << '\n';
		//cout << C << ' ' << F << ' ' << X << '\n';
	
		double rate = 2.0;
		for(int j = 0;; ++j) {
			double to_complete, to_completeC;
			double next_cookie;
			double next_rate;
			bool cont;
			
			to_complete = timeToComplete(rate, X);
			next_cookie = timeToComplete(rate, C);
			next_rate = rate + F;
			to_completeC = next_cookie + timeToComplete(next_rate,
								    X);

			cont = isSmaller(to_complete, to_completeC);

			//cout << "Step " << j << ": " << to_complete << ' ';
			//cout << to_completeC << ' ' << cont << '\n';
			//cout << "Total: " << total << '\n';
			if( cont ) {
				total += to_complete;
				break;
			} else {
				total += next_cookie;
				rate += F;
			}
		}

		cout << "Case #" << i << ": " << total << '\n';

	}

    return 0;
}
