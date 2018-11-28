#include <iostream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

int main() {
	double test_cases, C, F;
	double X;
	cin >> test_cases;
	vector<double> results(test_cases);
	for (int i = 0; i < test_cases; i++) {
		cin >> C >> F >> X;
		double rate = 2;
		double cks = 0;
		double time = 0;
		while (cks < X) {
			double time_1 = X/rate;
			double time_r = C/(rate);
			while ((X/rate) > ((C/rate)+(X/(rate+F)))) {
				time = time + double((C/rate));
				rate = rate + double(F);
				time_1 = X/rate;
				time_r = C/(rate);
			}
			cks = X;
			time = time + double((X/rate));
			results[i] = time;
		}
	}
	string s = "Case #";
	int c = 1;	
	
	for (int i = 0; i < test_cases; i++) {
		cout << fixed;
		cout.precision(7);
		cout << s;
		cout << to_string(c);
		c++;
		cout << ": " << results[i] << endl;
	}	
	return 0;
}	
