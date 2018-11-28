//============================================================================
// Name        : codejam-A.cpp
// Author      : myscloud
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> digit(10, 0);
vector<int> alpha(26, 0);

void decrease(string numStr, int num, char key) {
	int count = alpha[key - 'A'];
	digit[num] = count;
	for(int i = 0; i < numStr.length(); i++) {
		alpha[numStr[i] - 'A'] -= count;
	}
}

int main() {
	int test;
	string digitString;
	cin >> test;
	for(int t = 1; t <= test; t++) {
		cin >> digitString;
		for(int i = 0; i < digit.size(); i++) digit[i] = 0;
		for(int i = 0; i < alpha.size(); i++) alpha[i] = 0;

		for(int i = 0; i < digitString.length(); i++) {
			alpha[digitString[i] - 'A']++;
		}

		decrease("ZERO", 0, 'Z');
		decrease("SIX", 6, 'X');
		decrease("EIGHT", 8, 'G');
		decrease("TWO", 2, 'W');

		decrease("SEVEN", 7, 'S');

		decrease("FIVE", 5, 'V');

		decrease("FOUR", 4, 'F');

		decrease("THREE", 3, 'T');
		decrease("NINE", 9, 'I');
		decrease("ONE", 1, 'O');


		cout << "Case #" << t << ": ";
		for(int i = 0; i < 10; i++){
			int count = digit[i];
			if(count > 0){
				for(int j = 0; j < count; j++){
					cout << i;
				}
			}
		}
		cout << endl;
	}
	return 0;
}
