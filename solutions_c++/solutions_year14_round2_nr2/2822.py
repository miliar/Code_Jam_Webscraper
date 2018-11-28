// may.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


#include<iostream>
#include<math.h>
#include<fstream>
using namespace std;
ifstream infile;
ofstream outputfile;
int main()
{   unsigned long long int a,b,n,k;
	infile.open("input.in", ios::in);
	outputfile.open("output.txt",ios::out|ios::trunc);
	infile>>n;
	int cas=1;
	while(infile>>a>>b>>k)
	{
		int i,j;
		unsigned long long int count=0;
		for(i=0;i<a;i++)
			for(j=0;j<b;j++)
			{
				if((i&j)<k)
				{	count++;
				}
				//outputfile<<i<<" "<<j<<"\n";

			}
			outputfile<<"Case #"<<cas<<": "<<count<<"\n";
			cas++;

	}

return 0;
}

