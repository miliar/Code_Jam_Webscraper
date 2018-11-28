#include <memory>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <stdlib.h>
#include <map>
#include <algorithm>
#include <cmath>

bool isPalindrome(long n) {
	long num = n;
	long rev = 0;
	while (num > 0) {
		rev = rev * 10 + num % 10;
		num /= 10;
	}
	return n == rev;
}

void solveCase(std::ifstream& in, std::ofstream& out) {
	long A, B;
	in >> A;
	in >> B;

	long count = 0;
	//int limit = ((int) sqrtf(B)) + 1;
	for (int i = A; i <= B; i++) {
		//std::cout << i << " " << isPalindrome(i) << std::endl;
		if (isPalindrome(i)) {
			long sq = (long)sqrtf(i);
			if (sq*sq == i && isPalindrome(sq)) {
				//std::cout << i << std::endl;
				count++;
			}
		}
	}
	out << count;
}

int main() {
	std::string baseDir = "problems2013/";
	std::string testFile = "C-small-attempt0";

	std::ifstream in(baseDir + testFile + ".in");
	std::ofstream out(baseDir + testFile + ".out");
	std::string t = baseDir + testFile + ".in";

	std::cout << "Starting solving cases..." << std::endl;

	int numberOfCases = 0;
	int currCase = 0;

	in >> numberOfCases;

	while (currCase++ < numberOfCases) {
		out << "Case #" << currCase << ": ";
		try {
			solveCase(in, out);
		} catch (std::exception& e) {
			std::cout << "Error on Case #" << currCase << " " << e.what()
					<< std::endl;
		}
		if (currCase < numberOfCases) {
			out << std::endl;
		}
		std::cout << "Cases solved (" << currCase << "/" << numberOfCases << ")"
				<< std::endl;
	}

	std::cout << "All cases solved!";
	return 0;
}
