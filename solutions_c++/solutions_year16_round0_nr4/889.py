#include <iostream>
using namespace std;

typedef unsigned long long ull;

int divisionCeiling(int x, int y) {
	return 1 + ((x - 1) / y);
}

int main() {
	int cases;
	cin >> cases;
	for (int caseCounter = 1; caseCounter <= cases; caseCounter++) {
		int k, c, s;
		cin >> k >> c >> s;

		int needToCover = k;
		int coveredWithOneQuery = max(1, c);
		int queriesAvailable = s;

		int queriesNeeded = divisionCeiling(needToCover, coveredWithOneQuery);

		if (queriesNeeded > queriesAvailable) {
			cout << "Case #" << caseCounter << ": IMPOSSIBLE" << endl;
			continue;
		}

		cout << "Case #" << caseCounter << ":";

		int first = 0;
		int last = min(first + coveredWithOneQuery - 1, k - 1);
		for (int i = 1; i <= queriesNeeded; i++) {
			ull position = 0;
			for (int j = first; j <= last; j++)
				position = position * k + j;
			cout << " " << position + 1;
			first += coveredWithOneQuery;
			last = min(first + coveredWithOneQuery - 1, k - 1);
		}
		cout << endl;
	}
	return 0;
}
