// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <fstream>
#include <set>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream f_in("a.in");
	ofstream f_out("a.out");

	int t;
	f_in >> t;
	for (int i = 0; i < t; i++)
	{
		int n;
		f_in >> n;
		if (n == 0)
		{
			f_out << "Case #" << i+1 << ": INSOMNIA" << endl;
			continue;
		}

		long res;
		int m = 0;
		set<char> numbers;
		while(numbers.size() < 10)
		{
			m++;
			res = n*m;
			char str[32];
			ltoa(res, str, 10);
			for(int j = 0; j < strlen(str); j++)
				numbers.insert(str[j]);
		}

		f_out << "Case #" << i+1 << ": " << res << endl;
	}

	f_in.close();
	f_out.close();

	return 0;
}

