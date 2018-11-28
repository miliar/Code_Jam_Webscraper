// B.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <fstream>
#include <string>

using namespace std;

int get_res(string & str, int index)
{
	int new_inx = index;
	while (str[new_inx] != '-')
	{
		new_inx--;
		if (new_inx < 0)
			return 0;
	}

	if (str[0] == '+')
	{
		int i = 0;
		while (str[i] == '+')
		{
			str[i] = '-';
			i++;
		}
	}
	else
	{
		string str_tmp(str);
		for (int i = 0; i <= new_inx; i++)
		{
			str[i] = (str_tmp[new_inx - i] == '+') ? '-' : '+';
		}
	}

	return get_res(str, new_inx) + 1;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream fi("b.in");
	ofstream fo("b.out");

	int t;
	fi >> t;

	string str;
	getline(fi, str);
	for (int i = 0; i < t; i++)
	{
		getline(fi, str);

		fo << "Case #" << i + 1 << ": " << get_res(str, str.length()-1) << endl;
	}

	fi.close();
	fo.close();

	return 0;
}

