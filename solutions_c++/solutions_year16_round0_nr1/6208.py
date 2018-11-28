// gcj_1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>

using namespace std;

template<typename T>
std::string to_string(T&& value) {
	std::stringstream ss;
	ss << value;
	return ss.str();
}

// cast from a string to desired type

template<typename T>
pair<bool, T> from_string(const std::string& value) {
	T result;
	std::istringstream is(value);
	is >> result;
	if (!is.bad())
		return make_pair(true, result);
	else
		return pair<bool, T>{};
}

int main()
{
	std::string line;
	std::getline(std::cin, line);

	auto no_test_cases = from_string<size_t>(line).second;

	vector<size_t> output;

	for (size_t i = 0; i < no_test_cases; ++i) {
		std::getline(std::cin, line);
		auto this_case = from_string<size_t>(line).second;

		if (this_case == 0) {
			output.push_back(0);
			continue;
		}

		size_t curr_no = this_case;
		set<size_t> digits_seen;

		auto insert_digits = [&]() {
			auto digit_no = curr_no;
			while (digit_no != 0) {
				auto temp = digit_no;
				temp %= 10;
				digits_seen.insert(temp);
				digit_no /= 10;
			}
		};

		insert_digits();

		while (digits_seen.size() != 10) {
			curr_no += this_case;
			insert_digits();
		}

		output.push_back(curr_no);
	}

	ofstream myfile;
	myfile.open("example.txt");

	for (size_t i = 0; i < output.size(); ++i)
		myfile << "Case #" << to_string(i+1) << ": " << (output[i] == 0 ? "INSOMNIA" : to_string(output[i])) << endl;
	myfile.close();

#ifdef WIN32
	std::string exit_on_enter;
	std::getline(std::cin, exit_on_enter);
#endif

    return 0;
}

