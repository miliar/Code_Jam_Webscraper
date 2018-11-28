#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <stack>
#include <queue>
#include <unordered_map>

using namespace std;

std::vector<std::string> splitString(const std::string& s, const std::string& delimiter) {
	std::vector<std::string> v;
	size_t start = 0;
	auto end = s.find(delimiter);

	if (end == std::string::npos) {
		v.push_back(s);
	}
	else {
		while (end != std::string::npos) {
			v.push_back(s.substr(start, end - start));
			end += delimiter.length();
			start = end;
			end = s.find(delimiter, end);

			if (end == std::string::npos) {
				v.push_back(s.substr(start, s.length()));
			}
		}
	}

	return v;
}

vector<string> generateAllReverse(const string& stackOfCake) {
	vector<string> nextStates;

	for (int reverseIndex = 0; reverseIndex < stackOfCake.size(); reverseIndex++) {
		string clone = stackOfCake;
		for (int i = 0; i <= reverseIndex; ++i) {
			swap(clone[i], clone[reverseIndex - i]);
		}

		for (int i = 0; i <= reverseIndex; ++i) {
			if (clone[i] == '+')
				clone[i] = '-';
			else
				clone[i] = '+';
		}
		nextStates.emplace_back(clone);
	}
	

	return nextStates;
}

bool check(const string& stackOfCake) {
	for (int i = 0; i < stackOfCake.size(); ++i) {
		if (stackOfCake[i] != '+')
			return false;
	}

	return true;
}

void solve(std::ifstream& in, std::ofstream& out) {
	int testCaseNum;
	string stackOfCake;
	in >> testCaseNum;
	const int MAX_STEP = 100;
	int t{ 1 };

	while (t <= testCaseNum) {
		unordered_map<string, vector<string>> nextStateChildrenMap;
		unordered_map<string, bool> currStateMap{};
		unordered_map<string, bool> nextStateMap{};
		in >> stackOfCake;
		bool find = false;

		currStateMap[stackOfCake];
		int step = 0;

		for (; step < MAX_STEP; step++) {
			for (auto it = currStateMap.begin(); it != currStateMap.end(); ++it) {
				if (check(it->first)) {
					find = true;
					break;
				}
				vector<string> nextStates{};
				if (nextStateChildrenMap.find(it->first) != nextStateChildrenMap.end()) {
					nextStates = nextStateChildrenMap[it->first];
				}
				else {
					nextStates = generateAllReverse(it->first);
				}

				for (auto& state : nextStates) {
					nextStateMap[state];
				}
			}
			
			if (find) {
				break;
			}

			currStateMap = nextStateMap;
		}

		out << "Case #" << t << ": " << step << std::endl;
		t++;
	}
}

int main() {
	std::ifstream smallDataFile{ "small-practice.in" };
	//std::ifstream largeDataFile{ "C-large-practice.in" };
	std::ofstream smallOutputFile{ "small.out" };
	//std::ofstream largeOutputFile{ "C-large.out" };

	solve(smallDataFile, smallOutputFile);
	//solve(largeDataFile, bigOutputFile);

	return 0;
}