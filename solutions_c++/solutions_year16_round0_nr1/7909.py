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

int d[10];


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
	unsigned long long ndiv, ans;
	int nrem;

	infile >> nCase ;
	cout << "Case Num:" << nCase << endl;

	for(int iCase=0; iCase<nCase; iCase++)
	{
		cout << "Case #" << iCase+1 << ": ";
		outfile << "Case #" << iCase+1 << ": ";

		memset(d, 0, sizeof(int)*10);

		infile >> n;
		cout << n << endl;

		if(n == 0)
		{
			cout << "INSOMNIA" << endl;
			outfile << "INSOMNIA" << endl;
			continue;
		}

		int p = 1;
		ans = 0;

		while(1)
		{
			ndiv = n*p;
			while(ndiv != 0)
			{
				nrem = ndiv % 10;
				d[nrem] = 1;
				for(j=0;j<10;j++)
				{
					if(d[j]==0)
						break;
				}
				if(j==10)
				{
					ans = n*p;
					cout << ans << endl;
					outfile << ans << endl;
					break;
				}
				ndiv = ndiv / 10;
			}
			if(ans != 0)
				break;
			p++;
		}



		//cout << "\n    " << r << "\n*\n    " << t;
		//cout << "\n--------------------\n" << r * t << "\n\n";

		//outfile << result << endl;
		//cout << result << endl;
		//outfile << endl;

	}

	return 0;
}
