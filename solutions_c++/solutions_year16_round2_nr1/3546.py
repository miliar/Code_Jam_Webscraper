#include <iostream>
#include <string>
using namespace std;

string getPhoneNum(string &, string[], int[], int, string);

int main() {
	int T;
	string s;
	int letterCount[26];
	string numToWord[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
	cin >> T;
	for(int count = 0; count < T; ++count) {
		cin >> s;
		for(int i = 0; i < 26; ++i) {
			letterCount[i] = 0;
		}

		for(int i = 0; i < s.length(); ++i) {
			letterCount[s[i] - 'A'] = letterCount[s[i] - 'A'] + 1;
		}

		cout << "Case #" << count + 1 << ": " << getPhoneNum(s, numToWord, letterCount, s.length(), "") << endl;

	}

	return 0;
}

string getPhoneNum(string & s, string numToWord[], int letterCount[], int lettersLeft, string numSoFar) {
	if(lettersLeft == 0)
		return numSoFar;

	for(int i = 0; i < 10; ++i) {
		for(int j = 0; j < 10; ++j) {
			string word = numToWord[j];
			int k;
			for(k = 0; k < word.length(); ++k) {
				if(letterCount[word[k] - 'A'] <= 0)
					break;

				letterCount[word[k] - 'A'] = letterCount[word[k] - 'A'] - 1;
			}

			if(k == word.length()) {
				char digit = j + '0';
				string result = getPhoneNum(s, numToWord, letterCount, lettersLeft - word.length(), numSoFar + digit);
				if(result != "") {
					return result;
				}

				else {
					for(k = 0; k < word.length(); ++k) {
						letterCount[word[k] - 'A'] = letterCount[word[k] - 'A'] + 1;
					}
				}
			}

			else {
				for(int x = 0; x < k; ++x) {
						letterCount[word[x] - 'A'] = letterCount[word[x] - 'A'] + 1;
				}
			}
		}
	}

	return "";
}