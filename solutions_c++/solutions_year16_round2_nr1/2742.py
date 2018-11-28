// CJ - Get Digits.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;
bool FindNumber(int strindex, string& str);
void Removenthchar(string& str, int n);
void RemoveCertains(string& input);
int countchars(string s, char c);
string numbers[] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
vector<int> phonenumber;
int main()
{
	string fname = "";
	string strT = "", inpline = "", currString = "", initialString = "";
	int T = 0, N = 0, J = 0, currJ = 0;
	ifstream inpstream;
	ofstream outstream;
	
	
	cout << "Input filename without extension" << endl;
	//Input filename
	cin >> fname;
	//Open file
	inpstream.open("C:\\Users\\User\\Downloads\\" + fname + ".in");

	//Get size of file
	getline(inpstream, strT);
	T = stoi(strT);
	//Open output file
	outstream.open("C:\\Users\\User\\Downloads\\" + fname + ".out", ofstream::out | ofstream::trunc);
	
	for (int linecount = 1; linecount <= T; linecount++) {
		getline(inpstream, inpline);
		RemoveCertains(inpline);
		sort(phonenumber.begin(), phonenumber.end());
		outstream << "Case #" << linecount << ": ";
		for (int phonelen = 0; phonelen < phonenumber.size(); phonelen++) {
			outstream << phonenumber[phonelen];
		}
		outstream << endl;
		phonenumber.clear();
	}
	
    return 0;
}

bool FindNumber(int strindex, string& str) {
	size_t loc = 0;
	strindex;
	for (int i = 0; i < numbers[strindex].length(); i++) {
		loc = str.find(numbers[strindex][i]);
		if (loc == string::npos) return false;
		else Removenthchar(str, loc);
	}
	return true;
}

void Removenthchar(string& str, int n) {
	string temp = "";
	for (int i = 0; i <= str.length(); i++) {
		if (i != n) temp += str[i];
	}
	str = temp;
}

void RemoveCertains(string& input) {
	size_t zero, one, two = 0,three, four = 0,five, six = 0,seven, eight = 0,nine, i = 0;
	zero = countchars(input, 'Z');
	two = countchars(input, 'W');
	four = countchars(input, 'U');
	six = countchars(input, 'X');
	eight = countchars(input, 'G');
	for (i = 0; i < zero; i++) {
		phonenumber.push_back(0);
		FindNumber(0, input);
	}
	for (i = 0; i < two; i++) { 
		phonenumber.push_back(2);
		FindNumber(2, input);
	}
	for (i = 0; i < four; i++) {
		phonenumber.push_back(4);
		FindNumber(4, input);
	}
	for (i = 0; i < six; i++) {
		phonenumber.push_back(6);
		FindNumber(6, input);
	}
	for (i = 0; i < eight; i++) {
		phonenumber.push_back(8);
		FindNumber(8, input);
	}
	three = countchars(input, 'H');
	for (i = 0; i < three; i++) {
		phonenumber.push_back(3);
		FindNumber(3, input);
	}
	one = countchars(input, 'O');
	for (i = 0; i < one; i++) {
		phonenumber.push_back(1);
		FindNumber(1, input);
	}
	five = countchars(input, 'F');
	for (i = 0; i < five; i++) {
		phonenumber.push_back(5);
		FindNumber(5, input);
	}
	seven = countchars(input, 'S');
	for (i = 0; i < seven; i++) {
		phonenumber.push_back(7);
		FindNumber(7, input);
	}
	nine = countchars(input, 'I');
	for (i = 0; i < nine; i++) {
		phonenumber.push_back(9);
		FindNumber(9, input);
	}
}
int countchars(string s, char c) {
	int count = 0;

	for (int i = 0; i < s.length(); i++) {
		if (s[i] == c) count++;
	}
	return count;
}