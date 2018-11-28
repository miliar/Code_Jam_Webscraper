// codejam2015r1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
//#include "ifstream"
//#include "ofstream"

using namespace std;

int main()
{
	ifstream fin;
	ofstream fout;
	fin.open ("A-large.in");
	fout.open ("output.txt");

	int t, smax, ss;
	string s;
	fin>> t;

	for(int ii=1;ii<=t;ii++)
	{
		fin>>smax>>s;

		int friends=0, counter=0;

		for(int i=0;i<=smax;i++)
		{
			ss = s[i] - '0';
			if((i>counter + friends ) && s[i] != '0')	friends = (i - counter); 
			counter += ss;			
		}
		
		fout<<"Case #"<<ii<<": "<<friends<<endl;
			
	}

	return 0;
}

