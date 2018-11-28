// bullseye.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<iostream>
#include<string>
#include<fstream>
#include<sstream>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	string n;
	int T;
	ofstream output;
	ifstream input;
	output.open("C:/Users/mkara_000/Downloads/karara12.in");
	input.open("C:/Users/mkara_000/Downloads/A-small-attempt0.in");

	getline(input,n);
	T = stoi(n);
	for(int i = 1 ; i <= T ; i ++)
	{
		string line;
		getline(input,line);
		string r,z;
		istringstream iss(line);
		string token;
		getline(iss,token,' ');

		r = token;
		
		getline(iss,token,' ');
		z = token;

		double R,t;
		R = stod(r);
		t = stod(z);
		double r1,r2,area;
		r1 = R;
		r2 = R + 1;
		area = (r2*r2) - (r1*r1);
		int numOfCircles = 0;
		while (area <= t)
		{
			t -= area;
			numOfCircles ++;
			r1 += 2;
			r2 = r1 + 1;
			area = (r2*r2) - (r1*r1);
			
			
		}
		output<<"Case #"<<i<<": "<<numOfCircles<<endl; 
	}

	return 0;
}

