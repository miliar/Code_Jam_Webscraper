// q1.cpp : Defines the entry polong for the console application.
//



#include "stdafx.h"
#include <stdio.h>

#include <fstream>
#include <math.h>

using namespace std;




int main()
{
	long t;
	long X,Y,x,y;
	long moves;

	ifstream fp;
	ofstream fout;

	fp.open("input.txt",ios::beg);

	fout.open("output.txt",ios::beg);
	
	double result=0;
	fp>>t;
	for (long i=0; i<t; ++i)
	{
		moves=1;
		x=0;
		y=0;
		fp>>X;
		fp>>Y;
		fout<<"Case #"<<i+1<<": ";
		if(X>0)
		{
			for(int iX=0;iX<X;++iX)
				fout<<"WE";
		}
		if(X<0)
		{
			for(int iX=0;iX<(abs(X));++iX)
				fout<<"EW";
		}
		if(Y>0)
		{
			for(int iY=0;iY<Y;++iY)
				fout<<"SN";
		}
		if(Y<0)
		{
			for(int iY=0;iY<(abs(Y));++iY)
				fout<<"NS";
		}
				
		

		
		
		fout<<endl;
	}
	fp.close();
	fout.close();
}
