//============================================================================
// Name        : codejam.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
using namespace std;
#define MIN(a, b) ((a > b) ? b : a)
#define MAX(a, b) ((a > b) ? a : b)

bool isPalindrome(vector<int> num) {
	int n = num.size();
	for (int i = 0; i < n/2; i++) {
		if (num[i] != num[n - i -1]) return false;
	}
	return true;
}

bool isPalindrome(int n) {
	vector<int> num;
	while (n > 0) {
		num.push_back( n % 10);
		n = n /10;
	}
	reverse(num.begin(), num.end());

	return isPalindrome(num);
}

bool isSquare(int n) {
	int sq = (int) sqrt(n);
	if (sq * sq == n) return true;
	return false;
}

int main() {
	ifstream fi;
	ofstream fo;
	fi.open("in.in");
	fo.open("out.txt");

	int t;
	fi >> t;
	for (int c = 1; c <= t; c++) {
		int a, b;
		fi >> a >> b;
		int count = 0;

		for (int n = a; n <= b; n++) {
			if (!isSquare(n)) continue;
			if (!isPalindrome(n)) continue;
			int sq = (int) sqrt(n);
			if (isPalindrome(sq)) count++;
		}
		fo << "Case #" << c << ": " << count <<"\n";
	}

	fo.close();
	fi.close();
	return 0;
}
