// -*- mode: c++; coding: utf-8; tab-width: 4; -*-
#include <iostream>
#include <limits>
#include <iomanip>

unsigned int to_flag(long v) {
	int flag = 0;
//	std::cout << v << ": ";
	while (true) {
		int m = v % 10;
		v = v / 10;
		flag = flag | (1 << m);
		if (v == 0) {
			break;
		}
	}
//	std::cout << std::hex << flag << std::endl;
//	std::cout << std::dec;
	return flag;
}

long check_count(long N) {
	if (N == 0) {
		return -1;
	}
	int flag = 0;
	int max = std::numeric_limits<int>::max();
	for (long i = 0; i < max; ++i) {
		long val = N * (i + 1);
		flag = flag | to_flag(val);
		if (flag == 0x3ff) {
			return val;
		}
	}
}

int main(int argc, char *argv[]) {
	int T;
	std::cin >> T;
	for (int i = 0; i < T; ++i) {
		long N;
		std::cin >> N;
		long c = check_count(N);
		std::cout << "Case #" << (i + 1) << ": ";
		if (c < 0) {
			std::cout << "INSOMNIA";
		} else {
			std::cout << c;
		}
		std::cout << std::endl;
	}
}
