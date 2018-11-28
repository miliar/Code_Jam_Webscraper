#include "stdafx.h"
#include <iostream>
#include <iomanip>
#include <math.h>
#include <string>
#include <sstream>
#include <fstream>

using namespace std;

bool isConsonant(char ch) {
	if(ch == 'a') {
		return false;
	}
	else if(ch == 'e') {
		return false;
	}
	else if(ch == 'i') {
		return false;
	}
	else if(ch == 'o') {
		return false;
	}
	else if(ch == 'u') {
		return false;
	}
	return true;
}

int main(int argc, char* argv[])
{
    ifstream sourceFile("./A1.in");
    ofstream output("./output.txt");

    int T;
    sourceFile >> T;

	for(int z = 0; z < T; z++) {
		string s;
		int n;

		sourceFile >> s;
		sourceFile >> n;

		int length = s.length();
		int result = 0;

		for(int i = length; i >= n; i--) {
			for(int j = 0; j < length - i + 1; j++) {
				int cc = 0;
				for(int k = j; k < j + i; k++) {
					if(isConsonant(s.at(k))) {
						cc++;
						if(cc >= n) {
							result++;
							break;
						}
					}
					else {
						cc = 0;
					}
				}
			}
		}

		output << "Case #" << z + 1 << ": " << result << endl;	
	}

    return 0;
}
