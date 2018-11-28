#include "stdafx.h"
#include<iostream>
using namespace std;
#include<fstream>

int _tmain(int argc, _TCHAR* argv[])
{
	long long T,m,k,r,t,area; 
	ifstream infile;
	ofstream outfile;
	infile.open("A-small-attempt0.in");
	outfile.open("output.out",ios::out);
	if(!infile||!outfile)
		cerr<<"open error";
	infile>>T;
	for(m=1;m<=T;m++)
	{
		infile>>r>>t;
		k=0;
		area=2*r+1;
		while(t-area>=0)
		{
			k++;
			t=t-area;
			area=2*r+4*k+1;
		}
		outfile<<"Case #"<<m<<": "<<k<<endl;
		cout<<"Case #"<<m<<": "<<k<<endl;
	}
	infile.close();
	outfile.close();
	return 0;
}