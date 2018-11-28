#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;

vector<pair<char, int> > letterToDigit;
string name[] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };

void init() {
	letterToDigit.push_back(make_pair<char, int>('G', 8));
	letterToDigit.push_back(make_pair<char, int>('U', 4));
	letterToDigit.push_back(make_pair<char, int>('W', 2));
	letterToDigit.push_back(make_pair<char, int>('X', 6));
	letterToDigit.push_back(make_pair<char, int>('Z', 0));
	letterToDigit.push_back(make_pair<char, int>('F', 5));
	letterToDigit.push_back(make_pair<char, int>('H', 3));
	letterToDigit.push_back(make_pair<char, int>('I', 9));
	letterToDigit.push_back(make_pair<char, int>('O', 1));
	letterToDigit.push_back(make_pair<char, int>('S', 7));
}

int main() {
	init();
	int cases;
	cin >> cases;
	for (int caseCounter = 1; caseCounter <= cases; caseCounter++) {
		string letters;
		cin >> letters;

		map<char, int> count;
		for (int i = 0; i < letters.length(); i++) {
			count[letters[i]]++;
		}

		int sol[10];

		for (int p = 0; p < letterToDigit.size(); p++) {
			char letter = letterToDigit[p].first;
			int digit = letterToDigit[p].second;
			int cnt = count[letter];
			sol[digit] = cnt;
			for (int i = 0; i < name[digit].length(); i++) {
				char ch = name[digit][i];
				count[ch] -= cnt;
			}
		}

		cout << "Case #" << caseCounter << ": ";
		for (int i = 0; i < 10; i++) {
			for (int j = 0; j < sol[i]; j++)
				cout << i;
		}
		cout << endl;
	}
	return 0;
}
