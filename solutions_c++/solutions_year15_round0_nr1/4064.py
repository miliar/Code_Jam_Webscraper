#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>
#include <vector>
#include <cassert>
using namespace std;

struct TestCase {
	int maxShyness;
	vector<int> shynessCounts;
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
		fs >> tc.maxShyness;
		string counts;
		fs >> counts;
		assert(counts.size() == tc.maxShyness + 1);
		for (int j = 0; j < tc.maxShyness + 1; j++) {
			int val = counts[j] - '0';
			assert(val <= 9);
			tc.shynessCounts.push_back(val);
		}
		res.push_back(tc);
	}
	fs.close();
	return res;
}

void solve(TestCase& tc, std::ostream& os) {
	int standing = 0;
	int missingTotal = 0;
	for (int i = 0; i < tc.shynessCounts.size(); i++) {
		int missing = max(0, i - standing);
		standing += tc.shynessCounts[i] + missing;
		missingTotal += missing;
	}
	os << missingTotal;
}

int main(int argc, const char *argv[]) {
	std::ofstream fs("A-large.out");
	fs.precision(8);
	fs << std::fixed;
	int i = 1;
	for (auto tc : load("A-large.in")) {
		fs << "Case #" << i << ": ";
		solve(tc, fs); fs << std::endl;
		i++;
	}
	fs.close();
	return 0;
}
