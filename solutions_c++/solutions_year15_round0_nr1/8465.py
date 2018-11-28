// A.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>

using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("input.txt");
	ofstream out("output.txt");
	int n;
	in >> n;


	for (int w = 1; w <= n; w++)
	{
		int fre = 0;
		int sum = 0;

		int k;
		in >> k;

		char c;
		in >> c;
		sum = c - 48;
		for (int i = 1; i <= k; i++)
		{
			in >> c;
			if (i <= sum)
				sum += c - 48;
			else
			{
				fre += i - sum;
				sum += i - sum + c - 48;
			}
		}

		out << "Case #" << w << ": " << fre << endl;


	}
	return 0;
}

