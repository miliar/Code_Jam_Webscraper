//============================================================================
// Name        : Cookie.cpp
// Author      : Moustafa Mohamed Ali
// Version     :
// Copyright   : 2014
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <bits/stdc++.h>

using namespace std;

int main() {
	freopen("B-large.in","r",stdin);
	freopen("output.in","w",stdout);
	cout.precision(15);
	int nTestCases ;
	cin>>nTestCases;
	for (int i = 1 ; i <= nTestCases ; ++i  ){
		long double c , f, x , crntProduction = 2.000000 ;
		bool lessTimeExist = true ;
		cin>>c>>f>>x;
		long double finalTime = x / crntProduction ;
		long double timeToBuyNewFarm = 0.00 ;
		while (lessTimeExist ){
			timeToBuyNewFarm += c / crntProduction ;
			crntProduction += f ;
			double netTimeToReachX = x /crntProduction;
			double totalTime = timeToBuyNewFarm + netTimeToReachX ;
			if (totalTime < finalTime )
				finalTime = totalTime ;
			else
				lessTimeExist = false ;
		}
		cout<<"Case #"<<i<<": "<<finalTime<<endl;
	}
	return 0;
}
