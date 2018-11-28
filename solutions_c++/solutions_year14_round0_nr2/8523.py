#include <iostream>
#include <cmath>
#include <cctype>
#include <algorithm>
#include <sstream>
#include <vector>
#include <queue>
#include <string>
#include <stack>
#include <stdio.h>
#include <utility>
#include <iomanip>
#include <set>
#include <map>
#include <fstream>
using namespace std;
int main()
{
     ofstream oufile;
      ifstream infile;
      infile.open("B-large.in");
     oufile.open ("output-B-large.out");
     double c1,x1,f1;
     int test;

     int n;
     infile>>n;
     for(int test=0;test<n;test++)
     {
         infile>>c1>>f1>>x1;
         double  time=0 ,time1=0,time2=0;

         double rate=2.0;

         while(true)
         {
             time1=x1/rate;
             time2=c1/rate+x1/(rate+f1);
             if(time2<time1)
             {
               time=time+c1/rate;
                rate=rate+f1;
             }
             else
             {
                 time=time+x1/rate;
                 break;
             }
         }
         oufile<< "Case #" << test+1<< ": "  << std::fixed<< setprecision(7)<<time<< endl;
     }

}
