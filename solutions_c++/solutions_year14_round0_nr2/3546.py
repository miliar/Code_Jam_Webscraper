#include <iostream>
#include <string>
#include <stdio.h>
#include <algorithm> // binsearch,max(a,b),min(a,b)
#include <math.h> 
#include <queue>
#include <vector>
#include <set>
#include <list>
#include <map> 
#include <string.h> // memset
#include <cstdlib> // abs(int),labs(int),llabs(int),min,max
#include <limits.h> // int_max,int_min,long_long_max,long_long_min
#define EPS 0.00000001
using namespace std;
double apsi(double a)
{
    if(a>=0) return a;
    return -1.0*a;
}
int main()
{
  double baseTime = 0,C,F,X;
  int test;
  cin>>test;
  for(int i=1;i<=test;i++)
  {
    cin>>C>>F>>X;
    baseTime = X/2.0;
    double minTime = baseTime;
    double currBaseTime;
    double travelTime;
    currBaseTime = 0;
    double speed = 2.0;
    travelTime = X/2.0;
    double prev = 0;
    while(currBaseTime <= baseTime){
    double possibleTime = travelTime + currBaseTime;
    baseTime = min(possibleTime,baseTime);
    prev = possibleTime; 
    minTime = min(possibleTime,minTime);
    currBaseTime += C/speed;
    speed += F;
    travelTime = X/speed;
    }
  printf("Case #%d: %.7lf\n",i,minTime);
  }
	return 0;	
}
