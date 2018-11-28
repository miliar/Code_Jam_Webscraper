#include "stdio.h"
#include "stdlib.h"
#include <iostream>
#include <fstream>
using namespace std;

ifstream  fin("A-small-attempt0.in");
ofstream fout("A-small-attempt0.out");

int calc(int rad,int paint)
{
	int radius=rad;
	int count=0;
	while(1)
	{
		rad=1+(2*radius);
		if(rad<=paint)
		{
			count++;
			paint=paint-rad;
		}
		else
			break;
		radius+=2;
	}
	return(count);
}

int main()
{
	int T;
	fin>>T;
	int i=0;
	int res;

	int r,t;

	while(i<T)
	{
		fin>>r;
		fin>>t;
		res=calc(r,t);

		i++;

		fout<<"Case #";
		fout<<i;
		fout<<": ";
		fout<<res;
		
		if(i!=T)
		{
			 fout<<"\n";
		}
	}
	return(0);
}