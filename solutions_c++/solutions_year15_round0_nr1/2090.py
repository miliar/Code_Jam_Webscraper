// StandingOvation.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <sstream>

int solve_case(int s_max, std::vector<int> s_levels) {
	int standing = s_levels[0], result = 0;
	for (int i = 1; i <= s_max; i++) {
		int add = 0;
		if (s_levels[i] != 0 && i > standing) {
			add = i - standing;
		}
		result += add;
		standing += add + s_levels[i];
	}
	return result;
}

int _tmain(int argc, _TCHAR* argv[])
{
	std::ifstream in("in.txt");
	std::streambuf *cinbuf = std::cin.rdbuf();
	std::cin.rdbuf(in.rdbuf());

	std::ofstream out("out.txt");
	std::streambuf *coutbuf = std::cout.rdbuf();
	std::cout.rdbuf(out.rdbuf());

	int T;
	std::cin >> T;
	for (int i = 1; i <= T; i++) {
		// build input for single test case
		int s_max;
		std::string s_string;
		std::cin >> s_max >> s_string;
		std::vector<char> s_chars(s_string.begin(), s_string.end());
		std::vector<int> s_levels;
		for (int i = 0; i < s_chars.size(); i++) {
			char c = s_chars[i];
			s_levels.push_back(c - '0');
		}
		// compute output
		std::cout << "Case #" << i << ": " << solve_case(s_max, s_levels) << std::endl;
	}

	std::cin.rdbuf(cinbuf);
	std::cout.rdbuf(coutbuf);
	return 0;
}