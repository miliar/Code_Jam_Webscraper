//============================================================================
// Name        : CodeJam.cpp
// Author      : test
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <cmath>
#include <iostream>
#include <string>
#include <boost\lexical_cast.hpp>

using namespace std;

bool checkPalindrome(string input)
{
	int limit = ceil(input.length() / 2.0);
	for(int i = 0; i < limit; ++i)
	{
		int second = input.length() - i - 1;
		if(second < 0 || second >= input.length()) break;
		if(input[i] != input[second])
		{
			return false;
		}
	}
	return true;
}

int main()
{
    // Load cases
	int cases = 0;
	cin >> cases;

	for(int xxx = 0; xxx < cases; ++xxx)
	{
		int _begin, _end;
		cin >> _begin >> _end;
		int begin = static_cast<int>( floor( sqrt(_begin)));
		int end   = static_cast<int>( floor( sqrt(_end)));

		int counter = 0;

		for(int i = begin; i <= end; ++i)
		{
			// Check square
			int square = i * i;
			if(square < _begin || square > _end) continue;
			// Check palindrome
			string stryng = boost::lexical_cast<string>(i);
			if(!checkPalindrome(stryng))
			{
				continue;
			}
			// Check square palindrome
			stryng = boost::lexical_cast<string>(square);
			if(!checkPalindrome(stryng))
			{
				continue;
			}
			++counter;
		}
		cout << "Case #" << (xxx + 1) << ": " << counter << endl;
	}
	return 0;
}
