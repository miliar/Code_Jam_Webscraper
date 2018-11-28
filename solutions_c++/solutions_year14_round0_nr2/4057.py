#include<iostream>
#include <stdio.h>
using namespace std;

int main()
{
	int t;
	double c,x,f,time;
	int machines;
	cin>>t;
	for(int cases =1; cases<=t;cases++)
	{
		cin>>c>>f>>x;
		machines = (f*x-2*c)/(f*c);
		time = 0.0f;
		if(machines < 0)
			machines = 0;
		for(int i=0;i<machines;i++)
		{
			time += c/(2 + f*i);
		}	
		
		time += x/(2+ f*machines);
		printf("Case #%d: %.7f\n", cases, time);
//		cout<<"Case #"<<cases<<": "<<setprecision(7)<<time<<endl;
	}
}
