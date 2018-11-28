// InfiniteHouseOfPancakes.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <sstream>

std::vector<int> calc_stack(int p) {
	std::vector<int> s;
	int entry = p;
	int last = p;
	int n = 2;
	do {
		s.push_back(entry);
		last = entry;
		entry = (p + n - 1) / n;
		n++;
	} while (entry < last);
	return s;
}

int solve_case(int D, std::vector<int> diners) {
	int max_d = 1001;
	for (int i = 0; i < D; i++) {
		max_d = std::max(max_d, diners[i]);
	}

	std::vector<int> DP = calc_stack(diners[0]);
	for (int i = 1; i < D; i++) {
		std::vector<int> s = calc_stack(diners[i]);
		std::vector<int> DP_new(DP.size() + s.size(), 1001);
		for (int m = 0; m < DP.size(); m++) {
			for (int n = 0; n < s.size(); n++) {
				DP_new[m + n] = std::min(DP_new[m + n], std::max(DP[m], s[n]));
			}
		}
		// cut off tail
		int l = std::min((unsigned)max_d, DP_new.size());
		std::vector<int> temp(DP_new.begin(), DP_new.begin() + l);
		DP = temp;
	}
	int result = DP[0];
	for (int i = 1; i < DP.size(); i++) {
		result = std::min(result, DP[i] + i);
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
		int D;
		std::cin >> D;
		std::vector<int> diners;
		for (int j = 0; j < D; j++) {
			int e;
			std::cin >> e;
			diners.push_back(e);
		}
		// compute output
		std::cout << "Case #" << i << ": " << solve_case(D, diners) << std::endl;
	}

	std::cin.rdbuf(cinbuf);
	std::cout.rdbuf(coutbuf);

	/*
	std::vector<int> s = calc_stack(2);
	for (int i = 0; i < s.size(); i++) {
		std::cout << s[i] << " ";
	}
	*/

	return 0;
}