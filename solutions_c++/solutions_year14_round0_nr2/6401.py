// CookieClickerAlpha.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
//#pragma once

#include "targetver.h"

#include <stdio.h>
#include <tchar.h>
#include<iostream>
#include<fstream>
#include <iomanip>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("B-large.in");
	ofstream out("out.txt");
	int numTC;
	in>>numTC;
	for(int i=0;i<numTC;i++)
	{
		double c,f,x;
		double cps=2.0000000;
		c=f=x=0.0000000;
		in>>c>>f>>x;
		double mintime=0.00000000;
		while(x/cps > (c/cps + x/(cps+f)))
		{
			mintime += c/cps;
			cps += f;
		}
		mintime += x/cps;
		out.setf(ios::showpoint);
		out<<"Case #"<<i+1<<": "<<setprecision(9)<<mintime<<endl;
	}
	return 0;
}

