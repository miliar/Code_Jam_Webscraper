#include <math.h>
#include<iostream>
#include<fstream>
#include<sstream>
using namespace std;
void main()
{
	ifstream in("smallinput.in",ios::in);
	ofstream out("smalloutput.txt",ios::out);
	int numofCases;
	in>>numofCases;
	for(int index=0;index<numofCases;index++)
	{
		double r,t;
		in>>r>>t;
		double k=floor(((-2*r+1)+sqrt((2*r-1)*(2*r-1)+8*t))/4);
		if((2*k*k+(2*r-1)*k)>t)
			k=k-1;
		long inte=k;
		stringstream stream;
		stream<<k;
		out<<"Case #"<<index+1<<": "<<inte<<endl;
	}
}