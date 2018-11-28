// q1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <fstream>
#include <sstream>

#include <iostream>
#include <string>

#include <map>
#include <vector>
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

	ofstream myfile;
	myfile.open("out.txt");

	auto no_test_cases = from_string<size_t>(line).second;
	for (size_t test_no = 1; test_no <= no_test_cases; ++test_no) {
		std::getline(std::cin, line);
		auto word = line;

		std::string solution{ *word.begin() };

		for (auto it = std::next(word.begin()); it != word.end(); ++it) {
			auto ch = *it;
			if (ch >= solution.front())
				solution.insert(solution.begin(), ch);
			else
				solution.push_back(ch);
		}

		myfile << "Case #" << to_string(test_no) << ": " << solution << endl;
	}

	myfile.close();

    return 0;
}

