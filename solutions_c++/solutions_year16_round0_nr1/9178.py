#include <iostream>
#include <vector>
#include <string>
#include <fstream>
using namespace std;

int CountingSheep(int n) {
	vector<int> digits;
	int mult = 1;
	while (digits.size() < 10) {
		int result = mult * n;
		while (result != 0) {
			int digit = result % 10;
			for (size_t i = 0; i < digits.size(); i++) {
				if (digit == digits[i]) {
					digit = -1;
				}
			}
			if (digit != -1) {
				digits.push_back(digit);
			}
			result = result / 10;
		}
		mult = mult + 1;
	}
	return (mult-1)* n;
}

int main() {
	int cases;
	ifstream ifs("Text.txt");
	if (!ifs) {
		cout << "can't open the file" << endl;
		exit(1);
	}
	ifs >> cases;
	for (size_t i = 1; i <= cases; i++) {
		int n;
		ifs >> n;
		if (n == 0) {
			cout << "Case #" << i << ": INSOMNIA" << endl;
		}
		else {
			cout << "Case #" << i << ": " << CountingSheep(n) << endl;
		}
	}
}