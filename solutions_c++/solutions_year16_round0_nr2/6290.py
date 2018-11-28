// gcj_2.cpp : Defines the entry point for the console application.
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

	for(size_t test_no = 0; test_no < no_test_cases; ++test_no) {
		std::getline(std::cin, line);
		vector<bool> happy_sides;
		happy_sides.reserve(line.size());
		for (auto&& ch : line) {
			if (ch == '+')
				happy_sides.push_back(true);
			else if (ch == '-')
				happy_sides.push_back(false);
			else
				throw("argh!");
		}

		size_t no_diff = 0;
		if (happy_sides.size() > 1) {
			auto it_first = happy_sides.begin();
			auto it_second = std::next(it_first);
			while (it_second != happy_sides.end()) {
				if( *it_first != *it_second )
					++no_diff;
				++it_first, ++it_second;
			}
		}
		size_t end_penalty = (!happy_sides.empty() && !happy_sides.back()) ? 1 : 0;

		output.push_back(no_diff + end_penalty);
	}

	ofstream myfile;
	myfile.open("out.txt");

	for (size_t i = 0; i < output.size(); ++i)
		myfile << "Case #" << to_string(i + 1) << ": " << to_string(output[i]) << endl;
	myfile.close();

#ifdef WIN32
	std::string exit_on_enter;
	std::getline(std::cin, exit_on_enter);
#endif

	return 0;
}

