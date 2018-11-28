#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
#include<iostream>
#include<fstream>
#include<iomanip>

int main() 
{
	ifstream fpInput("C:\\Users\\ametpall\\Downloads\\D-large.in", ios::in);
	ofstream fpOutput("C:\\Res.txt", ios::out);
	int tc; fpInput>>tc;
	for(int tci = 0; tci < tc; tci++) 
	{
		fpOutput<<"Case #"<< tci+1<<": ";
		long lCount = 0;
		fpInput>>lCount;

		vector<double>vFirst,vFFirst;
		vector<double>vSecond,vSSecond;
		for(long lIndex = 0; lIndex< lCount;lIndex++)
		{
			double dTemp;
			fpInput>>dTemp;
			vFirst.push_back(dTemp);
		}
		for(long lIndex = 0; lIndex< lCount;lIndex++)
		{
			double dTemp;
			fpInput>>dTemp;
			vSecond.push_back(dTemp);
		}
		sort(vFirst.begin() , vFirst.end());
		sort(vSecond.begin() , vSecond.end());
		
		vFFirst = vFirst;
		vSSecond = vSecond;
		long lCheatPoints = 0 , lOptimalPoints = 0;
		
		vector<double>::iterator it;
		while((it = vSecond.begin()) != vSecond.end())
		{			
			vector<double>::iterator itInner;
			bool bFoundMinimum = false;
			for(itInner = vFirst.begin(); itInner!= vFirst.end(); itInner++)
			{
				if(*itInner > *it)
				{	
					bFoundMinimum = true;
					lCheatPoints++;	
					vFirst.erase(itInner , itInner+1);
					break;
				}				
			}
			if(!bFoundMinimum)
				break;
			vSecond.erase(it , it+1);			
		}

		vector<double>::reverse_iterator it2;
		for(it2 = vFFirst.rbegin(); it2!= vFFirst.rend(); it2++)
		{			
			vector<double>::iterator itInner;
			bool bFoundMinimum = false;
			for(itInner = vSSecond.begin(); itInner!= vSSecond.end(); itInner++)
			{
				if(*it2 > *itInner)
					continue;
				else
				{						
					lOptimalPoints++;	
					vSSecond.erase(itInner , itInner+1);
					break;
				}				
			}						
		}

		fpOutput<<lCheatPoints<<" "<<lCount - lOptimalPoints<<"\n";
		
	}
	
	 return 0;
}