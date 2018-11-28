// CJ - Evac.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

char letters[26] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' };
vector<string> &split(const string &s, char delim, vector<string> &elems);
vector<string> split(const string &s, char delim);
vector<int> getInpVector(string inputstr);
vector<int> FindLargest(vector<int> inpvals);
string getPosToEvac(vector<int> &inpvals);
int getPos(vector<int> inpvals, int val, bool skip);
int countOnes(vector<int> inpvals);

int main()
{
	string inpline = "";
	vector<int> inputvals;
	int N = 0;
	string fname = "";
	string strT = "";
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
	for (int i = 0; i < T; i++) {
		getline(inpstream, strT);
		N = stoi(strT);
		getline(inpstream, inpline);
		inputvals = getInpVector(inpline);
		//for (int j = 0; j < inputvals.size(); j++) cout << inputvals.at(j) << endl;
		outstream << "Case #" << i + 1 << ":";
		inpline = getPosToEvac(inputvals);
		while (inpline != "") {
			outstream << " " << inpline;
			inpline = getPosToEvac(inputvals);
		}
		outstream << endl;
	}
    return 0;
}

vector<string> &split(const string &s, char delim, vector<string> &elems) {
	stringstream ss(s);
	string item;
	while (getline(ss, item, delim)) {
		elems.push_back(item);
	}
	return elems;
}


vector<string> split(const string &s, char delim) {
	vector<string> elems;
	split(s, delim, elems);
	return elems;
}

vector<int> getInpVector(string inputstr) {

	vector<int> temp;
	vector<string> input;

	input = split(inputstr, ' ');
	for (int i = 0; i < input.size();i++) {
		temp.push_back(stoi(input.at(i)));
	}
	return temp;
}

vector<int> FindLargest(vector<int> inpvals) {
	vector<int> largest;
	int size = inpvals.size();
	sort(inpvals.begin(), inpvals.end());
	largest.push_back(inpvals.at(size-1));
	largest.push_back(inpvals.at(size-2));
	return largest;
}

string getPosToEvac(vector<int> &inpvals) {
	int posTwo = 0;
	int posOne = 0;
	vector<int> temp = inpvals;
	vector<int> largest = FindLargest(temp);

	if (largest[0] == 0) return "";
	posOne = getPos(inpvals, largest[0], false);
	if (largest[0] == largest[1]) {
		posTwo = getPos(inpvals, largest[1], true);
	}
	else if (largest[0] == largest[1] + 1) {
		posTwo = -1;
	}
	else {
		posTwo = posOne;
	}
	if (countOnes(inpvals) == 3) posTwo = -1;
	string chars = "";
	chars += letters[posOne];
	inpvals.at(posOne) -= 1;
	if (posTwo != -1) {
		chars += letters[posTwo];
		inpvals.at(posTwo) -= 1;
	}
	return chars;
}

int getPos(vector<int> inpvals, int val, bool skip) {
	for (int i = 0; i < inpvals.size(); i++) {
		if (inpvals.at(i) == val) {
			if (skip == false) {
				return i;
			}
			else {
				skip = false;
			}
		}
	}
	return -1;
}

int countOnes(vector<int> inpvals) {
	int count = 0;
	for (int i = 0; i < inpvals.size();i++) {
		if (inpvals.at(i) == 1) count++;
	}
	return count;
}