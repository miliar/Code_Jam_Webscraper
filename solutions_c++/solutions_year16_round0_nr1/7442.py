#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

bool checknumbers(int n, vector<bool> &seen) {
	while (n / 10 > 0) {
		for (int i = 0; i < 10; ++i) {
			int rest = n % 10;
			if (i == rest) seen[i] = true;
			if (i == n) seen[i] = true;
		}
		n /= 10;
	}
	for (int i = 0; i < 10; ++i) {
		if (i == n) seen[i] = true;
	}
	for (int i = 0; i < 10; ++i) {
		if (!seen[i]) return false;
	}
	return true;
}

int main() {
	int n;
	cin >> n;

	ofstream output;
	output.open("output.txt");


	for (int i = 0; i < n; ++i) {
		int number, num;
		cin >> number;
		bool asleep, exitCondition;
		asleep = exitCondition = false;
		vector<bool> seen(10);
		for (int j = 0; j < 10; ++j) seen[j] = false;

		for (int j = 1; !asleep && !exitCondition; ++j) {
			if (number == 0) exitCondition = true;
			else {
				num = number * j;
				asleep = checknumbers(num, seen);
			}
		}

		output << "Case #" << i + 1 << ": ";
		if (!asleep) output << "INSOMNIA" << endl;
		else output << num << endl;

	}
	output.close();
	return 0;
	
}