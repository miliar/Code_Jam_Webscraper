//============================================================================
// Name        : Q1_A.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

int main() {
	int T,S;
	string shys;
	cin >> T;
	for (int i = 1 ; i <= T; i++){
		cin >> S;
		cin >> shys;
		int accumulator = shys[0] - '0';
		int toAdd = 0;
		for (int j = 1 ; j < S+1 ; j++){
			//cout << "accumulator" << accumulator << endl;
			if (j > accumulator){
				toAdd += (j - accumulator);
				accumulator += (j - accumulator);
				//cout << "toAD" << toAdd << endl;
			}
			accumulator += shys[j] - '0';
		}
		cout << "Case #" << i << ": " << toAdd << endl;
	}
}
