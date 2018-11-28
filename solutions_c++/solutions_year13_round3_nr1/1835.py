// GCJ Consonants.cpp : Defines the entry point for the console application.
//


// This was coded in visual studio 2012, this was the only file I modified in the default WIN32 Console Application Project

#include "stdafx.h"
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

// Optimizations
// Only check substrings that of at least the same size as the n-value

using namespace std;

inline int numberOfSubstringsOfSizeMOfStringOfSizeN(const int m, const int n) { return n - m + 1; }


inline int findNumberOfSubstringsOfSizeXWithNConsecutiveConsonants(const string name, const int n, const int x) {
	int toReturn = 0;

	{
		int loop1End = numberOfSubstringsOfSizeMOfStringOfSizeN(x, name.length());
		for (int placeHolderStart = 0; placeHolderStart < loop1End; ++placeHolderStart)
		{
			int placeHolderEnd = placeHolderStart + x;

			int consecutiveConsonantsCount = 0;
			for (int i = placeHolderStart; i < placeHolderEnd; ++i) {

				/* ASCII codes for lowercase vowels
				a: 97
				e: 101
				i: 105
				o: 111
				u: 117
				*/

				char toTest = name[i];
				// Not checking letters are lowercase
				if (97 != toTest && 101 != toTest && 105 != toTest && 111 != toTest && 117 != toTest) {
					++consecutiveConsonantsCount;
				} else {
					consecutiveConsonantsCount = 0;
				}

				if (n == consecutiveConsonantsCount) {
					toReturn += 1;
					break;
				}
			}
		}
	}

	return toReturn;
}

inline int findNValue(const string name, const int n) {
	int toReturn = 0;
	int nameLength = name.length();

	for (int x = nameLength; x >= n; --x) {
		int num = findNumberOfSubstringsOfSizeXWithNConsecutiveConsonants(name, n, x);
		toReturn += num;

		if (0 == num) {
			break;
		}
	}


	return toReturn;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ios::sync_with_stdio(0);
 #pragma warning(disable : 4996)
	freopen("A-small-attempt0.in", "r", stdin);
 #pragma warning(disable : 4996)
	freopen("a.out", "w", stdout);

	int numberOfTestCases;
	cin >> numberOfTestCases;
	cin.ignore(1);

	for (int i = 0; i < numberOfTestCases; ++i) {
		string name;
		cin >> name;
		int n;
		cin >> n;

		cout << "Case #" << (i + 1) << ": " << findNValue(name, n) << endl;
		cin.ignore(1);
	}

	return 0;
}

