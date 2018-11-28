// Prob1A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "fstream"
using namespace std;
const double PI  =3.141592653589793238462;

#define INFILE "A-small-attempt0.in"
#define OUTFILE "A-small.out"

int _tmain(int argc, _TCHAR* argv[])
{
	char str[1000];	
	ifstream infile(INFILE);
	ofstream outfile(OUTFILE);
	
	int t,r,n,count;
	infile>>n;
	double firstRing;
	//infile.getline(str,1000);
	for (int i=0; i<n; i++)
	{
		count = 0;
		infile >>r>>t;
		firstRing = 2*r+1;
		while (t>=firstRing)
		{
			count++;
			t-=firstRing;
			firstRing+=4;
		}
		outfile<<"Case #"<<i+1<<": "<<count<<"\n";
	}


	infile.close();
	outfile.close();
	return 0;
}

