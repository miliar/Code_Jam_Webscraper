// codejam.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <set>
using namespace std;


void MagicTrick()
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
}

void CokieClickerAlpha(){
	ofstream answer;
	ifstream myfile;
	answer.open("outputs/Banswer2.txt");
  myfile.open ("inputs/B-large.in");
	int numtestcases;
  myfile >> numtestcases;
	cout << numtestcases;
	answer.precision(50);
	
	for(int i=0;i<numtestcases;i++) {
		long double C, F, X;
		long double rate = 2.0;

		myfile >> C >> F >> X;
		long double best = 999999999999;
		long double time = 0.0;
		long double score = 0.0;
		long double nextFarmPurchase;
		long double notBuyingFarms;
		while(true)
		{
			notBuyingFarms = (X)/rate + time;
			if(best < notBuyingFarms)
				break;
			else
				best = notBuyingFarms;

			nextFarmPurchase= (C)/rate;
			time += nextFarmPurchase;
			//score -= C;
			rate += F;
			//cout << time << "\n";
		}
		// buy a farm
		answer << "Case #" << (i+1) << ": " << best << "\n";
	}
    myfile.close();
	  answer.close();
}

int _tmain(int argc, _TCHAR* argv[])
{ 
	CokieClickerAlpha();
	//cin >> x;
	return 0;
}

