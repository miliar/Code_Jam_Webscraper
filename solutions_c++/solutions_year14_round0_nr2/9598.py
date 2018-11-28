/* 
 * File:   main.cpp
 * Author: zviad
 *
 * Created on December 5, 2012, 12:08 AM
 */

#include <cstdlib>
#include <math.h>
#include <iostream>
#include <stdio.h>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <map>
using namespace std;


long double f;
long double c;
long double x;


long double getTime(long farmCnt){
    long double secs=0;
    for(long i=0;i<farmCnt;i++){
        secs=secs+c/(2+i*f);
    }
    secs=secs+x/(2+farmCnt*f);
    return secs;
}

int main() {    
   int t;long farmcnt=0;
   freopen("input.txt", "rt", stdin);
   freopen("output.txt", "wt", stdout);
   cin>>t; 
   
   for(int tt=0;tt<t;tt++){
       cin>>c>>f>>x;
       farmcnt=0;
       while(getTime(farmcnt)>getTime(farmcnt+1)){
           farmcnt++;
       }
//       cout.fixed;
//       cout<<"Case #"<<tt+1<<": "<<getTime(farmcnt)<<"\n";
       printf("Case #%d: %.7Lf\n",tt+1, getTime(farmcnt));

   }     
   return 0;
}



