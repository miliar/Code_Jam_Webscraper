// codejam.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <algorithm>
#include <functional>
#include <string>
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


void War()
{
	const int MAX_SIZE = 1000;
	ofstream answer;
	ifstream myfile;
	myfile.precision(50);
	answer.precision(50);
	cout.precision(50);
	answer.open("outputs/Danswer2.txt");
	myfile.open ("inputs/D-large.in");
	int numtestcases;
	myfile >> numtestcases;
	//cout << "cases " << numtestcases << "\n";
	for(int i=0;i<numtestcases;i++) {
		int numblocks;
		long double naomi[MAX_SIZE];
		long double ken[MAX_SIZE];
		myfile >> numblocks;
		//cout << "numblocks " << numblocks << "\n";
		for(int j=0;j<numblocks;j++){
			int tmp;
			myfile >> naomi[j];//tmp;
			//naomi[j] = tmp;
			//naomi.push_back(tmp);
		}
		for(int j=0;j<numblocks;j++){
			int tmp;
			myfile >> ken[j]; //tmp;
			//ken[j] = tmp;
			//ken.push_back(tmp);
		}
		sort(naomi, naomi + numblocks);
		sort(ken, ken+numblocks);
		//vector<long double> naomi(anaomi);
		//vector<long double> ken(aken);
		//sort(naomi,naomi + 40);
		//sort(ken,ken + 40);

		//vector<long double> wnaomi(naomi);
		//vector<long double> wken(ken);
		bool wkused[MAX_SIZE];
		for(int j=0;j<numblocks;j++)
		{
			wkused[j] = false;
		}

		//war
		int wscore=0;
		for(int j=0;j<numblocks;j++)
		{

			//int wchoose = naomi[j];
			//wnaomi.pop_back();
			int ilowest=-1;
			int llowest=-1;
			for(int k=0;k<numblocks;k++)
			{
				//cout << naomi[j] << " " << ken[k] << "\n"; 
				if(!wkused[k])
				{
					if(naomi[j] <ken[k] && (ilowest == -1 || ken[k] < ken[ilowest]))

						ilowest=k;
					else if(llowest == -1 || ken[k] < ken[llowest])
						llowest =k;
				}
			}
			if(ilowest != -1)
			{
				wkused[ilowest] = true;
			}
			else
			{
				wkused[llowest] = true;
				wscore++;
			}
		}

		//dwar
		int dscore =0;

		for(int j=0;j<numblocks;j++)
		{
			wkused[j] = false;
		}

		for(int j=numblocks-1;j>=0;j--)
		{

			//int wchoose = naomi[j];
			//wnaomi.pop_back();
			int ilowest=-1;
			int llowest=-1;
			//cout << "START\n";
			for(int k=numblocks-1;k>=0;k--)
			{
				//cout << naomi[k] << " " << ken[j] << "\n"; 
				if(!wkused[k])
				{
					if(naomi[k] > ken[j] && (ilowest == -1 || naomi[k] < naomi[ilowest]))
						ilowest=k;
					else if(llowest == -1 || naomi[k] < naomi[llowest])
						llowest =k;
				}
			}
			if(ilowest != -1)
			{
				wkused[ilowest] = true;
				dscore++;
			}
			else
			{
				wkused[llowest] = true;
			}
		}
		answer << "Case #" << (i+1) << ": " << dscore << " " << wscore << "\n";
	}

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

void TheRepeater()
{
	ofstream answer;
	ifstream myfile;
	answer.open("outputs/Aanswer0.txt");
	myfile.open ("inputs/A-small-attempt0.in");
	int numtestcases;
	myfile >> numtestcases;
	cout << numtestcases;
	//answer.precision(50);

	for(int i=0;i<numtestcases;i++) {
		int numStrings;

		myfile >> numStrings;
		int moves=0;
		string strs[100];
		for(int j=0;j<numStrings;j++)
		{
			myfile >> strs[j];
		}

		//for(int j=0;j<numStrings;j++)
		//{
		//
		//}

		answer << "Case #" << (i+1) << ": ";
		answer << moves << "\n";
	}
	myfile.close();
	answer.close();
}

void Loto()
{
	ofstream answer;
	ifstream myfile;
	answer.open("outputs/Banswer1.txt");
	myfile.open ("inputs/B-small-attempt1.in");
	int numtestcases;
	myfile >> numtestcases;
	cout << numtestcases;
	//answer.precision(50);

	for(int i=0;i<numtestcases;i++) {
		unsigned long long A,B,K;
		myfile >> A >> B >> K;
		unsigned long long ans=0;
		//cout << i << "\n";
		for(int j=0;j<B;j++)
		{
			for(int k=0;k<A;k++)
			{
				int m = j&k;
				if(m < K )
				{
					ans++;
//if(i==0)
//{
//	cout << "good {" << j << "," << k << "}\n";
//}
				}
			//	else
			//		if(i==0)
			//			cout << "bad {" << j << "," << k << "}\n";
			}
		}

		answer << "Case #" << (i+1) << ": ";
		answer << ans << "\n";
	}
	myfile.close();
	answer.close();
}
int _tmain(int argc, _TCHAR* argv[])
{ 
	Loto();
	//int x;
	//cin >> x;
	return 0;
}

