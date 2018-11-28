#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>
#include <vector>
#include <cassert>
#include <unordered_map>
#include <map>

using namespace std;

struct TestCase {
	vector<int> counts;
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
		int s;
		fs >> s;
		for (int j = 0; j < s; j++) {
			int a;
			fs >> a;
			tc.counts.push_back(a);
		}
		res.push_back(tc);
	}
	fs.close();
	return res;
}

struct Party {
	int count;
	char name;
};

template <typename T>
int sumCount(T start, T end) {
	int s = 0;
	for (T it = start; it < end; ++it)
		s += it->count;
	return s;
}

std::string solve(TestCase& tc) {
	vector<Party> parties;
	for (size_t i = 0; i < tc.counts.size(); i++)
		parties.push_back(Party{ tc.counts[i], 'A' + i });
	auto comparator = [](const Party& a, const Party& b) { return b.count < a.count; };

	sort(parties.begin(), parties.end(), comparator);

	string res;
	while (parties.size() > 0 && parties.begin()->count > 0) {
		vector<Party> caseA = parties, caseB = parties;
		caseA[0].count = max(0, caseA[0].count - 1);

		caseB[0].count = max(0, caseB[0].count - 1);
		if (caseB.size() >= 2)
			caseB[1].count = max(0, caseB[1].count - 1);

		sort(caseA.begin(), caseA.end(), comparator);
		sort(caseB.begin(), caseB.end(), comparator);

		if (caseB.size() >= 2 && caseB[0].count <= sumCount(caseB.begin() + 1, caseB.end())) {
			res += parties[0].name;
			res += parties[1].name;
			parties = caseB;
		}
		else {
			res += parties[0].name;
			parties = caseA;
		}

		res += ' ';
		while (parties.size() > 0 && parties.rbegin()->count == 0)
			parties.resize(parties.size() - 1);
	}



	return res;
}

int main(int argc, const char *argv[]) {


	std::ofstream fs("A-large.out");
	int i = 1;
	for (auto tc : load("A-large.in")) {
		fs << "Case #" << i << ": " << solve(tc) << std::endl;
		std::cout << i << endl;
		i++;
	}
	fs.close();
	return 0;
}
