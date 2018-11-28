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
#include <iomanip>
#include <list>

using namespace std;

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
	int n;
	double d;

	infile >> nCase ;
	cout << "Case Num:" << nCase << endl;

	for(int iCase=0; iCase<nCase; iCase++)
	{

		cout << "Case #" << iCase+1 << ": " << endl;
		outfile << "Case #" << iCase+1 << ": ";


		infile >> n;

		list<double> vN;
		list<double> vK;
		list<double> vK1;

		int wScore = 0;
		int decwScore = 0;

		for(i=0; i<n; i++)
		{
			infile >> d;
			vN.push_front(d);
		}

		for(i=0; i<n; i++)
		{
			infile >> d;
			vK.push_front(d);
		}

		vN.sort();
		vK.sort();
		vK1 = vK;


		std::list<double>::iterator up, it;

		for(it = vN.begin(); it != vN.end(); it++)
		{
			cout <<  std::fixed << std::setprecision(7) << *it << " ";
		}
		cout << endl;
		for(it = vK.begin(); it != vK.end(); it++)
		{
			cout <<  std::fixed << std::setprecision(7) << *it << " ";
		}
		cout << endl;


		for(it = vN.begin(); it != vN.end(); it++)
		{
			up = std::upper_bound(vK.begin(), vK.end(), *it);

			if(*up < *it)	//not found
			{
				vK.erase(vK.begin());
				wScore ++;
			}
			else
			{
				vK.erase(up);
			}
		}

		for(it = vK1.begin(); it != vK1.end(); it++)
		{
			up = std::upper_bound(vN.begin(), vN.end(), *it);

			if(*up < *it)	//not found
			{
				vN.erase(vN.begin());
			}
			else
			{
				vN.erase(up);
				decwScore ++;
			}
		}


		cout << "DevWar:" << decwScore << endl;
		cout << "War:" << wScore << endl;

		outfile << decwScore << " " << wScore << endl;

		//cout << "\n    " << r << "\n*\n    " << t;
		//cout << "\n--------------------\n" << r * t << "\n\n";

		//outfile << result << endl;
		//cout << result << endl;
		//outfile << endl;

	}

	return 0;
}
