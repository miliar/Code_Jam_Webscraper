// codejam.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <set>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{ 
	ofstream answer;
	ifstream myfile;
	answer.open("outputs/answer.txt");
  myfile.open ("inputs/A-small-attempt0.in");
	int numtestcases;
  myfile >> numtestcases;
	cout << numtestcases;
	for(int i=0;i<numtestcases;i++) {
		int firstans;
		myfile >> firstans;
		int firstarr[4][4];
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				myfile >> firstarr[j][k];

		
		int secondans;
		myfile >> secondans;
		int secondarr[4][4];
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				myfile >> secondarr[j][k];

		answer << "Case #" << (i+1) << ": ";

		int potans=0;
		int ans=0;
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				if(firstarr[firstans-1][j] == secondarr[secondans-1][k])
				{
					potans++;
					ans = firstarr[firstans-1][j];
				}
			}
		}

		if(potans == 0)
			answer << "Volunteer cheated!\n";
		else if(potans == 1)
			answer << ans << "\n";
		else if(potans > 1)
			answer << "Bad magician!\n";
	}
  myfile.close();
	answer.close();
	int x;
	//cin >> x;
	return 0;
}

