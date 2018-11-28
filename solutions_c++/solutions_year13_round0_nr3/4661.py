// ProbA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "fstream"
#include "math.h"

#define INFILE "C-small-attempt0.in"
#define OUTFILE "C-small.out"

using namespace std;


bool isSymmetric(int n)
{
	char str[100];
	itoa(n,str,10);
	for (int i=0, j=strlen(str)-1; i<j; i++,j--)
		if (str[i]!=str[j])
			return false;
	return true;
}

int _tmain(int argc, _TCHAR* argv[])
{
	char str[1000];	
	ifstream infile(INFILE);
	ofstream outfile(OUTFILE);
	int a,b;
	int t;
	infile>>t;
	int count;
	//infile.getline(str,1000);
	for (int i=0; i<t; i++)
	{
		infile>>a>>b;
		count = 0;
		for (int n = (int)sqrt((float)a); n*n <= b; n++)
		{
			int nn = n*n;
			if ((nn>=a) && (nn<=b))
				if (isSymmetric(n) & isSymmetric(nn))
					count++;
		}

		outfile<<"Case #"<<i+1<<": "<<count<<"\n";
	}

	infile.close();
	outfile.close();
	return 0;
}

