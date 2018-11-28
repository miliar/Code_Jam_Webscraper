#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <set>
using namespace std;

vector<int> getcards() {
	vector<int> ret;
	int row;
	cin >> row;
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			int tmp;
			cin >> tmp;
			if (i == row - 1) {
				ret.push_back(tmp);
			}
		}
	}
	return ret;
}

int main(int argc, char** argv) {
	int numcase;
	cin >> numcase;
	for (int mastercounter = 0; mastercounter < numcase; mastercounter++) {
		vector<int> case1, case2, answer;
		case1 = getcards();
		case2 = getcards();
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (case1[i] == case2[j]) {
					answer.push_back(case1[i]);
				}
			}
		}
		cout << "Case #" << mastercounter + 1 << ": ";
		if (answer.size() == 1) {
			cout << answer[0] << "\n";
		} else if (answer.size() > 1) {
			cout << "Bad magician!" << "\n";
		} else if (answer.size() == 0) {
			cout << "Volunteer cheated!" << "\n";;
		}
	}
}