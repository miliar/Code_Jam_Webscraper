#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <iterator>
using namespace std;

void lastWord(const string& s) {
	string lastWord;
	lastWord.push_back(s[0]);
	if (s.length() > 1) {
		for (int i = 1; i < s.length(); i++) {
			if (s[i] >= lastWord[0]) {
				lastWord.insert(lastWord.begin(), s[i]);
			}
			else {
				lastWord.push_back(s[i]);
			}
		}
	}
	cout << lastWord;
}

int main() {
	size_t cases;
	ifstream ifs("Text.txt");
	if (!ifs) {
		cout << "can't open the file" << endl;
		exit(1);
	}
	ifs >> cases;
	for (size_t i = 1; i <= cases; i++) {
		string word;
		ifs >> word;
		cout << "Case #" << i << ": ";
		lastWord(word);
		cout << endl;
	}
}