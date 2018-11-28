#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
#include <fstream>
#include<iomanip>
using namespace std;
int main()
{
	double T,C,F,X,time,cookies,rate;
	double minTime; //Miinimum Time requred to use a farm to recover the cookies spent
	int i,j,k;
	freopen("B-large.in","r",stdin);freopen("practice_large_out.out","w",stdout);
	cin>>T;
	for(i = 0;i < T;i++)
    {   cookies = 0.000000;
        rate = 2.000000;
        time = 0.0000000;
		cin>>C>>F>>X;
		minTime = (double)C/(double)F;
		while(1)
		{ time = time + (double)C/(double)rate;
          
		  if((double)X/(rate+F) > minTime)
		  {rate = rate + F;
		  }
	      else
	      break;
		}
		time = time + (double)(X-C)/rate;
		std::cout << std::setprecision(7) << std::fixed;
		cout<<"Case #"<<i+1<<": "<<time<<endl;
    }
	return 0;
}
