#include <iostream>
#include <sstream>
#include <string>

#include <set>
#include <algorithm>
#include <iterator>

// Using boost libraries (1.53.0)
// https://sourceforge.net/projects/boost/files/boost/1.53.0/
#include <boost/date_time/posix_time/posix_time.hpp>
#include <boost/lexical_cast.hpp>

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

std::string solve_test_case() {
	std::set<int> first_row;
	std::set<int> second_row;
	auto first_row_num = gl<int>();
	for (auto i = 1; i <= 4; ++i) {
		if (i != first_row_num) {
			std::string junk;
			std::getline(std::cin, junk);
			continue;
		}
		std::string line;
		std::getline(std::cin, line);
		std::istringstream iss(line);
		for (auto j = 1; j <= 4; ++j) {
			int i;
			iss >> i;
			first_row.insert(i);
		}
	}
	auto second_row_num = gl<int>();
	for (auto i = 1; i <= 4; ++i) {
		if (i != second_row_num) {
			std::string junk;
			std::getline(std::cin, junk);
			continue;
		}
		std::string line;
		std::getline(std::cin, line);
		std::istringstream iss(line);
		for (auto j = 1; j <= 4; ++j) {
			int i;
			iss >> i;
			second_row.insert(i);
		}
	}
	std::vector<int> solutions;
	std::set_intersection(first_row.begin(), first_row.end(), second_row.begin(), second_row.end(), std::inserter(solutions, solutions.begin()));
	switch (solutions.size()) {
		case 0:
			return "Volunteer cheated!";
		case 1:
			return boost::lexical_cast<std::string>(solutions.front());
		default:
			break;
	}
	return "Bad magician!";
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
