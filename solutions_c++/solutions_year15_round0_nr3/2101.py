// Dijkstra.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <sstream>

const int value_table[4][4] = { { '1', 'i', 'j', 'k' },
	{ 'i', '1', 'k', 'j' },
	{ 'j', 'k', '1', 'i' },
	{ 'k', 'j', 'i', '1' } };

const bool bool_table[4][4] = { { true, true, true, true },
	{ true, false, true, false },
	{ true, false, false, true },
	{ true, true, false, false } };

char mult(char v, char w, bool& sign) {
	int v_int;
	switch (v) {
	case '1': v_int = 0; break;
	case 'i': v_int = 1; break;
	case 'j': v_int = 2; break;
	default: v_int = 3; break;
	}
	int w_int;
	switch (w) {
	case '1': w_int = 0; break;
	case 'i': w_int = 1; break;
	case 'j': w_int = 2; break;
	default: w_int = 3; break;
	}
	char new_v = value_table[v_int][w_int];
	sign = (sign == bool_table[v_int][w_int]);
	return new_v;
}

std::vector<char> quint(std::vector<char> w) {
	std::vector<char> w5(w.begin(), w.end());
	for (int i = 0; i < 4; i++) {
		w5.insert(w5.end(), w.begin(), w.end());
	}
	return w5;
}

std::vector<char> appendv(std::vector<char> w, int n) {
	std::vector<char> w5(w.begin(), w.end());
	for (int i = 0; i < n - 1; i++) {
		w5.insert(w5.end(), w.begin(), w.end());
	}
	return w5;
}

std::string solve_case(int L, int X, std::vector<char> w) {
	std::vector<char> w5 = quint(w), mw5(w5);
	std::reverse(mw5.begin(), mw5.end());
	// calculate index for i
	char v = '1';
	bool sign = true;
	int i = 0;
	while (i < L*5 && (v != 'i' || !sign)) {
		v = mult(v, w5[i], sign);
		i++;
	}
	if (i == L*5) {
		return "NO";
	}

	// calculate index for k
	v = '1';
	sign = true;
	int k = 0;
	while (k < L*5 && (v != 'k' || !sign)) {
		v = mult(mw5[k], v, sign);
		k++;
	}
	if (k == L*5) {
		return "NO";
	}
	k = L * X - k;
	if (i >= k) {
		return "NO";
	}
	// determine if j in middle segment
	if (true) {
		std::vector<char> full_w = appendv(w, X);
		v = '1';
		sign = true;
		int j = i;
		while (j < k) {
			v = mult(v, full_w[j], sign);
			j++;
		}
		if (v == 'j' && sign) {
			return "YES";
		}
		return "NO";
	}
	else {
		// initial segment
		v = '1';
		sign = true;
		int j1 = i;
		while (j1 % L != 0) {
			v = mult(v, w5[j1], sign);
			j1++;
		}
		char v_init = v;
		bool sign_init = sign;
		// end segment
		v = '1';
		sign = true;
		int j2 = 0;
		while (j2 < k % L) {
			v = mult(v, w5[j2], sign);
			j2++;
		}
		char v_end = v;
		bool sign_end = sign;
		// middle segment
		int blocks = (k - j1) / L;
		v = '1';
		sign = true;
		int j = 0;
		while (j < L) {
			v = mult(v, w[j], sign);
			j++;
		}
		char v_block = v;
		bool sign_block = sign;
		sign = true;
		char v_middle = '1';
		for (int m = 0; m < blocks; m++) {
			v = mult(v_middle, v_block, sign);
		}
		bool sign_middle;
		if (!sign_block && blocks % 2 == 1) {
			sign_middle = !sign;
		}
		else {
			sign_middle = sign;
		}

		// finally, calculate if j is middle segment result
		int sign_count = 0;
		if (sign_init) {
			sign_count++;
		} if (sign_middle) {
			sign_count++;
		} if (sign_end) {
			sign_count++;
		}
		bool extra_sign;
		if (sign_count == 1 || sign_count == 3) {
			extra_sign = false;
		}
		else {
			extra_sign = true;
		}
		// if sign count 1 or 3, add a minus
		v = v_init;
		sign = true;
		v = mult(v, v_middle, sign);
		v = mult(v, v_end, sign);
		if (v == 'j' && sign == extra_sign) {
			return "YES";
		}
		return "NO";
	}
	return "NO";
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
		int L, X;
		std::cin >> L >> X;
		std::vector<char> w;
		for (int j = 0; j < L; j++) {
			char c;
			std::cin >> c;
			w.push_back(c);
		}
		// compute output
		std::cout << "Case #" << i << ": " << solve_case(L, X, w) << std::endl;
	}

	std::cin.rdbuf(cinbuf);
	std::cout.rdbuf(coutbuf);

	return 0;
}