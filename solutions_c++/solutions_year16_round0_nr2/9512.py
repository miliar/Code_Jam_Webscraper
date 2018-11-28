#include <iostream>
#include <string>
using namespace std;

int Flip(string s) {
	bool stillMinus = false;
	int count = 0;
	for (int i = 0; i < s.size(); i++) {
		if (s[i] == '-') {
			if (!stillMinus) {
				stillMinus = true;
				count++;
			}
		}
		if (s[i] == '+') {
			stillMinus = false;
		}
	}
	count = count << 1;
	if (s[0] == '-') count--;
	return count;
}

void main() {
	int testNum;
	int number;
	cin >> testNum;

	bool flags[10];
	
	string s;
	int step = 0;
	for (int i = 0; i < testNum; i++) {
		for (int i = 0; i < 10; i++) {
			flags[i] = false;
		}
		cin >> s;
		cout << "Case #" << i + 1 << ": " << Flip(s) << "\n";
	}
}