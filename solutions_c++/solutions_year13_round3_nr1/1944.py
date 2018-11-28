// 1c.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<iostream>
#include<string>
using namespace std;
unsigned long T;
string S;
unsigned long L,N;
long long result;
bool isConsonant( string &s ) {
	for ( unsigned long i = 0; i < N; i++ ) {
		if ( s[i] == 'a' || s[i] == 'e' || s[i] == 'i'  || s[i] == 'o'  || s[i] == 'u'  )
			return false;
	}
	return true;
}
int _tmain(int argc, _TCHAR* argv[])
{
	cin >> T;
	unsigned long last_index;
	for ( unsigned long i = 0; i < T ; i++ ) {
		cin >> S >> N;
		L = S.length()-N+1; 
		last_index = 0;
		result = 0;
		for ( unsigned long j = 0; j < L; j++ ) {
			if ( isConsonant(S.substr(j,N))) {
				result += (L-j)*(j+1-last_index);
				last_index = j+1;
			}
		}
		cout << "Case #" << i+1 << ": " << result << "\n";
	}
	return 0;
}

