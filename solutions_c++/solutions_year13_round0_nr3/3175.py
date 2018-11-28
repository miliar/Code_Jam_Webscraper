	//
	//  Lawnmower.cpp
	//
	//
	//  Created by Alex Sorafumo on 13/04/13.
	//
	//

#include <iostream>
#include <string>
#include <cmath>
#include <stdlib.h>
#include <sstream>

using namespace std;

bool isPalindrome(string);
string nextPalindrome(string);
string findPalindrome(string);
string convertInt(int);

int main(){
	int numCases, casesTested = 0;
	int interval[10001][2];
	int fairSquares;
	long value;
	cin >> numCases;
		//Get inputs
	while (casesTested < numCases) {
		cin >> interval[casesTested][0] >> interval[casesTested][1];
		casesTested++;
	}
	casesTested = 0;
	string number, square;
		//Process Inputs and Spit out results
	while (casesTested < numCases) {
		fairSquares = 0;
		number = convertInt(interval[casesTested][0]);
		number = findPalindrome(number);
		value = atol(number.c_str());
		while (value <= interval[casesTested][1]) {
			if(isPalindrome(number) && sqrt(value) == (int)sqrt(value) && isPalindrome(convertInt((int)sqrt(value)))){
				fairSquares++;
					//cout << "Pal: " << number << " | SQRT: " << (int)sqrt(value) << endl;
			}
			number = nextPalindrome(number);
			value = atol(number.c_str());
		}
		cout << "Case #" << casesTested + 1 << ": " << fairSquares << endl;
		casesTested++;
	}
	return 0;
}

bool isPalindrome(string number){
	int digits = number.length();
	int s = 0, e = digits - 1;
	while (s < e) {
		if (number[s] != number[e]) {
			return false;
		}
		s++;
		e--;
	}
		//cout << "Pal: " <<  number << endl;
	return true;
}

string nextPalindrome(string number){
	int digits = number.length();
	int s, e;
	int carry = 1;
	if (digits % 2 == 1) {
		s = e = digits / 2;
		while (s >= 0 && e <= digits){
			if (s == e) {
				if (carry > 0) {
					if (number[s] == '9') {
						number[s] = '0';
						carry++;
					}
					else{
						number[s]++;
					}
				}
			}
			else{
				if (carry > 0) {
					if (number[s] == '9' || number[e] == '9') {
						number[s] = '0';
						number[e] = '0';
						carry++;
					}
					else{
						number[s]++;
						number[e]++;
					}
				}
			}
			carry--;
			s--;
			e++;
			if (carry == 0) {
				break;
			}
		}
		if (carry == 1) {
			number.insert(number.begin(), '1');
			number[digits] = '1';
		}
	}
	else{
		s = e = digits / 2;
		s--;
		while (s >= 0 && e <= digits){
			if (carry > 0) {
				if (number[s] == '9' || number[e] == '9') {
					number[s] = '0';
					number[e] = '0';
					carry++;
				}
				else{
					number[s]++;
					number[e]++;
				}
			}
			carry--;
			s--;
			e++;
			if (carry == 0) {
				break;
			}
		}
		if (carry == 1) {
			number.insert(number.begin(), '1');
			number[digits] = '1';
		}
	}
	return number;
}

string findPalindrome(string number){
	int carry, pos;
	int digits = number.length();
	while(!isPalindrome(number)){
		carry = 1;
		pos = digits - 1;
		while (pos >= 0) {
			if (number[pos] == '9') {
				number[pos] = '0';
				carry++;
			}
			else{
				number[pos]++;
			}
			carry--;
			pos--;
			if (carry == 0) {
				break;
			}
		}
		if (carry == 1) {
			number.insert(number.begin(), '1');
			number[digits] = '1';
		}
			//cout << "Pal: " <<  number << endl;
	}
	return number;
}

string convertInt(int number)
{
	stringstream ss;
	ss << number;
	return ss.str();
}

