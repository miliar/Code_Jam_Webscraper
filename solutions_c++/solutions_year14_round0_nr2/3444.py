#include <iostream>
#include <stdio.h>
#include <iomanip>

bool is_worth_to_buy_cookies(double const& C, double const& F, double const& X, double const& cook_per_sec, double * next_farm_cost) {

	double missing_time = (X / cook_per_sec);
	
	(*next_farm_cost) = (C / cook_per_sec);
	double next_missing_time = (X / (cook_per_sec + F));

	return ((*next_farm_cost) + next_missing_time) < missing_time;
}

int main() {
	std::ios_base::sync_with_stdio(0);
	std::cout << std::fixed << std::setprecision(7);

	int test_cases;
	std::cin >> test_cases;

	int current_case = 1;

	while (current_case <= test_cases)
	{
		double F;
		double C;
		double X;
		
		double cookies_per_second = 2.0;
		double total_time = 0;

		std::cin >> C >> F >> X;

		double register next_farm_cost;

		while (is_worth_to_buy_cookies(C, F, X, cookies_per_second, &next_farm_cost)) {
			total_time += next_farm_cost;
			cookies_per_second += F;
		}
		
		total_time += (X / cookies_per_second);
		std::cout << "Case #" << current_case << ": " << total_time << std::endl;

		current_case++;
	}
}