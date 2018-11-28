#include<iostream>
#include<conio.h>
#include<string.h>
#include<fstream>
#include<string>
#include<vector>
#include<utility>
#include<iomanip>
using namespace std;
void main()
{
	ifstream fin;
	ofstream fout;
	fin.open("B-large (1).in");
	fout.open("blaa.out");
	long double T,C,F,X,p=2,s,c1=0,s1=0;
	fin>>T;
	for(int i=1;i<=T;i++)
	{c1=0;p=2;
	fin>>C>>F>>X;
	here:
	s=c1+X/p;
	c1=c1+C/p;
	p=p+F;
	s1=c1+X/p;
	if(s<=s1)
	{fout.setf(ios::fixed);
		fout<<"Case #"<<i<<": "<<setprecision(10)<<s<<"\n";
	}
	else
	{
		goto here;
	}
	}
}