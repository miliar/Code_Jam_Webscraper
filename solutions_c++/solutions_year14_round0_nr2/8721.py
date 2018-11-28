//============================================================================
// Name        : coocki.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include<limits>
#include <fstream>
using namespace std;
ofstream fout("output2.txt");
ifstream fin("B-large.in");
int main() {
	int test,i,j;
	double c,f,x,r,sec,sec2,secb;
    fout.precision(std::numeric_limits<double>::digits10);
	fin>>test;
	for(i=1;i<=test;i++)
		{sec=0.0;r=2.0;
		//	cout<<" \nc1\n";
			fin>>c>>f>>x;
			while(1)
			{
				sec2=x/r;
				secb=(c/r)+(x/(r+f));
				if(sec2<secb)
				{
					sec+=sec2;
				//	cout<<"+"<<sec;
					break;
				}
				else
				{
					sec=sec+c/r;
				//	cout<<"-"<<sec;
					r+=f;
				}
			}
		fout<<"\nCase #"<<i<<": "<<sec;
		}

	return 0;
}
