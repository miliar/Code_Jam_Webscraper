#include <iostream>
#include <string>

using namespace std;

string lastWord(string letters) {
	int n = letters.length();
	string lastword = "";
	if (n > 0) {
		char start = letters[0];
		char end = letters[0];
		lastword += letters[0];
		for(int i=1; i<n; i++) {
			char letter = letters[i];
			if (letter >= start) {
				lastword = letter + lastword;
				start = letter;
			}
			else {
				lastword = lastword+letter;
				end = letter;
			}
		}
	}
	return lastword;
}

int main() {
	int cases;
	cin>>cases;
	int index = 1;
	while(index <= cases) {
		string input;
		cin>>input;
		cout<<"Case #"<<index<<": "<<lastWord(input)<<endl;
		index++;
	}
	return 0;
}
