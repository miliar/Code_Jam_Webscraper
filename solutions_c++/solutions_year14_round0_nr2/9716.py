// Cookie clicker.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <iomanip>  

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{

	ifstream input;
	ofstream output;

	double sumtime, factories, temptime, time, c, f, x, numberofcases;

	input.open("test.txt");
	output.open("output.txt");

	if(!input||!output)
	{
		cout<<"error, file not found";
		return 0;
	}
	input>>numberofcases;
	for(int counter=0;counter<numberofcases;counter++)
	{
		input>>c>>f>>x;
		time=9999999;
		cout<<"cost=" << c<<endl;
		cout<<"production=" << f<<endl;
		cout<<"winning condition=" << x<<endl;

		sumtime=0;
		temptime=0;
		for(factories=0;time>sumtime;factories++)
		{
			temptime=sumtime+x/(factories*f+2);
			sumtime+=c/(factories*f+2);
			if(time>temptime)
				time=temptime;
			cout<<"factories=" << factories<<endl;
			cout<<"time=" << time<<endl;
			cout<<"temptime=" << temptime<<endl;
			cout<<endl;
		}

		output<<"Case #"<<counter+1<<": "<<setprecision(20)<<time<<endl;
	}
	return 0;
}
