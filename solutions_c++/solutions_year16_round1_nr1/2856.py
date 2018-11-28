#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>
#include <vector>
#include <cassert>
#include <unordered_map>

using namespace std;

struct TestCase {
	string S;
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
		fs >> tc.S;
		res.push_back(tc);
	}
	fs.close();
	return res;
}

std::string solve(TestCase& tc) {
	string res = string("") + tc.S[0];
	for (int i = 1; i < tc.S.size(); i++) {
		if (tc.S[i] >= res[0])
			res = tc.S[i] + res;
		else
			res += tc.S[i];
	}
	return res;
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
