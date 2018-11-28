// CountingSheep.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text

//
#include <string>

string findLastSheep(int seed);

void main() {
  int n, v;
  cin >> n;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= n; ++i) {
    cin >> v;  
    cout << "Case #" << i << ": " << findLastSheep(v) << endl;
  }
}

string findLastSheep(int seed) {
	if (seed == 0) {
		return "INSOMNIA";
	}
	else {
		bool flag[10];
		for (int i = 0; i <= 9; ++i) {
			flag[i] = false;
		}
		int ctrFlag = 0;
		int ctrSheep = 0;
		int lastSheep;

		string strDigit;
		while (ctrFlag<10) {
			lastSheep = ++ctrSheep * seed;
			strDigit = to_string((_ULonglong)lastSheep);
			for (int i = 0; i < strDigit.length(); ++i) {
				int digit = strDigit[i]-'0';
				if (flag[digit] == false) {
					flag[digit] = true;
					ctrFlag++;
				}
			}
		}
		return to_string((_ULonglong)lastSheep);
	}
}