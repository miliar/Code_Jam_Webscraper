// future_glimpse.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

// include c++ headers
#include <iostream>
#include <unordered_map>
#include <map>
#include <set>
#include <cstdio>
#include <string>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	int t;
	cin >> t;

	// some constants
	char PLUS = '+';
	char MINUS = '-';

	for(int i=1; i<=t; i++)
	{
		string s;
		cin >> s;
		int moves = 0;
		int len = s.length();

		// initial state
		char LAST = s[0];
		
		for(int j=0; j<len; j++)
		{
			if(LAST != s[j])
			{
				moves++;
				LAST = s[j];
			}
		}

		if(LAST==MINUS)
		{
			moves++;
		}

		cout << "Case #" << i << ": " << moves << endl;
 	}

	return 0;
}

