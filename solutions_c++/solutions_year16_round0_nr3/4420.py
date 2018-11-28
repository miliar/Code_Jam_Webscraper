// jamcoin.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <fstream>

using namespace std;
int isprime(long long);
int nontrivial(long long);
long long stoix(string, int);

int _tmain(int argc, _TCHAR* argv[])
{
	int testcase = 0;
	int N = 0;
	int J = 0;
	int found = 0;
	long long inc = 0;
	int mul[11] = {0};
	string result;
	ifstream infile("ip.txt");
	ofstream outfile("op.txt");
	infile >> testcase;
	if (testcase != 1) {
		return 0;
	}
	infile >> N >> J;
	outfile << "Case #1: " << endl;
	if (N <= 0 || J <= 0) {
		return 0;
	}
	int startposi = (sizeof(int) * 8) - N + 2;
	int counter = 0;
	while (1) {
		result += '1';
		for (int i = 0; i < (N - 2); i++) {
			unsigned int ls = ((inc << (startposi + i)));
			unsigned int rs = (ls >> ((sizeof(int) * 8 - 1)));
			result += ('0' + rs);
		}
		result += '1';
		for (int i = 2; i <= 10; i++){
			long long ans = stoix(result, i);
			if (!isprime(ans)) {
				mul[i] = nontrivial(ans);
				counter++;
			}
			else {
				counter = 0;
				memset(mul, 0, 11);
				break;
			}
			if (counter == 9) {
				found++;
				counter = 0;
				outfile << result << " ";
				for (int i = 2; i <= 10; i++) {
					outfile << mul[i] << " ";
				}
				outfile << endl; 
				for (int i = 0; i < 11; i++){
					mul[i] = 0;
				}
			}
		}
		result.clear();
		inc++;
		counter = 0;
		if (found == J) {
			break;
		}
	}

	return 0;
}

int isprime(long long number) {
	if (number <= 1) return 0; 
	long long i;
	for (i = 2; i*i <= number; i++) {
		if (number % i == 0) return 0;
	}
	return 1;
}
int nontrivial(long long ans)
{
	for (int i = 2; i < ans; i++) {
		if ((ans%i) == 0) 
			return i;
	}
	return -1;
}


long long stoix(string str, int base)
{
	long long result = 0;
	string hold = str;
	int len = str.size();
	for (int i = 0; i < len; i++) {
		double powr = pow(base, i);
		int sum = hold[len-i-1] - '0';
		result += (sum*powr);
		str.resize(str.size() - 1);
	}
	return result;
}