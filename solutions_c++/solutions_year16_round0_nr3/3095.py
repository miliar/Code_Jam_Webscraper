// CJ - Coin Jam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include "BigIntegerLibrary.hh"

using namespace std;

int CheckPrime(BigUnsigned currTest);
BigUnsigned BigPow(BigUnsigned base, int power);
BigUnsigned ConvertStringToBaseN(string input, int N);
string ConvertDecToString(BigUnsigned decrep, int bitlength);
BigUnsigned ConvergSqrt(BigUnsigned currSol, BigUnsigned n);
vector<int> GetFactors(string input);
string GetNextString(string input);
string GetInitialString(int N);

int main()
{

	string fname = "";
	string strT = "", inpline = "", currString = "", initialString = "";
	int T = 0, N = 0, J = 0, currJ = 0;
	vector<int> currFactors;
	ifstream inpstream;
	ofstream outstream;
	BigUnsigned currTest = 0;
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
	
	getline(inpstream, inpline);
	if (inpline[0] == '1') N = 16, J = 50;
	else if(inpline[0] == '3') N = 32, J = 500;
	else N = 6, J = 3;

	outstream << "Case #1:" << endl;
	//cout << CheckPrime(BigPow(100, 8)+61) << endl;
	initialString = GetInitialString(N);
	currString = initialString;
	while (currJ < J) {
		currFactors = GetFactors(currString);
		if (find(currFactors.begin(), currFactors.end(), NULL) == currFactors.end()) {
			currJ += 1;
			outstream << currString;
			for (int i = 0; i < currFactors.size(); i++) {
				outstream << " " << currFactors.at(i) ;
			}
			outstream << endl;
		}
		currString = GetNextString(currString);
		if (currString.length() > initialString.length()) currJ = J, cout << "Error!" << endl;
	}
	

	string test = "";

    return 0;
}


int CheckPrime(BigUnsigned currTest) {
	BigUnsigned maxMultiple = ConvergSqrt(currTest, NULL)+1;
	BigUnsigned divisor = 0;
	//Ignore factors above 10k to speed up processing time
	if (maxMultiple > 10000) maxMultiple = 10000;
	for (BigUnsigned i = 2; i <= maxMultiple; i++) {
		if (currTest % i == 0) {
			divisor = i;
			i = maxMultiple;
		}
	}
	if (divisor == 0) return NULL;
	else return divisor.toInt();
	
}

BigUnsigned BigPow(BigUnsigned base, int power) {
	BigUnsigned answer = 1;
	if (power == 0) return 1;
	if (power < 0) return NULL;
	for (int i = 0; i < power; i++) {
		answer *= base;
	}
	return answer;
}


string ConvertDecToString(BigUnsigned decrep, int bitlength) {

	int remainder = 0;
	string stringrep = "";
	if (decrep == 0) stringrep = "0";
	else {
		while (decrep != 0) {
			if (decrep % 2 == 0) stringrep += "0";
			else stringrep += "1";
			decrep = decrep / 2;
		}
	}
	for (int i = stringrep.length(); i < bitlength; i++) stringrep += "0";
	reverse(stringrep.begin(), stringrep.end());
	return stringrep;

}

BigUnsigned ConvertStringToBaseN(string input, int N) {

	BigUnsigned binrep = 0;
	for (int i = 0; i < (int)input.length(); i++) {
		if (input[(int)input.length() - i - 1] == '1') {
			binrep += BigPow(N, i);
		}
	}
	return binrep;
}

BigUnsigned ConvergSqrt(BigUnsigned currSol, BigUnsigned n) {
	if (n == NULL) n = currSol;
	BigUnsigned nextSol = (currSol + n / currSol) / 2;

	if (currSol == nextSol || nextSol > currSol) return currSol;
	else return ConvergSqrt(nextSol, n);

}

vector<int> GetFactors(string input) {
	BigUnsigned decrep = 0;
	vector<int> factorlist;
	int currentFactor = 0;
	for (int base = 2; base <= 10; base++) {
		decrep = ConvertStringToBaseN(input, base);
		currentFactor = CheckPrime(decrep);
		if (currentFactor == NULL) factorlist.push_back(NULL), base = 10;
		else factorlist.push_back(currentFactor);
	}
	return factorlist;
}

string GetNextString(string input) {
	return ConvertDecToString(ConvertStringToBaseN(input, 2) + 2, input.length());
}

string GetInitialString(int N) {
	string initialString = "1";
	for (int i = 2; i < N; i++) {
		initialString += "0";
	}
	initialString += "1";
	return initialString;
}