//=====================7=======================================================
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
//#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <stdarg.h>
#include <gmpxx.h>

using namespace std;

int N[26];


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

	int i,j;
	unsigned int n;
	int p, total;
	int max, maxIndex, door;
	char c;

	infile >> nCase ;
	cout << "Case Num:" << nCase << endl;

	for(int iCase=0; iCase<nCase; iCase++)
	{
		cout << "Case #" << iCase+1 << ": ";
		outfile << "Case #" << iCase+1 << ": ";

		memset(N, 0, sizeof(int)*26);

		infile >> n;
		cout << n << endl;

		total = 0;
		for(i=0; i<n; i++)
		{
			infile >> p;
			N[i] = p;
			total += p;
		}

		max = -1;
		door = 0;
		while(1)
		{
			for(i=0; i<n; i++)
			{
				if(max < N[i])
				{
					max = N[i];
					maxIndex = i;
				}
			}

			c = 'A'+ maxIndex;
			cout << c;
			outfile << c;
			N[maxIndex]--;
			total--;
			door++;
			max = -1;

			if(door>=2 || (door==1&&total==2) )
			{
				cout << ' ';
				outfile << ' ';
				door = 0;
			}

			if(total <= 0)
				break;
		}

		cout << endl;
		outfile << endl;

		//cout << "\n    " << r << "\n*\n    " << t;
		//cout << "\n--------------------\n" << r * t << "\n\n";

		//outfile << result << endl;
		//cout << result << endl;
		//outfile << endl;

	}

	return 0;
}
