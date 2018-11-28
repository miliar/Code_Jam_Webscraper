#include <iostream>
//#include <istream>
#include <fstream>
#include <string>

using namespace std;

void main()
{
	int T;

	ifstream file("input.txt");
	ofstream output("output.txt");
	file >> T;
	int nT = 0;
	while (T--) {
		nT++;
		string s;
		file >> s;

		int lastNegativePos = -1;
		for (int i = (int)s.length() - 1; i >= 0; i--) {
			if (s[i] == '-') {
				lastNegativePos = i;
				break;
			}
		}
		if (lastNegativePos < 0) {
			output << "Case #" << nT << ": " << 0 << endl;
		}
		else {
			int change = 0;
			for (int i = 0; i < lastNegativePos; i++) {
				if (s[i] != s[i + 1]) {
					change++;
				}
			}
			int nFlips = change + 1;
			output << "Case #" << nT << ": " << nFlips << endl;
		}
	}

}
/*

5
-
-+
+-
+++
--+-

*/