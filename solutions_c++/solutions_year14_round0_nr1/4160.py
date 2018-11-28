#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>

using namespace std;

vector<int> getRow() {
	int rowNr, trash;
	cin >> rowNr;
	vector<int> row(4);
	for (int i = 0; i < 16; i++) {
		if (i / 4 + 1 == rowNr)
			cin >> row[i % 4];
		else
			cin >> trash;
	}
	return row;
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		auto row1 = getRow();
		auto row2 = getRow();
		int answerCount = 0;
		int answer = 0;
		for (int i = 0; i < 4; i++) {
			auto it = find(row2.begin(), row2.end(), row1[i]);
			if (it != row2.end()) {
				answerCount++;
				answer = row1[i];
			}
		}
		switch (answerCount) {
			case 0:
				printf("Case #%d: Volunteer cheated!\n", t);
				break;
			case 1:
				printf("Case #%d: %d\n", t, answer);
				break;
			default:
				printf("Case #%d: Bad magician!\n", t);
		}
	}
	return 0;
}