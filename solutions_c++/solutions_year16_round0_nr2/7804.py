#include <iostream>
#include <string>
using namespace std;

int main() {

	int numberOfInputs;
	cin >> numberOfInputs;

	string pancakes;

	int numberOfFlips = 0;

	for (int input = 1; input <= numberOfInputs; input++) {
		cin >> pancakes;

		numberOfFlips = 0;

		for (int i = 0; i < pancakes.length(); i++) {
			if (i < pancakes.length() - 1) {
				if (pancakes.at(i) != pancakes.at(i + 1)) {
					numberOfFlips++;
				}
			}
			else {
				if (pancakes.at(i) == '-') {
					numberOfFlips++;
				}
			}
		}

		cout << "Case #" << input << ": " << numberOfFlips << endl;
	}

	return 0;
}