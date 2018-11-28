#include <iostream>
#include <string>
using namespace std;
string output(string S) {
	string lastWord;
	lastWord.push_back(S.at(0));
	for (int i = 1; i < S.length(); i++) {
		if (S.at(i) >= lastWord.at(0)) {
			reverse(lastWord.begin(), lastWord.end());
			lastWord.push_back(S.at(i));
			reverse(lastWord.begin(), lastWord.end());
		}
		else
			lastWord.push_back(S.at(i));
	}
	return lastWord;
}
int main(void) {
	int T;
	cin >> T;
	string S;
	for (int i = 0; i < T; i++) {
		cin >> S;
		string lastWord = output(S);
		cout << "Case #" << i + 1 << ": " << lastWord << endl;
	}
	return 0;
}