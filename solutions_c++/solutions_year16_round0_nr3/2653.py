#include <iostream>
#include <bitset>
#include <algorithm>
#include <cmath>

using namespace std;

int nFoundJamcoins = 0;
const int nDigits = 16;
const int nJamcoins = 50;

int getDivisor(unsigned long long int number) {
	for (int i = 3; i < sqrt(number); i+=2) {
		if (number % i == 0) return i;
	}

	return 0;
}


void printJamcoin(int jamcoin[]) {
	for (int i = 0; i < nDigits; ++i) {
		cout << jamcoin[i];
	}
	cout << " ";
}

void checkValidJamcoin(int jamcoin[]) {
	unsigned long long int sum2 = 0;
	unsigned long long int sum4 = 0;
	unsigned long long int sum6 = 0;
	unsigned long long int sum8 = 0;
	unsigned long long int sum10 = 0;
	for (int digit = 0; digit < nDigits; ++digit) {
		if (jamcoin[digit] == 0) {
			continue;
		}

		int powerBase = nDigits-digit-1;
		sum2 += pow(2, powerBase);
		sum4 += pow(4, powerBase);
		sum6 += pow(6, powerBase);
		sum8 += pow(8, powerBase);
		sum10 += pow(10, powerBase);
	}

	int divisor2 = getDivisor(sum2);
	int divisor4 = getDivisor(sum4);
	int divisor6 = getDivisor(sum6);
	int divisor8 = getDivisor(sum8);
	int divisor10 = getDivisor(sum10);

	if (divisor2 && divisor4 && divisor6 && divisor8 && divisor10) {
		printJamcoin(jamcoin);
		cout << divisor2 << " 2 " << divisor4 << " 2 " << divisor6 << " 2 " << divisor8 << " 2 " << divisor10 << endl;
		nFoundJamcoins ++;
		if (nFoundJamcoins == nJamcoins) {
			exit(0);
		}
	}
}

int main(int argc, char const *argv[]) {

	cout << "Case #1:" << endl;

	for (int nOnes = 2; nOnes < nDigits; nOnes+=2) {
		int jamcoin[nDigits];
		for (int id = 0; id < nDigits; ++id) {
			jamcoin[id] = 0;
		}

		jamcoin[nDigits-1] = 1;
		for (int id = 0; id < nOnes-1; ++id) {
			jamcoin[id] = 1;
		}

		sort(jamcoin+1, jamcoin+nDigits-1);

		while (next_permutation(jamcoin+1, jamcoin+nDigits-1)) {
			checkValidJamcoin(jamcoin);
		}
	}

	return 0;
}