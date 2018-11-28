#include <cstddef>
#include <fstream>
#include <iomanip>
#include <iostream>

using std::size_t;

double simulate (size_t num_fac,
	double cost,
	double extra_income,
	double target) {

	double result {0};
	double income {2};

	for (size_t i = 0; i < num_fac; ++i) {
		result += cost/income;
		income += extra_income;
	}

	result += target/income;

	return result;
}

double best (
	double cost,
	double extra_income,
	double target) {

	double best_time = target/2;
	size_t best_fac = 0;
	double test_time;
	//While extra factory is faster
	while ( (test_time = simulate(best_fac+1,
				cost,extra_income,target)) < best_time) {
		best_time = test_time;
		++best_fac;
	}

	return best_time;
}


int main (int argc, const char* argv[]) {
	if (argc != 2) {
		std::cerr << "You morron!\n";
		return -1;
	}

	std::ifstream in {argv[1]};
	std::ofstream out {"cookie.out"};

	out << std::setiosflags(std::ios::fixed) << std::setprecision(7);

	int num_cases;
	in >> num_cases;

	for (int i = 1; i <= num_cases; ++i) {
		double cost, extra_income, target;
		in >> cost >> extra_income >> target;

		out << "Case #" << i << ": "
			<< best(cost,extra_income,target) << "\n";
	}

}