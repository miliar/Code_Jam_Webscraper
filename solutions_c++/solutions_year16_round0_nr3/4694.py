/*
 * jamNumbers.cpp
 *
 *  Created on: Apr 9, 2016
 *      Author: Lesly
 */

#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
using namespace std;

vector <int> binVector;
int countString = 0;
int j = 0;

long long primeDivisor(int n,long long decRep)
{
	for(long long i = 2; i < sqrt(decRep); i++)
	{
		if(decRep % i == 0){
			return i;
		}
	}

	return decRep;
}

void convertingAndFindNumbers(int n){
//	string binString;
//	reverse(binString.begin(), binString.end());

	vector<long long> divisors;


	for(int base = 2; base < 11; base++)
	{
//		long long dec = 0;
//		for (int i = 0; i < binString.size(); i++) {
//			dec += ((long long)(binString[i]) - 48)*pow(base, i);
//		}
//		cout << dec << " ";

		long long decRep = 0;
		for(int i = 0; i < n; i++)
		{
			if(binVector[i] == 1) decRep += pow(base, n - i - 1);
		}

//		cout << "decimal repr in base " << base << " is: " << decRep << endl;

		long long primeDivisorNumber = primeDivisor(n, decRep);

		if(primeDivisorNumber != decRep){
			divisors.push_back(primeDivisorNumber);
		}
		else
		{
			divisors.clear();
			return;
		}
	}

	countString++;
	for(auto i: binVector)
	{
		cout << i;
	}
	cout << " ";
	for(int i = 0; i < 9; i++)
	{
		cout << divisors[i] << " ";
	}
	cout << endl;


	divisors.clear();

}

void resetVector(int n)
{
	binVector.clear();
	binVector.resize(n, 0);
	binVector[0] = 1;
	for (int i = 1; i < n - 1; i++){
		binVector[i] = 0;
	}
	binVector[n - 1] = 1;

}

void generateBinaryNumbers(int level, int n){

	if (countString == j){
		return;
	}

	if(level < (n - 2)){
		generateBinaryNumbers(level + 1, n);

		for(int i = level + 1; i < n - 1; i++){
			binVector[i] = 0;
		}
		binVector[level + 1] = 1;

		generateBinaryNumbers(level + 1, n);
	}
	else
	{
		// String's Analysis
		if(level == n - 2) convertingAndFindNumbers(n);
	}
}



int main() {

	int t = 0;
	int n = 0;

	cin >> t >> n >> j;
	cout << "Case #1: " << endl;

	resetVector(n);

	generateBinaryNumbers(1, n);
	resetVector(n);
	binVector[1] = 1;
	generateBinaryNumbers(1, n);

	return 0;
}


