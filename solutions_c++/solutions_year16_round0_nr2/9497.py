//============================================================================
// Name        : Revenge_of_the_Pancakes.cpp
// Author      : Mohammed Essam
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <string.h>
using namespace std;

int main() {
	int T = 0, count = 0;
	ifstream in("B-large.in");
	ofstream out("B-large-out.txt");
	in >> T;
	string *panStrings = new string[T];
	string *popStrings= new string[T];
	for (int i = 0; i < T; i++) {
		in >> panStrings[i];
		for (int c = (panStrings[i].length())-1 ; c >= 0; c--) {
			popStrings[i] +=panStrings[i].at(c);
		}
	}
	for (int z = 0; z < T; z++) {
		for (int i = 0; i < popStrings[z].length(); i++) {
			if (popStrings[z].at(i) == '-') {
				panStrings[z].at(i) = '+';
				for (int j = i + 1; j < popStrings[z].length(); j++) {
					if (popStrings[z].at(j) == '-') {
						popStrings[z].at(j) = '+';
					} else {
						popStrings[z].at(j) = '-';
					}
				}
				count++;
			} else {
				continue;
			}
		}
		out << "Case #" << z + 1 << ": " << count << endl;
		count = 0;
	}

}
