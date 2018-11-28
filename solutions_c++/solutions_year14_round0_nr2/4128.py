#include<iostream>
#include<stdio.h> 
#include<stdlib.h>
#include<fstream>
#include<set>
#include <limits>
#include<iomanip>
#include<cmath>
using namespace std;
ifstream fin("B-small-attempt3.in");
ofstream fout("B-small.attempt3.out");
int main()
{
	int n;
	double C,F,X;
	double curR,curMoney,curT,lastT,lastR,noFarmTime=0,farmTime=numeric_limits<double>::max();
	double minT=numeric_limits<double>::max();
	fin>>n;
	for(int k=0;k<n;k++)
	{
		fin>>C>>F>>X;
	//	cout<<C<<" "<<F<<" "<<X<<endl;
		curR = 2.0;
		curMoney = 0;
		curT = 0;
		lastR = 2.0;
		noFarmTime=numeric_limits<double>::max();
		farmTime=numeric_limits<double>::max();
		minT=numeric_limits<double>::max();
		for(int i=0;i<sqrt(X);i++)
		{
			curMoney = (curT - lastT) * lastR;
			noFarmTime = (X - curMoney) / lastR + curT; 
			if(curMoney >= C) 
			{
				farmTime = X / (curR) + curT;
			}
		//	noFarmTime = (X - curMoney) / lastR + curT;
		//	if(X > curMoney)
		//	farmTime = C / curR + X / (curR + F) + curT;
			if(noFarmTime > farmTime && farmTime < minT && farmTime > 0) minT = farmTime;
			else if(noFarmTime < minT && noFarmTime > 0) minT = noFarmTime; 
	//		
	//		cout<<curMoney<<" "<<noFarmTime<<" "<<farmTime<<" "<<curT<<" "<<curR<<endl;
	//		if(farmTime < noFarmTime) break;
			lastR = curR;
			curR += F;
			lastT = curT;
			curT += C / lastR;
		}
		fout<<"Case #"<<k+1<<": "<<setiosflags(ios::fixed)<<setprecision(13)<<minT<<endl;
	}
}
