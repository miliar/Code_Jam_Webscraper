#include <iostream>
#include <bitset>

using namespace std;

int countSheep(int x) {
	bitset<10> digits;
	if (x == 0) {
		return -1;
	}
	int xc = x;
	while(true) {
		int c = x;
		while (c != 0) {
			digits[c % 10] = true;
			c = c / 10;
		}
		if (digits.all()) {
			break;
		}
		x += xc;
	}
	return x;
}

int main() {
	int n;
	cin >> n;
	for (int i = 0; i < n; ++i) {
		int ni;
		cin >> ni;
		int c = countSheep(ni);
		cout << "Case #" << i+1 << ":";
		if (c == -1) {
			cout << " INSOMNIA";
		} else {
			cout << " " << c;
		}
		cout << "\n";
	}
	return 0;
}