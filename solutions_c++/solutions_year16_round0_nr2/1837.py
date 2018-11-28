#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>
#include <vector>
#include <cassert>
#include <unordered_map>

using namespace std;

struct TestCase {
	string stack;
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
		fs >> tc.stack;
		res.push_back(tc);
	}
	fs.close();
	return res;
}

bool allplus(const string& stack) {
	bool allplus = true;
	for (int i = 0; i < (int)stack.length(); i++) {
		if (stack[i] == '-')
			return false;
	}
	return true;
}

void swap(string& stack) {
	int end = -1;
	for (int i = stack.length() - 1; i >= 0; i--) {
		if (stack[i] == '-') {
			end = i;
			break;
		}
	}

	for (int i = 0; i <= end; i++) {
		if (stack[i] == '+') {
			stack[i] = '-';
		} else {
			stack[i] = '+';
		}
	}
}

std::string solve(TestCase& tc) {
	string stack = tc.stack;
	int count = 0;
	while (!allplus(stack)) {
		swap(stack);
		++count;
	}
	return std::to_string(count);
}

int main(int argc, const char *argv[]) {
	std::ofstream fs("B-large.out");
	int i = 1;
	for (auto tc : load("B-large.in")) {
		fs << "Case #" << i << ": " << solve(tc) << std::endl;
		i++;
	}
	fs.close();
	return 0;
}

