// GoogleCodeJam2013QualCFairAndSquare.cpp : Defines the entry point for the console application.
//

// Compiled using GCC 4.7.2 using the command line option -std=c++11

//#include "stdafx.h"
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

vector<long long> fairAndSquareNumbersFromAToB;

const long long A = 1;
const long long B = 100000000000000;

inline string longLongToString(const long long i) {
    stringstream ss;
    ss << i;
    return ss.str();
}

inline bool isPalindromeP(const long long i) {
	string s1 = longLongToString(i);
	string s2 = s1;
	reverse(s2.begin(),s2.end());
	return (s1 == s2);
}

// The vector is built in order, and does not be to sorted
void buildVectorOfKnownFairAndSquareNumbers() {
	for (long long i = A; i <= B; ++i) {
		if (isPalindromeP(i)) {
			long long ii = i * i;
			if (ii <= B) {
				if (isPalindromeP(ii)) {
					fairAndSquareNumbersFromAToB.push_back(ii);
				}
			} else {
				return;
			}
		}
	}
}

inline int numberOfFairAndSquareNumbersFromSToT(const long long S, const long long T) {
	int count = 0;
	for (auto i : fairAndSquareNumbersFromAToB) {
		if (S <= i) {
			if (T >= i) {
				++count;
			} else {
				// This works because fairAndSquareNumbersFromAToB is sorted
				break;
			}
		}
	}
	return count;
}

int main()
{
	ios::sync_with_stdio(0);
  //#pragma warning(disable : 4996)
	freopen("C-large-1.in", "r", stdin);
  //#pragma warning(disable : 4996)
	freopen("a.out", "w", stdout);

	buildVectorOfKnownFairAndSquareNumbers();

	int numberOfTestCases;
	cin >> numberOfTestCases;
	cin.ignore(1);

	for (int i = 0; i < numberOfTestCases; ++i) {
		long long a, b;
		cin >> a;
		cin >> b;

		cout << "Case #" << (i + 1) << ": " << numberOfFairAndSquareNumbersFromSToT(a,b) << endl;
		cin.ignore(1);
	}

	return 0;
}
