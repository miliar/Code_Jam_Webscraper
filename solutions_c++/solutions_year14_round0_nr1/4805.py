//============================================================================
// Name        : MagicTrick.cpp
// Author      : Xuanchen Tang
// Version     :
// Copyright   :
// Description : Google Code Jam, Qualification Round 2014, Problem A. Magic Trick
//============================================================================

#include <iostream>
#include <set>
#include <numeric>
using namespace std;

int main() {
	int caseNumber;
	cin >> caseNumber;

	int rowNumber;
	int i, j;
	int a, b, c, d, sum;
	set<int> numbers;
	for (i = 0; i < caseNumber; ++i) {
		numbers.clear(); // Initialize
		cin >> rowNumber;
		for (j = 0; j < 4; ++j) {
			cin >> a >> b >> c >> d;
			if (j == (rowNumber - 1)) {
				numbers.insert(a);
				numbers.insert(b);
				numbers.insert(c);
				numbers.insert(d);
				sum = a + b + c + d;
			}
		}

		cin >> rowNumber;
		for (j = 0; j < 4; ++j) {
			cin >> a >> b >> c >> d;
			if (j == (rowNumber - 1)) {
				numbers.insert(a);
				numbers.insert(b);
				numbers.insert(c);
				numbers.insert(d);
				sum = sum + a + b + c + d;
			}
		}

		if (numbers.size() == 8) {
			cout << "Case #"<< i + 1 << ": Volunteer cheated!" << endl;
		} else if (numbers.size() == 7) {
			cout << "Case #"<< i + 1 << ": " << sum - accumulate(numbers.begin(), numbers.end(), 0) << endl;
		} else {
			cout << "Case #"<< i + 1 << ": Bad magician!" << endl;
		}
	}

	return 0;
}
