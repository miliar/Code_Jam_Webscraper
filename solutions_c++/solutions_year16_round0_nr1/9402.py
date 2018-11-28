#include <iostream>
using namespace std;


bool CheckFinish(bool *flags) {
	for (int i = 0; i < 10; i++) {
		if (!flags[i]) return false;
	}
	return true;
}

void TestNum(int number, int testNo, bool *flags) {
	if (number == 0) {
		cout << "Case #" << testNo << ": " << "INSOMNIA";
		return;
	}
	int cur = 0, temp = 0;
	while (!CheckFinish(flags)) {
		cur += number;
		temp = cur;
		while (temp > 0) {
			flags[temp % 10] = true;
			temp = temp / 10;
		}
	}
	cout << "Case #" << testNo << ": " << cur;
}

void main() {
	int testNum;
	int number;
	cin >> testNum;

	bool flags[10];
	
	
	int step = 0;
	for (int i = 0; i < testNum; i++) {
		for (int i = 0; i < 10; i++) {
			flags[i] = false;
		}
		cin >> number;
		TestNum(number, i + 1, flags);
		if (i != testNum - 1) cout << "\n";
	}
}