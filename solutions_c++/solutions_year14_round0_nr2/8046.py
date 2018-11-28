#include "stdafx.h"
#include <fstream>
#include <iomanip>
using namespace std;
const int b=2;
int _tmain(int argc, _TCHAR* argv[])
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int t;
	long double c,f,x;
	fin>>t;
	long double time_farm,prod,time_x,time_com,newtime_com;
	for(int i=0;i<t;i++)
	{
		fin>>c>>f>>x;
		time_farm=0,prod=b,time_x=x/b,newtime_com=x/b;
		do
		{
			time_com=newtime_com;
			time_farm=time_farm+c/prod;
			prod=prod+f;
			time_x=x/prod;
			newtime_com=time_farm+time_x;
		}
		while(newtime_com<time_com);
		fout<<"case #"<<i+1<<": ";
		fout<<setprecision(10)<<time_com<<endl;
	}
	return 0;
}