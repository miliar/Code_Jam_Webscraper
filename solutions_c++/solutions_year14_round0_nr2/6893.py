// Cookie_Clicker_Alpha.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <sstream>
#include<vector>
#include<iomanip>
#include<iterator>
using namespace std;



double minCompletionTime2(double C, double F, double X){
	double rate =2 ;
	//30.0 2.0 100.0
	int maximFarm = int( X/C) ;
	double shortest = X/rate ;
	double farmBuilding = 0 ;
	for (int i = 1 ; i <=maximFarm; i++){
		farmBuilding+= C/(rate+i*F-F);
		double time = farmBuilding + X/(rate+i*F);      
		if (time < shortest)
			shortest = time;
		
	}
	return shortest;
/*	X/rate 100/2
    C/rate + X/(rate+F) 
	C/rate+ C/(rate+F) + X(rate+2F)
	C/rate+ C/(rate+F)+ C/(rate+F) + X(rate + 3F)
*/
}
int _tmain(int argc, _TCHAR* argv[])
{
	ifstream myReadFile ("B-large.in");
	ofstream outputFile("output.txt");

	string input;
	int numTestCase = 0 ;
	int indexTestCase = 0 ;
	if(myReadFile.is_open()){
		while(!myReadFile.eof()){
		    std::getline(myReadFile,input);
			if(input.empty())
				break;
			if(numTestCase ==0)
				numTestCase = atoi(input.c_str());
			else{ //solve this testcase
				++ indexTestCase ;
				vector<string> parameters;
				stringstream temp(input);
				copy(istream_iterator<string>(temp),
					 istream_iterator<string>(),
					 back_inserter<vector<string> >(parameters));
				double C= atof(parameters[0].c_str());
				double F = atof(parameters[1].c_str());
				double X = atof(parameters[2].c_str());
				cout<<"X is "<<X<<endl;
				double result = minCompletionTime2(C,F,X);
				outputFile<<setprecision(15)<<"Case #"<<indexTestCase<<": "<<result<<endl;
			}
		}
	}
	return 0;
}

