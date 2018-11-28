/*
 * sample.cpp
 *
 *  Created on: Apr 11, 2015
 *      Author: ttcn
 */

#include <stdio.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <stdlib.h>
#include <algorithm>
#include <sstream>

using namespace std;

int main()
{
	fstream infile,outfile;
	infile.open("C-small-attempt2.in", ios::in );
	outfile.open("C-small-attempt2.out", ios::out | ios::trunc );

	int numOfinputs = 0;

	infile>>numOfinputs;
    cout<<"numOfinputs:" << numOfinputs << endl;

    int I=2,J=3,K=4;

    int qTable [][4] = {{1, I, J, K},
    					{I, -1, K, -1*J},
    					{J, -1*K, -1, I},
    					{K, J, -1*I, -1}
    					};

	for(int i=0; i<numOfinputs; i++)
	{
		int L;
		unsigned long long X;
		string qString;


		infile >> L >> X;
		infile >> qString;

		outfile << "Case #" << i+1 << ": ";
		int multiplier = 1;
		unsigned long long j;
		bool oIsFound = false;

		for(j=0; j < (L * X); j++)
		{
			int sign = multiplier < 0 ? -1:1;

			multiplier = sign * qTable[abs(multiplier)-1] [qString[j%L]-'i'+1];
			if (multiplier == I)
			{
				oIsFound = true;
				j++;
				break;
			}
		}

		if(oIsFound)
		{
			oIsFound = false;
			multiplier = 1;
			for(;j < (L * X); j++)
			{
				int sign = multiplier < 0 ? -1:1;

				multiplier = sign * qTable[abs(multiplier)-1] [qString[j%L]-'i'+1];
				if (multiplier == J)
				{
					oIsFound = true;
					j++;
					break;
				}
			}
		}

		if(oIsFound)
		{
			oIsFound = false;
			multiplier = 1;
			for(;j < (L * X); j++)
			{
				int sign = multiplier < 0 ? -1:1;

				multiplier = sign * qTable[abs(multiplier)-1] [qString[j%L]-'i'+1];
			}

			if (multiplier == K)
			{
				oIsFound = true;
			}
		}


		if(oIsFound)
			outfile<<"YES"<<endl;
		else
			outfile<<"NO"<<endl;
	}

	return 1;
}


