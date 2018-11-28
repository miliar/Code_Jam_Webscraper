// CookieClickerAlpha.cpp : Defines the entry point for the console application.
//



#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <vector>
#include <iomanip>  

using namespace std;

int main(int argc, char* argv[])
{
	ifstream ifs("B-large.in");

	int n;

	ifs>>n;

	for(int i = 0; i < n;i++)
	{

		double c,f,x;
		ifs>>c>>f>>x;

		double time1,time2,temp,speed;

		time1 = x/2;

		temp = c/2;
		speed = f + 2;
		time2 = temp + x/speed;

		int farm = 2;

		while(time1 > time2)
		{
			time1 = time2;

			
			temp = temp + c/speed;
			speed = speed +f;
			time2 = temp + x/speed;
			
		}

		cout.setf(ios::fixed); 
		cout<<"Case #"<<(i+1)<<": "<<setprecision(7)<<time1<<endl;

	}


	return 0;
}

