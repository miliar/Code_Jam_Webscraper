// CJ - Counting Sheep.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int getLastNumber(int N);
int determineOccurances(int Ni);

int main()
{

	string inputline = "";
	string fname = "";
	string strT = "", strN = "";
	int T = 0, N = 0, lastNumber = 0;
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
		getline(inpstream, strN);
		N = stoi(strN);
		lastNumber = getLastNumber(N);
		cout << "N = " << N << endl;
		outstream << "Case #" + to_string(i) + ": ";
		if (lastNumber == NULL) {
			outstream << "INSOMNIA";
		}
		else {
			outstream << to_string(lastNumber);
		}
		outstream << endl;
	}

    return 0;
}

int getLastNumber(int N) {
	bool repeat = false;
	int numtruth = 0, currTruth = 0, i = 1, foundloc = 0;
	vector<int> numbersSeen;
	vector<int>::iterator ittest;
	//numbersSeen.reserve[10];

	while (numtruth != 1023 && repeat == false) {
		
		numbersSeen.push_back(N*i);
		currTruth = determineOccurances(N*i);
		numtruth = numtruth | currTruth;
		
		ittest = find(numbersSeen.begin(), numbersSeen.end(), N*(i+1));
		
		if (ittest != numbersSeen.end()) {
			repeat = true;
		}
		i++;
	}
	if (repeat == false) {
		return N*(i-1);
	}
	else {
		return NULL;
	}
	
}

int determineOccurances(int Ni) {

	int npos = string::npos, currTruth = 0;
	string strNi = to_string(Ni);
	for (int i = 0; i < 10; i++ ) {
		if (strNi.find(to_string(i)) != npos) {
			currTruth = currTruth + (int)pow(2, i);
		}
	}
	return currTruth;

}