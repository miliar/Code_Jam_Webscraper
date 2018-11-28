#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>
#include <vector>
#include <cassert>
#include <unordered_map>

using namespace std;

struct TestCase {
	long long k, c, s;
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
		fs >> tc.k >> tc.c >> tc.s;
		res.push_back(tc);
	}
	fs.close();
	return res;
}

std::string solve(TestCase& tc) {
	long long length = (long long)powl(tc.k, tc.c);
	long long segmentLength = length / tc.k;

	if (tc.s == tc.k) {
		string res;
		for (int i = 0; i < tc.s; i++) {
			res += to_string(i + 1);
			res += ' ';
		}
		return res;
	}
	return "IMPOSSIBLE";
}

int main(int argc, const char *argv[]) {
	std::ofstream fs("D-small-attempt0.out");
	int i = 1;
	for (auto tc : load("D-small-attempt0.in")) {
		fs << "Case #" << i << ": " << solve(tc) << std::endl;
		i++;
	}
	fs.close();
	return 0;
}
