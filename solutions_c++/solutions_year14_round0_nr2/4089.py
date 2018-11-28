#include <iostream>
#include <sstream>
#include <string>

// Using boost libraries (1.53.0)
// https://sourceforge.net/projects/boost/files/boost/1.53.0/
#include <boost/date_time/posix_time/posix_time.hpp>
#include <boost/format.hpp>

// get a line of input
template <typename T>
T gl() {
	std::string s;
	std::getline(std::cin, s);
	std::istringstream ss(s);
	T result;
	ss >> result;
	return result;
}

template <>
std::string gl<std::string>() {
	std::string s;
	std::getline(std::cin, s);
	return s;
}


#define LOG \
	std::cerr << boost::posix_time::microsec_clock::local_time() \
<< ": " << __FILE__ << ": " << __LINE__ << ": "

double to_goal(double goal, double rate)
{
	return goal / rate;
}

double to_factory(double cost, double rate)
{
	return cost / rate;
}

std::string solve_test_case() {
	double elapsed_time = 0.0;
	double rate = 2.0;
	double COST_OF_FACTORY;
	double FACTORY_OUTPUT;
	double GOAL;
	std::cin >> COST_OF_FACTORY >> FACTORY_OUTPUT >> GOAL;
	double tgc = to_goal(GOAL, rate);
	double tf = to_factory(COST_OF_FACTORY, rate);
	double tgn = to_goal(GOAL, rate + FACTORY_OUTPUT);
	double tgwaf = tf + tgn;
	while (tgc > tgwaf) {
		elapsed_time += tf;
		rate += FACTORY_OUTPUT;
		tgc = tgn;
		tf = to_factory(COST_OF_FACTORY, rate);
		tgn = to_goal(GOAL, rate + FACTORY_OUTPUT);
		tgwaf = tf + tgn;
	}
	elapsed_time += tgc;
	return boost::str(boost::format("%.7f") % elapsed_time);
}

int main (int argc, char ** argv) {
	auto N = gl<int>();
	LOG << "There are " << N << " test cases" << std::endl;
	for (auto i = 1; i <= N; ++i) {
		LOG << "Attempting case #" << i << std::endl;
		auto result = solve_test_case();
		LOG << "Case #" << i << ": " << result << std::endl;
		std::cout << "Case #" << i << ": " << result << std::endl;
	}
}
