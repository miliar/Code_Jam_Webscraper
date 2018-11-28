#include <iostream>
#include <algorithm>
#include <sstream>
#include <stdio.h>
#include <iomanip>
#include <fstream>

using namespace std;

int main()
{
     ofstream myfile;
      ifstream infile;
      infile.open("input.in");
     myfile.open ("out.out");
     double cr,xr,fr;

     int num;
     infile>>num;
     for(int test=0;test<num;test++)
     {
         infile>>cr>>fr>>xr;
         double  time=0 ,time1=0,time2=0;

         double rate=2.0;

         while(1)
         {
             time1=xr/rate;
             time2=cr/rate+xr/(rate+fr);
             if(time2<time1)
             {
               time=time+cr/rate;
                rate=rate+fr;
             }
             else
             {
                 time=time+xr/rate;
                 break;
             }
         }
         myfile<< "Case #" << test+1<< ": "  << std::fixed<< setprecision(7)<<time<< endl;
     }

}
