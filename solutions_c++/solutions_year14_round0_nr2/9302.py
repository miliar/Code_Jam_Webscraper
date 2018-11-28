#include<iostream>
#include<string>
#include<fstream> 
#include<stdio.h>
#include<cmath>
#include<iomanip>

using namespace std; 

int main()
{
	
    int tcTotal,tcCount=1;
	ifstream myfile("C:\\Data\\Workspace\\CPP\\blarge.in");
	ofstream myfileoutput("C:\\Data\\Workspace\\CPP\\output.in");
	if(myfile.is_open())
	{
		myfile>>tcTotal;
		double C,F,X,T,Y,T1,T2,Rate;	
		
		while(myfile.good() && tcCount<=tcTotal)
		{
			myfile>>C;
			myfile>>F;
			myfile>>X;
			
			T = 0.0;
			Y = 0.0;
			T1 = 0.0;
			T2 = 0.0;
			Rate = 2.0000000;
			
			if (C>=X)
			{
				T = X/Rate;
				myfileoutput<<"Case #"<<tcCount<<": "<<std::setprecision(20)<<showpoint<<T<<"\n";
			}
			else
			{
				while(Y!=X)
				{
					T1 = X/Rate; //don't buy farm option
					T2 = (C/Rate) + (X/(Rate+F)); //buy farm option
					
					if(T1>T2) 
					{
						T = T + C/Rate; //
						Rate=Rate+F; 
					}
					else
					{
						T = T + (X/Rate);
						Y = X;
						myfileoutput<<"Case #"<<tcCount<<": "<<std::setprecision(20)<<showpoint<<T<<"\n";
					}
				}
			}
	       
			tcCount++;
		}
		myfile.close();
		myfileoutput.close();
    }
    return 0; 
} 

