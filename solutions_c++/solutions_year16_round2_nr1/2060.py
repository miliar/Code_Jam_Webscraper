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
#include <algorithm>
#include <numeric>

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

	vector<pair<size_t, string>> char_order{
		{ 0, "ZERO" },
		{ 2, "TWO" },
		{ 6, "SIX" },
		{ 8, "EIGHT" },
		{ 3, "THREE" },
		{ 4, "FOUR" },
		{ 5, "FIVE" },
		{ 7, "SEVEN" },
		{ 1, "ONE" },
		{ 9, "NINE" }
	};


	auto no_test_cases = from_string<size_t>(line).second;
	for (size_t test_no = 1; test_no <= no_test_cases; ++test_no) {
		std::getline(std::cin, line);
		auto string_s = line;

		map<size_t, size_t> digit_to_count;

		map<char, size_t> count_char;
		for (char ch : string_s)
			++count_char[ch];

		for (auto tup : char_order) {
			//auto ch = get<0>(tup);
			auto num = get<0>(tup);
			auto word = get<1>(tup);

			auto no_of_word = accumulate(word.begin(), word.end(), count_char[word.front()], [&count_char](size_t count, char ch) { return min(count, count_char[ch]); });
			for (auto ch : word)
				count_char[ch] -= no_of_word;

			digit_to_count[num] += no_of_word;
		}

		string solution_str;
		for (auto p : digit_to_count) {
			for (auto i = 0; i < p.second; ++i)
				solution_str += to_string(p.first);
		}

		myfile << "Case #" << to_string(test_no) << ": " << solution_str << endl;
	}

	myfile.close();

	return 0;
}

