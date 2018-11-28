#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>
#include <stack>
using namespace std;

int main () {

	ifstream inFile;
	ofstream outFile;

	inFile.open("B-large.in");
	outFile.open("problemBLargeOutput.txt");

	int T = 0;
	inFile>>T;


	string str;
	for (int i=1; i<=T; i++) {
		int numberOfFlips = 0;
		inFile>>str;
		char current = str[0];
		for (int j=1; j<str.length(); j++) {
			if (current != str[j]) {
				numberOfFlips++;
				current = str[j];
			}
		}
		if (current == '-') {
			numberOfFlips++;
		}
		outFile<<"Case #"<<i<<": "<<numberOfFlips<<endl;
	}


	inFile.close();
	outFile.close();

	return 0;
}
