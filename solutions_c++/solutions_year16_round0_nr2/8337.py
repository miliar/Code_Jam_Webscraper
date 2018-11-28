// RevengeOfThePancakes.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text

//
#include <string>

int countPancakeStackFlipMove(string sPancakeStack);

void main() {
  int n;
  string v;
  cin >> n;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= n; ++i) {
    cin >> v;  
    cout << "Case #" << i << ": " << countPancakeStackFlipMove(v) << endl;
  }
}

int countPancakeStackFlipMove(string sPancakeStack) {
	if (sPancakeStack.length() == 0) {
		return 0;
	}
	else {
		int lastPancakeIdx = sPancakeStack.length() - 1;
		
		char pancakeSlice = sPancakeStack[lastPancakeIdx];
		int ctrStackDiff = 0;
		if (pancakeSlice == '-') {
			ctrStackDiff = 1;
		}

		for (int i = lastPancakeIdx-1; i >= 0; --i) {
			char pancakeSliceNext = sPancakeStack[i];
			if (pancakeSliceNext != pancakeSlice) {
				ctrStackDiff++;
			}
			pancakeSlice = pancakeSliceNext;
		}
		
		return ctrStackDiff;
	}
}
