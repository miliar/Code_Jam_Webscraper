#include "stdio.h"
#include "stdlib.h"
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

ifstream  fin("A-small-attempt0.in");
ofstream fout("A-small-attempt0.out");



string x;
int N;
unsigned long long func();
int find(int i);
int main()
{
	unsigned long long countit;
	int T;
	fin>>T;
	int i=0;
	while(i<T)
	{
		fin>>x;
		fin>>N;
		countit=func();
		i++;

		fout<<"Case #";
		fout<<i;
		fout<<": ";
		fout<<countit;		

		if(i!=T)
		{
			 fout<<"\n";
		}
	}
	return(0);
}
unsigned long long func()
{
	int len=x.length();

	int i;
	unsigned long long count=0;
	int chkpt;
	unsigned long long prevbig=0;
	for(i=(len-N);i>=0;i--)
	{
		chkpt=find(i);
		if(chkpt==0)
		{
			if(count==0){}
			else{count=count+prevbig;}
		}
		else
		{
			         prevbig=(1+len-i-N);
			count=count+(1+len-i-N);
		}
	}
	return(count);
}

int find(int i)
{
	int z=i+N;
	char chk;
	for(;i<z;i++)
	{
		chk=x[i];
		if(chk=='a' ||chk=='e' ||chk=='i' ||chk=='o' ||chk=='u')
		{
			return(0);
		}
	}
	return(1);
}