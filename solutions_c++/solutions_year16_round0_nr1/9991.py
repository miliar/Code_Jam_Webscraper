#include <iostream>
#include <fstream>
#include <string>
using namespace std;





int main() {
	int testCases;
	int number;
	bool numbers[10];
	

	ifstream fin;
	fin.open("a.in");
	ofstream fout;
	fout.open("a.out");

	fin >> testCases;
	for (int i = 0; i < testCases; i++) {
		fin >> number;
		if (number == 0) {
			fout << "Case #" << i + 1 << ": INSOMNIA";
			if (i + 1 < testCases)
				fout << endl;
			continue;
		}

		for (int j = 0; j < 10; j++) {
			numbers[j] = false;
		}

		string s;

		for (int multiplier = 1; !(numbers[0] && numbers[1] && numbers[2] && numbers[3] && numbers[4] && numbers[5] && numbers[6] && numbers[7] && numbers[8] && numbers[9]); multiplier++) {
			s = to_string(number * multiplier);

			for (int j = 0; j < s.length(); j++) {
				int c = (int)(s[j]) - '0';
				numbers[c] = true;
			}
		}

		fout << "Case #" << i + 1 << ": " << s;
		if (i + 1 < testCases)
			fout << endl;
	}

	fin.close();
	fout.close();

	return 0;
}