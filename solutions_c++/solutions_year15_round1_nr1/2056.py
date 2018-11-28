//ques 1A A.

#include<iostream>
#include "conio.h"
#include<fstream>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

int main()
{
	int total,N;
	long int arr[1002]={0},diff=0,max=-1;
	long long int meth1=0,meth2=0;
	fin>>total;
	for(int i=0;i<total;i++)
	{
		fin>>N;
		meth1=0;
		meth2=0;
		max=-1;
		fin>>arr[0];
		for(int j=1;j<N;j++)
		{
			fin>>arr[j];
			diff=arr[j-1]-arr[j];
			if(diff>0)
				meth1=meth1+diff;
			if(diff>max)
				max=diff;
		}
		for(int j=0;j<N-1;j++)
		{
			if(arr[j]<max)
				meth2=meth2+arr[j];
			else
				meth2=meth2+max;
		}
		fout<<"Case #"<<i+1<<": "<<meth1<<" "<<meth2<<endl;
	}
	_getch();
	return 0;
}