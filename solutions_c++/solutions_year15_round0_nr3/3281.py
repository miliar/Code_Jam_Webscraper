/*
 * Main.cpp
 *
 *  Created on: 11.04.2015
 *      Author: David
 */

#include <iostream>
#include <fstream>

using namespace std;

const short quatTable[4][4] = { { 1, 2, 3, 4 }, { 2, -1, 4, -3 },
		{ 3, -4, -1, 2 }, { 4, 3, -2, -1 } };

struct quaternion {
	bool neg;
	char base;
};

quaternion operator*(quaternion lhs, quaternion rhs) {
	short lhsVal = lhs.base - 'h';
	short rhsVal = rhs.base - 'h';
	short result = quatTable[lhsVal][rhsVal];
	bool neg = lhs.neg;
	neg ^= rhs.neg;
	if (result < 0) {
		result *= (-1);
		neg ^= true;
	}
	char base = 'g' + result;
	return {neg, base};
}

quaternion operator*=(quaternion &lhs, quaternion rhs) {
	short lhsVal = lhs.base - 'h';
	short rhsVal = rhs.base - 'h';
	short result = quatTable[lhsVal][rhsVal];
	bool neg = lhs.neg;
	neg ^= rhs.neg;
	if (result < 0) {
		result *= (-1);
		neg ^= true;
	}
	char base = 'g' + result;
	lhs.neg = neg;
	lhs.base = base;
	return {neg, base};
}

bool operator==(quaternion lhs, quaternion rhs) {
	return lhs.base == rhs.base && (lhs.neg == rhs.neg);
}

void print(quaternion a) {
	if (a.neg)
		cout << "-";
	cout << a.base << endl;
}

bool is_splittable(unsigned long L, unsigned long X, char* lstring) {
	quaternion totalL = { false, 'h' };
	for (unsigned long i = 0; i < L; i++) {
		quaternion current = { false, lstring[i] };
		totalL *= current;
	}
	quaternion total = { false, 'h' };
	for (unsigned long i = 0; i < X; i++) {
		total *= totalL;
	}
	if (!total.neg || total.base != 'h')
		return false;

	quaternion totalLeft = { false, 'h' };
	bool iOk = false;
	bool jOk = false;
	quaternion I = { false, 'i' };
	quaternion J = { false, 'j' };
	quaternion IJ = I * J;
	for (unsigned long j = 0; j < X; j++)
		for (unsigned long i = 0; i < L; i++) {
			quaternion current = { false, lstring[i] };
			totalLeft *= current;
			if (totalLeft == I)
				iOk = true;
			if (totalLeft == IJ && iOk)
				return true;
		}
	return false;
}

int main() {
	ifstream infile("C-small.txt");
	ofstream outfile("output.txt");
	int tests;
	infile >> tests;
	for (int i = 0; i < tests; i++) {
		unsigned long L, X;
		infile >> L >> X;
		char* lstring = new char[L];
		for (unsigned long j = 0; j < L; j++)
			infile >> lstring[j];
		bool result = is_splittable(L, X, lstring);
		outfile << "Case #" << (i + 1) << ": ";
		if (result)
			outfile << "YES";
		else
			outfile << "NO";
		outfile << endl;
	}
	return 0;
}
