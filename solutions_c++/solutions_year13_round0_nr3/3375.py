#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <utility>
#include <cassert>
#include <cstdint>
#include <cmath>

//#include <gmpxx.h>
using big_int = unsigned long long;//mpz_class;

bool is_fair(const big_int& num){
	std::string str = std::to_string(num);
	size_t len = str.length();
	for(size_t pos = 0; pos < len/2; ++pos){
		if(str[pos] != str[len-(pos+1)]){
			return false;
		}
	}
	return true;
}

bool in_range(const big_int& num, const big_int& lower_limit, const big_int& upper_limit){
	auto returnval = num>=lower_limit && num <= upper_limit;
	return returnval;
}

unsigned long test_range(const big_int& low, const big_int& high){
	auto low_root = big_int(sqrt(low));
	auto high_root = big_int(sqrt(high));
	unsigned long found_numbers = 0;
	for(auto n = low_root; n <= high_root; ++n){
		if(!is_fair(n)){
			continue;
		}
		auto tmp = big_int{n}*big_int{n};
		if(is_fair(tmp) && in_range(tmp, low, high)){
			++found_numbers;
			std::cout << n << "² = " << tmp << std::endl;
		}
	}
	return found_numbers;
}

int main(int argc, char** argv){
	if(argc != 3) {
		return 1;
	}
	std::ifstream input{argv[1]};
	if(!input.is_open()){
		std::cerr << "cannot open inputfile" << std::endl;
		return 2;
	}
	std::ofstream output{argv[2]};
	if(!output.is_open()){
		std::cerr << "cannot open output" << std::endl;
		return 3;
	}
	std::string line;
	getline(input, line);
	int number_of_tests{std::stoi(line)};
	std::vector<std::pair<big_int, big_int>> ranges;
	ranges.reserve(number_of_tests);
	for(int i = 0; i < number_of_tests; ++i){
		getline(input, line);
		auto delim_pos = line.find(" ");
		if(delim_pos == std::string::npos){
			return 4;
		}
		ranges.emplace_back(
				std::stoul(line.substr(0, delim_pos)),
				std::stoul(line.substr(delim_pos+1))
				//big_int{line.substr(0, delim_pos)},
				//big_int{line.substr(delim_pos+1)}
		);
	}
	
	for(int i=0; i<number_of_tests; ++i){
		big_int found_fair_and_squares = test_range(ranges[i].first, ranges[i].second);
		output << "Case #"<< i+1 << ": " << found_fair_and_squares << "\n";
	}
}
