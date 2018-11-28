#include <iostream>
#include <algorithm>
#include <map>
#include <string>
#include <fstream>
using namespace std;

bool
checkPancakeXray(string pStack) {

	for (unsigned int i = 0; i < pStack.length();i++)
		if (pStack[i] == '-')
			return false;

	return true;
}

bool
checkAllBlankXray(string pStack) {
	for (unsigned int i = 0; i < pStack.length();i++) {
		if (pStack[i] == '+')
			return false;
	}
	return true;
}

void flip(string& pStack, unsigned int pos) {
	for (unsigned int i = 0; i < pos;i++) {
		if (pStack[i] == '+')
			pStack[i] = '-';
		else
			pStack[i] = '+';
	}
}



int main() {

	int testNum;
	string pancakeStack;
	ofstream outFileStream;
	int flipCount = 0;
	outFileStream.open("output.txt");

	unsigned int ch=0;

	cin >> testNum;

	for (int test = 1; test <= testNum; test++) {
		flipCount = 0;
		ch = 0;
		cout << "Case #" << test << ":" << " ";
		outFileStream << "Case #" << test << ":" << " ";
		cin >> pancakeStack;
		//cout << "original pancake stack:" << pancakeStack << endl;

		if (checkPancakeXray(pancakeStack)) {
			cout << "0" << endl;
			outFileStream << "0" << endl;
			continue;
		}
		else {
			// corner
			if (pancakeStack.length() == 1) {				
					cout << "1" << endl;
					outFileStream << "1" << endl;
					continue;
			}

			//corner
			if (checkAllBlankXray(pancakeStack)) {
				cout << "1" << endl;
				outFileStream << "1" << endl;
				continue;
			}

			while(ch < pancakeStack.length()) {
				if (pancakeStack[ch] == pancakeStack[ch + 1]) {
					ch++;
					continue;
				} else {
					//cout << "ch:" << ch << endl;
					flipCount++;					
					flip(pancakeStack, ch + 1);
					//cout << "reversed string:" << pancakeStack << endl;
					if (checkPancakeXray(pancakeStack))
						break;
					ch++;
					continue;		

				}
			}
			//cout << "final stack:" << pancakeStack << endl;
			//cout << "flip count = " << flipCount << endl;
			cout << flipCount << endl;
			outFileStream << flipCount << endl;


		}
	}
}