#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <iomanip>

#define MAX_ITERATIONS 10000

using namespace std;

double result(double curr_rate, double inc, double farm_cost, double win, int iterations) {
	double seconds_to_win_without_farm = win/curr_rate;

	if (iterations > MAX_ITERATIONS)
		return seconds_to_win_without_farm;
	
	return min(seconds_to_win_without_farm, farm_cost/curr_rate + result(curr_rate+inc, inc, farm_cost, win, iterations+1));
}

int main(void) {
	int cases; cin >> cases;
	int case_number=0;

    std::cout << std::fixed << std::setprecision(7);

	while (cases-->0) {
		case_number++;

		double farm_cost, extra_production, win; 
		cin >> farm_cost >> extra_production >> win;

		double ans = result(2.0, extra_production, farm_cost, win, 0);

		cout << "Case #" << case_number << ": " << ans << endl;		
	}
}