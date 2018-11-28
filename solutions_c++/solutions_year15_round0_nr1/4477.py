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
	infile.open("A-large.in", ios::in );
	outfile.open("A-large.out", ios::out | ios::trunc );

	int numOfinputs = 0;

	infile>>numOfinputs;
    cout<<"numOfinputs:" << numOfinputs << endl;

    char newline;
    infile.get(newline);

	for(int i=0; i<numOfinputs; i++)
	{
		int Smax;
		string Sindex;

		infile >> Smax;
		cout << Smax <<endl;
		infile >> Sindex;
		cout << Sindex <<endl;

		outfile << "Case #" << i+1 << ": ";

		int StandupAudi = 0;
		int NeededAudi = 0;
		for(int j=0; j <Sindex.length(); j++)
		{
			if(j <= StandupAudi)
			{
				//new will standup
				StandupAudi += Sindex[j] - '0';
			}
			else if(Sindex[j] != '0')
			{
				int currNeed = (j - StandupAudi);
				StandupAudi += (currNeed + Sindex[j] - '0');
				NeededAudi += currNeed;
			}
		}
		cout<<NeededAudi<<endl;
		outfile<<NeededAudi<<endl;
	}

	return 1;
}


