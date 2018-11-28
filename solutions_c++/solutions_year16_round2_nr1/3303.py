#include <iostream>
#include <string>


using namespace std;

int RemoveDigit(int* counts, char id, const string& digit) {
	auto num = counts[id - 'A'];
	for (auto c : digit) {
		counts[c - 'A'] -= num;
	}
	return num;
}

int main()
{
	int numCases = 0;
	cin >> numCases;

	string line;
	getline(cin, line);

	for (auto i = 1; i <= numCases; ++i) {
		getline(cin, line);
		int counts['Z' - 'A' + 1] = { 0 };
		int digits[10] = { 0 };
		for (auto c : line) {
			counts[c - 'A']++;
		}

		digits[0] = RemoveDigit(counts, 'Z', "ZERO");
		digits[2] = RemoveDigit(counts, 'W', "TWO");
		digits[4] = RemoveDigit(counts, 'U', "FOUR");
		digits[6] = RemoveDigit(counts, 'X', "SIX");
		digits[1] = RemoveDigit(counts, 'O', "ONE");
		digits[5] = RemoveDigit(counts, 'F', "FIVE");
		digits[7] = RemoveDigit(counts, 'S', "SEVEN");
		digits[8] = RemoveDigit(counts, 'G', "EIGHT");
		digits[3] = RemoveDigit(counts, 'T', "THREE");
		digits[9] = RemoveDigit(counts, 'E', "NINE");

		cout << "Case #" << i << ": ";
		cerr << "Case #" << i << ": ";
		for (auto j = 0; j < 10; ++j) {
			for (auto k = 0; k < digits[j]; ++k) {
				cout << j;
				cerr << j;
			}
		}
		cout << endl;
		cerr << endl;
	}

    return 0;
}

