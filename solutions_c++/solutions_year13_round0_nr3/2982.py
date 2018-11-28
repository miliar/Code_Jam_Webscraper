//============================================================================
// Name        : jam_test.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <fstream>
//#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

char num[10];

bool palindrome(int x)
{
	sprintf(num, "%d", x);
	int len = strlen(num);
	for(int i=0; i<len/2; i++)
		if(num[i] != num[len-1-i])
			return false;
	return true;
}

int main(int argc, char** argv)
{

	if(argc!=3)
	{
		cout << "Usage:" << endl;
		cout << "jam_test infile outfile" << endl;
		return 0;
	}

	ifstream infile(argv[1]);
	ofstream outfile(argv[2]);

	if(!infile)
		cout << "Input file open error!" << endl;

	if(!outfile)
		cout << "Output file open error!" << endl;

	int nCase;

	int a,b;
	int i,j;

	infile >> nCase ;
	//cout << "Case Num:" << nCase << endl;

	for(int iCase=0; iCase<nCase; iCase++)
	{
		cout << "Case #" << iCase+1 << ": " << endl;
		outfile << "Case #" << iCase+1 << ": ";

		infile >> a;
		infile >> b;

		int count = 0;
		int si = 0;

		cout << a << " " << b << endl;

		for(i=a;i<=b;i++)
		{
			si = sqrt(i);
			if(si*si == i)
			{
				if(palindrome(si) && palindrome(i))
					count++;
			}
		}

		outfile << count << endl;
		//outfile << endl;

	}

	return 0;
}
