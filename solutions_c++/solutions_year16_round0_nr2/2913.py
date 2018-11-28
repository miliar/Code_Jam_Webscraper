#include <iostream>
#include <cmath>
#include <vector>
#include <iomanip>
#include <sstream>
using namespace std;

bool allDigits(bool* nums, int size) {
	for (int i = 0; i < size; i++) {
		if (!nums[i]) {
			return false;
		}
	}
	return true;
}

void flip(bool* pancakes, int end) {
	bool temp;
	for (int i = 0; i < (end + 1)/2; i++) {
		//cout << "HI" << endl;
		temp = !pancakes[i];
		pancakes[i] = !pancakes[end - i];
		pancakes[end - i] = temp;
		//cout << "HI" << endl;
	}
	if (end % 2 == 0) {
		pancakes[end/2] = !pancakes[end/2];
	}
}

int findMinFlips(bool* pancakes, int size) {
	int idx, count = 0;
	/*for (int i = 0; i < size; i++) cout << pancakes[i] << " ";
	cout << endl;*/
	while (!allDigits(pancakes, size)) {
		idx = 0;
		while (idx < size - 1 && pancakes[idx] == pancakes[idx+1]) idx++;
		flip(pancakes, idx);
		count++;
		/*cout << "Flip " << count << " at " << idx << endl;
		for (int i = 0; i < size; i++) cout << pancakes[i] << " ";
		cout << endl << endl;*/
	}
	return count;
}

int main() {
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		string line;
		cin >> line;
		bool* pc = new bool[line.size()];
		//cout << line << endl;
		for (int j = 0; j < line.size(); j++) {
			if (line.at(j) == '+') {
				pc[j] = 1;
			} else {
				pc[j] = 0;
			}
		}
		/*for (int i = 0; i < line.size(); i++) cout << pc[i] << " ";
		cout << endl;*/
		int min = findMinFlips(pc, line.size());
		delete pc;
		pc = 0;
		cout << "Case #" << i << ": " << min << endl;
	}

	return 0;
}