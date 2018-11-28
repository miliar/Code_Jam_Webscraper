// Getting the Digits.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <cstdio>
#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main()
{
	int t;

	//cin >> t;

	ifstream ifile;
	ifile.open("A-large.in");
	ofstream ofile;
	ofile.open("ans.txt");
	ifile >> t;
	for (int index = 1; index <= t; index++)
	{
		int a[27] = { 0 };
		int num[10] = { 0 };
		string s;

		//cin >> s;
		ifile >> s;
		for (char c : s)
		{
			a[c - 'A' + 1]++;
		}
		
		//zero
		while (a['Z' - 'A' + 1] > 0)
		{
			a['Z' - 'A' + 1]--;
			a['E' - 'A' + 1]--;
			a['R' - 'A' + 1]--;
			a['O' - 'A' + 1]--;
			num[0]++;
		}
		//two
		while (a['W' - 'A' + 1] > 0)
		{
			a['T' - 'A' + 1]--;
			a['W' - 'A' + 1]--;
			a['O' - 'A' + 1]--;
			num[2]++;
		}
		//four
		while (a['U' - 'A' + 1] > 0)
		{
			a['F' - 'A' + 1]--;
			a['O' - 'A' + 1]--;
			a['U' - 'A' + 1]--;
			a['R' - 'A' + 1]--;
			num[4]++;
		}
		//six
		while (a['X' - 'A' + 1] > 0)
		{
			a['S' - 'A' + 1]--;
			a['I' - 'A' + 1]--;
			a['X' - 'A' + 1]--;
			num[6]++;
		}
		//eight
		while (a['G' - 'A' + 1] > 0)
		{
			a['E' - 'A' + 1]--;
			a['I' - 'A' + 1]--;
			a['G' - 'A' + 1]--;
			a['H' - 'A' + 1]--;
			a['T' - 'A' + 1]--;
			num[8]++;
		}
		//three
		while (a['H' - 'A' + 1] > 0 && a['R' - 'A' + 1] > 0)
		{
			a['T' - 'A' + 1]--;
			a['H' - 'A' + 1]--;
			a['R' - 'A' + 1]--;
			a['E' - 'A' + 1]--;
			a['E' - 'A' + 1]--;
			num[3]++;
		}
		//five
		while (a['F' - 'A' + 1] > 0 && a['I' - 'A' + 1] > 0)
		{
			a['F' - 'A' + 1]--;
			a['I' - 'A' + 1]--;
			a['V' - 'A' + 1]--;
			a['E' - 'A' + 1]--;
			num[5]++;
		}
		//seven
		while (a['S' - 'A' + 1] > 0 && a['E' - 'A' + 1] > 0)
		{
			a['S' - 'A' + 1]--;
			a['E' - 'A' + 1]--;
			a['V' - 'A' + 1]--;
			a['E' - 'A' + 1]--;
			a['N' - 'A' + 1]--;
			num[7]++;
		}
		//nine
		while (a['N' - 'A' + 1] > 0 && a['I' - 'A' + 1] > 0)
		{
			a['N' - 'A' + 1]--;
			a['I' - 'A' + 1]--;
			a['N' - 'A' + 1]--;
			a['E' - 'A' + 1]--;
			num[9]++;
		}
		//one
		while (a['O' - 'A' + 1] > 0 && a['N' - 'A' + 1] > 0 && a['E' - 'A' + 1] > 0)
		{
			a['O' - 'A' + 1]--;
			a['N' - 'A' + 1]--;
			a['E' - 'A' + 1]--;
			num[1]++;
		}

		//printf("Case #%d: ", index);
		ofile << "Case #" << index << ": ";


		for (int i = 0; i < 10; i++)
			for (int j = 0; j < num[i]; j++)
				ofile << i;
		
		ofile << endl;

	}





    return 0;
}

