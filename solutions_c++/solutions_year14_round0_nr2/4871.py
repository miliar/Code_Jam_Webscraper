// 2.CookieClickerAlpha.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
using namespace std;

double iteration(double c, double f, double x, double production){
	//direct to win
	double time1 = x/production;
	//build farm
	if(time1 > (c/production + x/(production + f)))
		return c/production + iteration(c, f, x, production+f);
	else
		return time1;
	//return (time1 < time2) ? time1:time2;
}

int _tmain(int argc, _TCHAR* argv[]){
	/*
	c = farm cost
	f = farm production
	x = win condition
	*/
	double c, f, x;
	int t;
	cin>>t;
	for(int i = 0; i < t; ++i){
		cin>>c>>f>>x;
		cout.unsetf (std::ios::floatfield);
		cout.precision(7);
		cout.setf(std::ios::fixed, std:: ios::floatfield);
		cout << "Case #" << i+1 << ": " <<  iteration(c, f, x, 2.0) << endl;
	}
}

