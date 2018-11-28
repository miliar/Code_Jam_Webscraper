// CJ - Infinite Pancake House.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int ConvertInpToInt(string input);
void FlipnthBit(int& binrep, int n);
void FlipTopnOfStack(int& binrep, int n, int bitlength);
int GetLengthToInvert(string inpline);
int GetOptimalSwaps(string inpline);
string ConvertBinToString(int binrep, int bitlength);

int main()
{
	string inputline = "";
	string fname = "";
	string strT = "", inpline = "";
	int T = 0;
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
	
	for (int i = 1; i <= T; i++) {
		getline(inpstream, inpline);
		outstream << "Case #" + to_string(i) + ": " + to_string(GetOptimalSwaps(inpline)) << endl;
	}
    return 0;
}

int ConvertInpToInt(string input) {

	int binrep = 0;
	for(int i = 0; i < (int)input.length(); i++) {
		if (input[(int)input.length() - i - 1] == '+') {
			binrep += (int)pow(2, i);
		}
	}
	return binrep;
}

//Least sig bit, n = 1
void FlipnthBit(int& binrep, int n) {
	binrep = binrep ^ (1 << (n - 1));
}

void FlipTopnOfStack(int& binrep, int n, int bitlength) {

	for (int i = 0; i < n; i++) {
		FlipnthBit(binrep, bitlength - i);
	}

}

int GetLengthToInvert(string inpline) {
	char first = inpline[0];
	int i = 0;

	while (inpline[i] == first) {
		i++;
	}
	return i;
}

int GetOptimalSwaps(string inpline) {
	int inplength = inpline.length();
	int binrep = ConvertInpToInt(inpline);
	int i = 0;
	string currRep = "";
	while (binrep != (int)pow(2,inplength)-1)
	{
		currRep = ConvertBinToString(binrep, inplength);
		FlipTopnOfStack(binrep, GetLengthToInvert(currRep), inplength);
		i++;
	}

	return i;
}

string ConvertBinToString(int binrep, int bitlength) {
	
	int remainder = 0;
	string stringrep = "";
	if (binrep == 0) stringrep = "-";
	else {
		while (binrep != 0) {
			if (binrep % 2 == 0) stringrep += "-";
			else stringrep += "+";
			binrep = binrep / 2;
		}
	}
	for (int i = stringrep.length(); i < bitlength; i++) stringrep += "-";
	reverse(stringrep.begin(), stringrep.end());
	return stringrep;

}