#include "stdafx.h"

#include <fstream>
#include <sstream>

#include <iostream>
#include <string>
#include <vector> 
#include <algorithm>
#include <map>
#include <stack>
#include <bitset>         // std::bitset

using namespace std;

int main()
{
	int t = 1;
	ifstream fin;
	fin.open("in.in");
	ofstream fout;
	fout.open("output.txt");

	fin >> t;

	for (int m = 0; m < t; m++)
	{
		int k, c, s;
		fin >> k >> c >> s;
		unsigned long long f = pow(k, (c - 1));
		fout << "Case #" << (m + 1) << ":";
		for (int i = 0; i < s; i++)
		{
			fout << " " << f*i + 1;
		}
		fout << "\n";
	}
	fout.close();
	
}