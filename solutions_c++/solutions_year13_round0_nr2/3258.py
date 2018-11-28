/*
 * solb.cpp
 *
 *  Created on: Apr 13, 2013
 *      Author: ben
 */

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

int lawn[100][100];
int colMax[100], rowMax[100];

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

	int i,j,m,n;
	bool ok;

	infile >> nCase ;
	//cout << "Case Num:" << nCase << endl;

	for(int iCase=0; iCase<nCase; iCase++)
	{
		cout << "Case #" << iCase+1 << ": " << endl;
		outfile << "Case #" << iCase+1 << ": ";

		infile >> m;
		infile >> n;

		ok = true;

		memset(lawn,0,sizeof(int)*100*100);
		memset(colMax,0,sizeof(int)*100);
		memset(rowMax,0,sizeof(int)*100);

		for(i=0; i<m; i++)
		{
			for(j=0; j<n; j++)
			{
				infile >> lawn[i][j];
				//cout << lawn[i][j];

				if(lawn[i][j] > rowMax[i])
					rowMax[i] = lawn[i][j];

				if(lawn[i][j] > colMax[j])
					colMax[j] = lawn[i][j];
			}
			//cout << endl;
		}

		for(i=0; i<m; i++)
		{
			for(j=0; j<n; j++)
			{
				if(lawn[i][j]<rowMax[i] && lawn[i][j]<colMax[j])
					ok = false;
			}
		}

		if(ok)
		{
			outfile << "YES" << endl;
			cout << "YES" << endl;
		}
		else
		{
			outfile << "NO" << endl;
			cout << "NO" << endl;
		}
		//outfile << count << endl;
		//outfile << endl;

	}
	outfile << endl;

	return 0;
}



