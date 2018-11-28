#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<sstream>
#include<vector>
#include<stack>

using namespace std;

bool isAllHappy(vector<bool> pancakes) {
	for (int i = 0; i < pancakes.size(); i++) {
		if (!pancakes[i]) {
			return false;
		}
	}
	return true;
}

void maneuver(vector<bool> &pancakes, int index) {
	stack<bool> temp;
	for (int j = 0; j <= index; j++) {
		temp.push(pancakes[j]);
	}
	for (int j = 0; j <= index; j++) {
		pancakes[j] = !temp.top();
		temp.pop();
	}
}

int main() {
	int T; // number of tests
	scanf("%d", &T);
	string line;
	getline(cin, line);

	vector<int> result;

	for (int i = 0; i < T; i++) {
		vector<bool> pancakes;

		getline(cin, line);		
		for (int j = 0; j < line.length(); j++) {
			pancakes.push_back(line[j] == '+' ? true : false);
		}

		int count = 0;
		while (! isAllHappy(pancakes)) {
			int lastBlankIndex = -1;
			for (int j = pancakes.size()-1; j >= 0; j--) {
				if (!pancakes[j]) {
					lastBlankIndex = j;
					break;
				}
			}

			if (!pancakes[0]) {
				maneuver(pancakes, lastBlankIndex);
				count++;
			} else {
				int k = 0;
				for (k = 0; k < lastBlankIndex; k++) {
					if (!pancakes[k]) {
						break;
					}
				}
				maneuver(pancakes, k-1);
				count++;
			}
		}

		result.push_back(count);
	}

	for (int i = 0; i < T; i++) {
		cout << "Case #" << i+1 << ": " << result[i] << endl;
	}
}


