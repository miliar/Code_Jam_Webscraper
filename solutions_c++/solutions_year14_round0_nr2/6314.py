#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>

using namespace std;

double end_time(double F, double X, double t)
{
	return t + X/F;
}

double buy_farm_time(double C, double F)
{
	return C/F;
}

int main()
{
	unsigned num_cases;
	cin >> num_cases;
	cout << fixed << setprecision(7);
	for (unsigned i = 1; i <= num_cases; i++) {
		double C, F, X;
		cin >> C >> F >> X;
		double F_curr = 2.0, time_curr = 0.0, end_time_curr, end_time_prev;
		end_time_curr = end_time_prev = end_time(F_curr, X, time_curr);
		while (end_time_prev >= end_time_curr) {
			end_time_prev = end_time_curr;
			time_curr += buy_farm_time(C, F_curr);
			F_curr += F;
			end_time_curr = end_time(F_curr, X, time_curr);
		}
		cout << "Case #" << i << ": " << end_time_prev << "\n";
	}
	return 0;
}
