
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string>
#include <cstring>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;

double time[100000];
double farm[100000];

int main()
{
	ifstream fin;
	fin.open("B-large.in");
	ofstream fout;
	fout.open("B-large.out");
	int t;
	fin>>t;
	double c, f, x;
	for(int n = 0; n<t; n++)
	{
		memset(time, 0.0, 100000*sizeof(double));
		memset(farm, 0.0, 100000*sizeof(double));
		fin>>c>>f>>x;
		time[0] = x/2;
		farm[0] = 0;
		double mintime = time[0];
		for(int i = 1; i<x; i++)
		{
			if(farm[i] > mintime)
				break;
			farm[i] = farm[i-1] + c/(2+(i-1)*f);
			time[i] = farm[i] + x/(2+i*f);
			if(time[i] < mintime)
				mintime = time[i];
		}
		fout.precision(7);
		fout.setf(ios::fixed);
		fout<<"Case #"<<n+1<<": "<<mintime<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}

