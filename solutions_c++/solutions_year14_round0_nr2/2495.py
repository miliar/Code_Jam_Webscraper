#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
#include<iostream>
#include<fstream>
#include<iomanip>

int main() 
{
	ifstream fpInput("C:\\Users\\ametpall\\Downloads\\B-large.in", ios::in);
	ofstream fpOutput("C:\\Res.txt", ios::out);
	int tc; fpInput>>tc;
	for(int tci = 0; tci < tc; tci++) 
	{
		fpOutput<<"Case #"<< tci+1<<": ";
		
		double lItemspersecond = 2;
		double dFamrCost ,  dNeeded , lFarmspersec;
		fpInput>>dFamrCost>>lFarmspersec>>dNeeded;
		 long double sume = 0;		 
		  double dTimeWithoutFarm,dTimeBuyFarm,dTimeWithFarm;
		 while(true)
		 {
			 dTimeWithoutFarm = dNeeded/lItemspersecond;

			 dTimeBuyFarm = dFamrCost/lItemspersecond;
			 lItemspersecond += lFarmspersec;
			 dTimeWithFarm = dTimeBuyFarm + dNeeded/lItemspersecond;

			 if(dTimeWithFarm > dTimeWithoutFarm)
			 {
				 sume += dTimeWithoutFarm;
				 break;		
			 }
			 else
			 {
				 sume += dTimeBuyFarm;
			 }
		 }
		
		fpOutput<<fixed<<setprecision(7)<< sume <<"\n";

	}
	
	 return 0;
}