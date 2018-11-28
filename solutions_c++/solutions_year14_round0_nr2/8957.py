#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <iomanip>

using namespace std;

int main() {

	int no_cases = 0;
	cin >> no_cases;
	std::cout << std::setprecision(7) << fixed;
	for (int cases = 1; cases <= no_cases; cases++) {
		double C, F, X;
		cin >> C >> F >> X;
		double new_time = 0;
		double current_time = 0;
		double no_cookies = 0;
		double end_time = 0;
		double current_rate = 2.0;
		double t_time = 0;
		t_time = 0;
		while (new_time <= current_time) {
			current_time = t_time + X / current_rate;
			new_time = t_time + C/current_rate + X / (current_rate + F);
			if (new_time < current_time) {
				t_time = t_time + C / current_rate;
			}
			else {
				end_time = current_time;
				break;
			}
			current_rate = current_rate + F;
		}
		if (cases == no_cases) {
			cout << "Case #" << cases << ": " << end_time;
		}
		else {
			cout << "Case #" << cases << ": " << end_time << endl;
		}
	}

	return 0;
}
