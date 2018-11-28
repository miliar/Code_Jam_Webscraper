// codejam1.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <fstream> 

using namespace std;
int main()
{
	std::ofstream ofs ("out.txt", std::ofstream::out);

	int t;
	cin>>t;
	for(int q = 1;q <=t;q++)
	{
		double c,f,x,time=0.0,cookies=0.0;
		double rate = 2;
		cin>>c>>f>>x;
			if(c>=x)
			{
				time = x/rate;
			}
			else
			{
				time = c/rate;
				while((x)/(rate+f) < (x-c)/rate)
				{
					rate+=f;
					time += (c/rate);
				}
				time += (x-c)/rate;
			}
			ofs.precision(numeric_limits<double>::digits10 + 1);
			ofs<<"Case #"<<q<<": "<<time<<endl;
	}
	ofs.close();
	return 0;
}
