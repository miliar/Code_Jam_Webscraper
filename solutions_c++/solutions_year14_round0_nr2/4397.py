#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;
#define ll long long
#define pb push_back 


int main()
{
   int T;
   cin >> T;

   double C, F, X;
   for(int j=0; j!=T; j++)
   {
      double time= 0;

      cin >> C >> F >> X;

      if(C< X)
      {
	 double max= (X/ C- 2/ F- 1);
	 const int floorMax= floor(max);
	 const int  ceilMax= floorMax+ 1;
	 if(floorMax >= 0)
	 {
	    for(int k=0; k<=floorMax; k++)
	    time+= C/ (2+ F* k);
	    time+= X/ (2+ F* ceilMax);
	 }
	 else
	 {
	    time= X/ (2);
	 }
      }
      else time= X/ (2);

      printf("Case #%d: %.7f\n", j+ 1, time);
   }

   return 0;
}

