#include <algorithm>
#include <iostream>
#include <unordered_map>
#include <unordered_set>

using namespace std;

void solveProblem(unordered_set<int> &firstSet, unordered_set<int> &secondSet) {
	int result = 0;
	int answer = -1;
	for (auto &val : firstSet) {
		if (secondSet.count(val) > 0) {
			++result;
			answer = val;
		}
	}

	if (result == 0) {
		cout << "Volunteer cheated!";
	} else if (result == 1) {
		cout << answer;
	} else {
		cout << "Bad magician!";
	}
}

int main() {
	int testCases = 0;

	cin >> testCases;

	for (int i = 1; i <= testCases; ++i) {
		// Load data
		unordered_map<int, unordered_set<int>> firstSet, secondSet;
		int firstAnswer, secondAnswer;

		cin >> firstAnswer;
		for (int row = 0; row < 4; ++row) {
			unordered_set<int> rowContent;
			for (int col = 0; col < 4; ++col) {
				int tmp;
				cin >> tmp;
				rowContent.insert(tmp);
			}
			firstSet[row] = rowContent;
		}

		// Second set
		cin >> secondAnswer;
		for (int row = 0; row < 4; ++row) {
			unordered_set<int> rowContent;
			for (int col = 0; col < 4; ++col) {
				int tmp;
				cin >> tmp;
				rowContent.insert(tmp);
			}
			secondSet[row] = rowContent;
		}

		// Solve problem
		cout << "Case #" << i << ": ";
		solveProblem(firstSet[firstAnswer - 1], secondSet[secondAnswer - 1]);
		cout << endl;
	}

	return 0;
}
