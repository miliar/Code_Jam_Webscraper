// Qual-A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	int cases = 0;
	cin >> cases;

	for (int x = 0; x < cases; ++x)
	{
		int n;
		int res = 0;
		int sum = 0;
		string str;
		cin >> n >> str;

		int len = str.length();

		for (int i = 0; i < len; ++i)
		{
			if (str[i] != '0' && sum < i)
			{
				cerr << "shyness " << i << " needs " << i - sum << " people." << endl;
				res += i - sum;
				sum += i - sum;
			}
			sum += str[i] - '0';
		}
		
		cout << "Case #" << x+1 << ": " << res << endl;
	}

	return 0;
}

