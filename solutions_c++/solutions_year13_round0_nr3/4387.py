/*
 * main.cpp
 *
 *  Created on: 7 avr. 2013
 *      Author: Khabat95
 */


#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <cassert>
#include <complex>

using namespace std;

bool isPalindrome(int value) {
	string value_str;
	stringstream value_convert;
	value_convert << value;
	value_str = value_convert.str();

	int length = value_str.length();
	char value_chars[length];
	memcpy(value_chars, value_str.c_str(), length);
	for(int i=0; i<length/2; ++i) {
		if(value_chars[i] != value_chars[length-1-i])
			return false;
	}

	return true;
}

bool isPalindromeSquare(int value) {
	double square = sqrt(value);
	if((int)square == square)
		return isPalindrome(square);

	return false;
}

void algo() {
	int a, b;
	cin >> a >> b;

	int res = 0;
	for(int i=a; i<=b; ++i) {
		if(isPalindrome(i) && isPalindromeSquare(i))
			res++;
	}

	cout << res << endl;
}

int main() {
	int n_cases;
	cin >> n_cases;

	for(int i=0; i<n_cases; ++i) {
		cout << "Case #" << i+1 << ": ";
		algo();
	}
}

