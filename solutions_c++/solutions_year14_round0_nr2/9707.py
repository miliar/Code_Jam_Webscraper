#include <iostream>
#include "stdio.h"
#include "stdlib.h"
#include <fstream>
#include <string>
#include <algorithm>
#include <iomanip>      // std::setprecision
using namespace std;


ifstream  fin("B-small-attempt0.in");
ofstream fout("B-small-attempt0.out");
 
int N;  
double min_time_to_complete;
int myfunc(double speed_coming_in,double time_coming_in);
double C,F,X;


int main()
{
   int T;
	fin>>T;
	int i=0;
	int res;

	 
	int x,y;
	while(i<T)
	{
		min_time_to_complete=-1.0;
		fin>>C;
		fin>>F;
		fin>>X;
	 
		 
		i++;

		fout<<"Case #";
		fout<<i;
		fout<<": ";
		
		myfunc(2.0,0.0);
		fout << setprecision(7) << fixed <<  min_time_to_complete; //Outputs 12.457
		 
		if(i!=T)
		{
			 fout<<"\n";
		}
	}
	return(0);
}
int myfunc(double speed_coming_in,double time_coming_in)
{
	double timefull=double((double(double(X)/double(speed_coming_in)))+(double(time_coming_in)));   //change this later
	if(min_time_to_complete==-1.0){min_time_to_complete=double(timefull);}
        if(timefull<min_time_to_complete){min_time_to_complete=double(timefull);}
	
	//Spd inc
	double xtratime=0.0+(double(time_coming_in))+(double(double(C)/speed_coming_in));
	if(xtratime>min_time_to_complete){return(-1);}
	myfunc(double(speed_coming_in+F+0.0),xtratime);
}


 
