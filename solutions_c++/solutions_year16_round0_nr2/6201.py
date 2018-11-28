#include <math.h>
#include <iostream>
#include <string>

using namespace std;

string flip(string n, int end) {
	for (int i = 0; i <= end; i++) {
		if (n[i] == '-')
			n[i] = '+';
		else
			n[i] = '-';
	}
	return n;
}

int main() {
	int numberOfCases, i = 0;
	string n;

	cin >> numberOfCases;

	while (cin >> n) {
		int nflips = 0;
		int scanned = n.length();

		for (int i = scanned; i >= 0; i--) {
			if (n[i] == '-') {
				n = flip(n, i);
				nflips++;
			}
		}

		cout << "Case #" << ++i << ": " << nflips << endl;
	}
}
