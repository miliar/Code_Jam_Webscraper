#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>
#include <vector>
#include <cassert>
#include <unordered_map>

using namespace std;

struct TestCase {
	long long number;
};

std::vector<TestCase> load(const std::string& s) {
	std::ifstream fs(s);
	if (!fs.is_open())
		std::cout << "Not found" << std::endl;

	int n;
	std::vector<TestCase> res;
	fs >> n;
	for (int i = 0; i < n; i++) {
		TestCase tc;
		fs >> tc.number;
		res.push_back(tc);
	}
	fs.close();
	return res;
}

bool accumDigits(long long nr, int(&digits)[10]) {
	while (nr > 0) {
		++digits[nr % 10];
		nr /= 10;
	}

	for (size_t i = 0; i < 10; i++) {
		if (digits[i] == 0)
			return false;
	}
	return true;
}

std::string solve(TestCase& tc) {
	long long nr = abs(tc.number);
	if (tc.number == 0)
		return "INSOMNIA";

	int digits[10];
	memset(digits, 0, sizeof(digits));
	long long current = nr;
	while (!accumDigits(current, digits)) {
		current += nr;
	}
	return std::to_string(current);
}

int main(int argc, const char *argv[]) {
	std::ofstream fs("A-large.out");
	int i = 1;
	for (auto tc : load("A-large.in")) {
		fs << "Case #" << i << ": " << solve(tc) << std::endl;
		i++;
	}
	fs.close();
	return 0;
}
