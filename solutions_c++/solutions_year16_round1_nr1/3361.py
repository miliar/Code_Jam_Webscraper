#include <iostream>
#include <string>

using namespace std;

int main() {
	unsigned short cases = 0;
	cin >> cases;

	for(unsigned short c = 1; c <= cases; c++) {
		cout << "Case #" << c << ": ";
		
		string input;
		cin >> input;
		
		string lastWord;
		lastWord += input.at(0);
		for(unsigned short i = 1; i < input.length(); i++) {
			if(input.at(i) >= lastWord.at(0)) {
				lastWord.insert(0, string(1, input.at(i)));
			} else {
				lastWord.insert(lastWord.end(), input.at(i));
			}
		}
		
		cout << lastWord << endl;
	}

	return 0;
}
