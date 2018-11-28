#include <iostream>

#include <string>

using namespace std;


int getMinFlips(string s) {
	char start = s[0];
	int flipCount = 0;
	for(int i = 1; i < s.size(); ++i) {
		if(s[i] != start) {
			flipCount ++;
			start = s[i];
		}
	}
	if(s[s.size()-1] == '-') {
		return flipCount + 1;
	}
	return flipCount;
}


int main () {
	int noTests;
	cin >> noTests;

	for (int i = 1; i <= noTests; ++i) {
		string s;
		cin >> s;
		cout << "Case #" << i << ": " << getMinFlips(s) << '\n';
	}
}