 
#include <iostream>
#include<iomanip>
#include <string>
#include <cmath>
using namespace std;

int main()
{
	
	std::cout << std::setprecision(7) << std::fixed;
   int T;
   cin>>T;
   
   for(int l1=0;l1<T;l1++)
   {
	
	  double C,X,F,rate=2;
	   cin>>C>>F>>X;
	  
	   int n=(int)((double)X/C-(double)rate/F);
	   if(n<0) n=0;
	   double time= X/(n*F + (double) rate);
	   for(int l2=0;l2<n;l2++)
	   {
		   time+=C/(rate+l2*F);
	   }
	   cout<<"Case #"<<l1+1<<": "<<time<<endl;
   }
  
    return 0;
}