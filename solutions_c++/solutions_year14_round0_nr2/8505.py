#include <iostream>
#include <stdio.h>

using namespace std;



void tcase()
{


   double c,f,x;


   cin >> c;
   cin >> f;
   cin >> x;

   double upperBound = x/2;
   double time = 0;


   double timePerFarm = c/2;

   

   double farms = 1;
   double farmBuyTime = 0; 

   double overAll = upperBound;

   do{

      upperBound = overAll;
      farmBuyTime += timePerFarm;
      overAll = farmBuyTime + (x/(2 + (f*farms))); 
      timePerFarm = c/(2 + (f*farms));
      ++farms;
   }
   while(overAll < upperBound);



   printf("%.7f\n", upperBound);

   return;

}

int main(int argc, char* argv[])
{


   int t;
   cin >> t;


   for(int l = 0; l < t; ++l)
   {

      cout << "Case #" << l+1 << ": ";
      tcase();

   }



   return 0;
}
