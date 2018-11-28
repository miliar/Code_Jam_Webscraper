
#include <iostream>
#include <string>

using namespace std;

int runTestCase();

int main() {

	int t = 0;
	cin >> t;

	for (int i = 0; i < t; i++) {
		cout << "Case #" << i + 1 << ": " << runTestCase() << endl;
	}
}

int runTestCase() {
	
	string pancakes;
	cin >> pancakes;

	int flips = 0;

	for (int i = 0; i < pancakes.size() - 1; i++) {
		if (pancakes[i] != pancakes[i + 1]) {
			flips++;
		}
	}

	if (pancakes[pancakes.size() - 1] == '-') {
		flips++;
	}

	return flips;
}