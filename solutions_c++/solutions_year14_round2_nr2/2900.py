//============================================================================
// Name        : lottaery.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>


using namespace std;
ofstream fout("output.txt");
ifstream fin("inp.txt");
int main() {
	long long a,b,k,i,j,n,res=0;
	int test,ilt;
	fin>>test;
	for(ilt=1;ilt<=test;ilt++)
	{
		fin>>a>>b>>k;
		for(i=0;i<a;i++)
		{
			for(j=0;j<b;j++)
			{
				n=i&j;
				if(n<k)
				{	//fout<<"\ni= "<<i<<" j="<<j<<" n="<<n;
					res++;

				}
			}
		}

		fout<<"\nCase #"<<ilt<<": "<<res;
		res=0;
	}
	return 0;
}
