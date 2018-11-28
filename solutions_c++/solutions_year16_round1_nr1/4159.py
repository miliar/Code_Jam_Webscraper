#include <iostream>
#include <string>
using namespace std;

string lastWord(string s) {
	int l = s.length();
	string lword = "";
	lword += s[0];
	for(int i = 1; i < l; i++) {
		if(s[i] >= lword[0]) {
			lword = s[i] + lword;
		} else {
			lword += s[i];
		}
	}
	return lword;
}

int main(void) {
	int T;
	string S;
	cin >> T;
	for(int i = 0; i < T; i++) {
		cin >> S;
		cout << "Case #" <<  i+1 << ": " << lastWord(S) << endl;
	}
	return 0;
}