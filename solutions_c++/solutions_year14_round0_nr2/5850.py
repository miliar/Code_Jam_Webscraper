#include <stdio.h>
#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

void main()
{
 	fstream fin;
	fin.open("problem1.in",ios::in);
	fstream fout;
	fout.open("output1.out",ios::out);
	int testCases=0;
	fin>>testCases;
	
	for(int i=1;i<testCases+1;i++){
	double total=0;
	double rate=2;
	double C,F,X;
	fin>>C>>F>>X;
	double totalTime=0;
	
		while(X/rate > (X/(rate+F))+(C/rate))
		{
				totalTime+=C/rate;
				rate+=F;

		}
		totalTime+=X/rate;

		
		

	fout<<"case #"<<i<<": ";
	fout<< setprecision(12)<<totalTime<<endl;
	}
}