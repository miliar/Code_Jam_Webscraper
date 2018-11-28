#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

bool isHappy(const string& inString) {
	for (auto c : inString) {
		if (c != '+') {
			return false;
		}
	}
	return true;
}

int main()
{
	int numCases = 0;
	cin >> numCases;

	string line;
	getline(cin, line);

	for (int i = 1; i <= numCases; ++i) {
		string pancakes;
		int flips = 0;
		getline(cin, pancakes);

		while (!isHappy(pancakes)) {
			string::size_type numToFlip = 1;
			while (numToFlip < pancakes.length() && pancakes[numToFlip] == pancakes.front()) {
				++numToFlip;
			}

			string flipped = pancakes.substr(0, numToFlip);
			for (string::size_type j = 0; j < flipped.length(); ++j) {
				if (flipped[j] == '+') {
					flipped[j] = '-';
				}
				else {
					flipped[j] = '+';
				}
			}

			if (flipped.length() != pancakes.length()) {
				pancakes = flipped + pancakes.substr(flipped.length(), pancakes.length() - flipped.length());
			}
			else {
				pancakes = flipped;
			}

			++flips;
		}
		cout << "Case #" << i << ": " << flips << endl;
	}

    return 0;
}

