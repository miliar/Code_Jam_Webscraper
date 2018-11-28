#include <iostream>
#include <vector>
using namespace std;

int main() {
	int cases;
	cin >> cases;
	for (int caseCounter = 1; caseCounter <= cases; caseCounter++) {
		string letters;
		cin >> letters;
		int lastWritten = letters.length();
		bool seen['Z' + 1] = { false };
		for (int i = 0; i < lastWritten; i++)
			seen[letters[i]] = true;
		vector<char> sol;
		for (char ch = 'Z'; ch >= 'A' && lastWritten > 0; ch--)
			if (seen[ch]) {
				for (int i = lastWritten - 1; i >= 0; i--) {
					if (letters[i] == ch) {
						lastWritten = i;
						letters[i] = ' ';
						sol.push_back(ch);
					}
				}
			}

		cout << "Case #" << caseCounter << ": ";
		for (int i = 0; i < sol.size(); i++)
			cout << sol[i];
		for (int i = 0; i < letters.length(); i++)
			if (letters[i] != ' ')
				cout << letters[i];
		cout << endl;

	}

	return 0;
}
