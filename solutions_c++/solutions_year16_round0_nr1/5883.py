// CodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
#include <numeric> 
#include <vector> 
#include <sstream>
using namespace std;


int _tmain(int argc, _TCHAR* argv[]) {
	FILE *fin = freopen("A-large.in", "r", stdin);
	assert(fin != NULL);
	FILE *fout = freopen("A-large.out", "w", stdout);
	int T;

	cin >> T;
	for (int t = 1; t <= T; t++){
		unsigned long long nOriginal,n,nCopy;
		bool nums[10] = { 0 };
		int seenNums = 0;
		cin >> nOriginal;
		if (nOriginal != 0){
			int i = 1;
			do {
				n = i * nOriginal;
				nCopy = n;
				do {
					int digit = nCopy % 10;
					nums[digit] = 1;
					seenNums = accumulate(begin(nums), end(nums), 0);
					nCopy /= 10;
				} while (nCopy >0 && seenNums != 10);
				i++;
			} while (seenNums != 10);

			cout << "Case #" << t << ": ";
			cout << n  << endl;
		}
		else{
			cout << "Case #" << t << ": ";
			cout << "INSOMNIA" << endl;
		}
	}
	exit(0);
}