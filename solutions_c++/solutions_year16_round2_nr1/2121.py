
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

uint32_t counters[256];
vector<int> digitCounter;

int main()
{
	// Read number of testcases
	int numTestcases, number;
	cin >> numTestcases;

	for (int i = 1; i <= numTestcases; i++) {
		// Parse number as string
		string phoneNumber;
		cin >> phoneNumber;

		// Initialize char counters
		for (int k = 0; k < 255; k++) counters[k] = 0;
		for (int k = 0; k < phoneNumber.length(); k++) counters[phoneNumber.at(k)]++;
		digitCounter.resize(10);
		for (int k = 0; k < 10; k++) digitCounter[k] = 0;

		// Add 0
		while (counters['Z'] > 0) {
			digitCounter[0]++;
			counters['Z']--;
			counters['E']--;
			counters['R']--;
			counters['O']--;
		}

		// Add 2
		while (counters['W'] > 0) {
			digitCounter[2]++;
			counters['T']--;
			counters['W']--;
			counters['O']--;
		}

		// Add 4
		while (counters['U'] > 0) {
			digitCounter[4]++;
			counters['F']--;
			counters['O']--;
			counters['U']--;
			counters['R']--;
		}

		// Add 6
		while (counters['X'] > 0) {
			digitCounter[6]++;
			counters['S']--;
			counters['I']--;
			counters['X']--;
		}

		// Add 8
		while (counters['G'] > 0) {
			digitCounter[8]++;
			counters['E']--;
			counters['I']--;
			counters['G']--;
			counters['H']--;
			counters['T']--;
		}

		// Add 1
		while (counters['O'] > 0) {
			digitCounter[1]++;
			counters['O']--;
			counters['N']--;
			counters['E']--;
		}

		// Add 3
		while (counters['T'] > 0) {
			digitCounter[3]++;
			counters['T']--;
			counters['H']--;
			counters['R']--;
			counters['E']--;
			counters['E']--;
		}

		// Add 5
		while (counters['F'] > 0) {
			digitCounter[5]++;
			counters['F']--;
			counters['I']--;
			counters['V']--;
			counters['E']--;
		}

		// Add 7
		while (counters['V'] > 0) {
			digitCounter[7]++;
			counters['S']--;
			counters['E']--;
			counters['V']--;
			counters['E']--;
			counters['N']--;
		}

		// Add 9
		while (counters['N'] > 0) {
			digitCounter[9]++;
			counters['N']--;
			counters['I']--;
			counters['N']--;
			counters['E']--;
		}

		cout << "Case #" << i << ": ";
		for (int k = 0; k < 10; k++) {
			for (int m = 0; m < digitCounter[k]; m++) {
				cout << k;
			}
		}
		cout << endl;

		//if (hasBeenSeen == true) cout << "Case #" << i << ": " << lastNum << (char)(0x0D) << endl;
		//else cout << "Case #" << i << ": INSOMNIA" << (char)(0x0D) << endl;
	}

}