#include<iostream>
#include <limits>
#include<iomanip>

typedef std::numeric_limits< double > dbl;
using namespace std;

int main()
{
  int testcases;
  cin>>testcases;
  
  for(int t=0;t<testcases;t++)
  {
    double result=0.0000000;
    double c,f,x;
    cin>>c>>f>>x;
    double initialcookies =2.0000000;
    double prevcalcValue = 0.0000000;
    double fixedTime = 0.0000000;
    double currentCookies = initialcookies;
    double increment = 0.0000000;
    int counter =0;
    prevcalcValue = x/currentCookies;
    //Actual Algo
    while(result<prevcalcValue)
    {
	 counter++;
	   /*if(result<prevcalcValue)
	   {
		prevcalcValue = result;
	   }
	   else
	   {
		break;
	   }*/
	   increment += c/currentCookies;
	   	 currentCookies += f;
	 fixedTime = x/currentCookies;
	 result = fixedTime+increment;
	 if(result<prevcalcValue)
	 {
	   prevcalcValue = result;
	   result = 0.0;
	 }
	   
	 //cout<<result<<"\n";
    }
    //cout<< setprecision(16);
    cout<<"Case #"<<t+1<<": "<<fixed<<setprecision(14)<<prevcalcValue<<"\n";
  }
}