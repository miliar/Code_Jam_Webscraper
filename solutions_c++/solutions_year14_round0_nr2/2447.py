#include <iostream>
#include <fstream>
#include <stdio.h>
int main() {
	std::ifstream input;
	input.open("./data/B-large.in");
	std::ofstream out;
	out.open("./data/B-large.out");
	long cases;
	input >> cases;

	double default_cps = 2.;
	std::cout << cases << std::endl;
	for (long c = 0; c < cases; ++c) {
		double farm_cost = 0;
		double add_cps = 0;
		double win_cond = 0;
		input >> farm_cost;
		input >> add_cps;
		input >> win_cond;

		double current_time = win_cond / default_cps;
		double time_offset = 0;
		double current_cps = default_cps;
		double next_time = time_offset + farm_cost/current_cps + win_cond/(current_cps+add_cps);
		while (next_time < current_time) {
			current_time = next_time;
			time_offset += farm_cost/current_cps;
			current_cps += add_cps;
			next_time = time_offset + farm_cost/current_cps + win_cond/(current_cps+add_cps);
		}
		// std::cout << current_time << std::endl;
		char buffer [50];
		sprintf(buffer, "%.7f", current_time);
		std::string result{buffer};
		std::cout << result << std::endl;
		out << "Case #" << c+1 << ": " << result << std::endl;
	}
	input.close();
	out.close();
}