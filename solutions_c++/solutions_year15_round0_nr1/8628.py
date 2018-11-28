//============================================================================
// Name        : gcj-a.cpp
// Author      : Engin Manap
// Version     :
// Copyright   : GLP3
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <cmath>

#define MAX_SIZE 1000

using namespace std;

inline int power(int base, int exp){
	if (exp == 0) return 1;
	if (exp == 1) return base;
	if (exp < 0 ) cerr << "negative exponent!" << endl;
	int r = base;
	for (int j = 1; j < exp; ++j)  r *= base;
	return r;
}

int main() {
	//read the input
	int testCases, maxS, currentCount, neededFriends;
	char sString[MAX_SIZE];
	cin >> testCases;


	for(int i=0; i<testCases; ++i){
		//process the test case

		//reset the values
		neededFriends = 0;
		currentCount=0;
		memset(sString,0,MAX_SIZE);
		cin >> maxS >> sString;

		//cerr << "max is " << maxS << endl;
		//cerr << "sString is " << sString << endl;


		//process the shyness string, one by one
		for(int j=0;j<=maxS;++j){
			if(currentCount < j){
				// we should add 1 person
				currentCount++;
				neededFriends++;
			}
			currentCount += sString[j] - 48;
			//sString = sString - ((sString / power(10,j))*power(10,j));
			//cerr << "string is now " << sString<< ", currently " << currentCount << " people clapping, " << neededFriends << " of them set up" << endl;

			}
			cout << "Case #" << i+1 <<": " << neededFriends << endl; //
		}
	return 0;
}
