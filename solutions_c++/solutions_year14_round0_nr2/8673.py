#include <iostream>

#include <iomanip>

#include <fstream>
using namespace std;
int main()
{
     ofstream myfile;
      ifstream infile;
      infile.open("input.in");
     myfile.open ("out.out");
     double C,X,F;


     int num1;
     infile>>num1;
     for(int i=0;i<num1;i++)
     {
         infile>>C>>F>>X;
         double  t=0 ,t1=0,t2=0;

         double rate=2.0;

         while(true)
         {
             t1=X/rate;
             t2=C/rate+X/(rate+F);
             if(t2<t1)
             {
               t=t+C/rate;
                rate=rate+F;
             }
             else
             {
                 t=t+X/rate;
                 break;
             }
         }
         myfile<< "Case #" << i+1<< ": "  << std::fixed<< setprecision(7)<<t<< endl;
     }

}
