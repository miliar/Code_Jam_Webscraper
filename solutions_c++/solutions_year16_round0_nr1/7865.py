// CountingSheep.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <sstream>
#include <string> // this should be already included in <sstream>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

bool CheckDigits(bool * ValidDigits, int & OkNumCount, string StringNum)
{
	for (std::string::iterator it = StringNum.begin(); it != StringNum.end(); ++it)
	{
		int index = (*it) - 48;
		if (!ValidDigits[index])
		{
			ValidDigits[index] = true;
			if (++OkNumCount == 10)
				return true;
		}
	}
	return false;		
}

int CountingSheepCalc(const int InitNumber)
{
	bool ValidDigits[10] = { false, false, false, false, false, false, false, false, false, false };
	int IterateNumber = InitNumber;
	int OkNumCount = 0;
	string StringNum = static_cast<ostringstream*>(&(ostringstream() << IterateNumber))->str();
	while (!CheckDigits(ValidDigits, OkNumCount, StringNum))
	{
		IterateNumber += InitNumber;
		StringNum = static_cast<ostringstream*>(&(ostringstream() << IterateNumber))->str();
	}
	return IterateNumber;
}


int _tmain(int argc, _TCHAR* argv[])
{
	int t, n, result;
	cin >> t; 
	for (int i = 1; i <= t; ++i) {
		cin >> n; 
		if (n)
		{
			result = CountingSheepCalc(n);
			cout << "Case #"  << i <<": "<< result << endl;
		}
		else
			cout << "Case #" << i << ": INSOMNIA" << endl;
	}
	return 0;
}

