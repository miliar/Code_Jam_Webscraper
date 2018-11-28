#include<iostream>
using namespace std;
#include<stdio.h>
#include <fstream>
#include <iomanip>
int main()
{
	
	int t =0 ;
	double c,f,x,time=0,time1=0,time2=0,rate=2;
	ifstream inf("input.txt");
	inf >> t;
	ofstream outf("output.txt");
	for(int i = 0; i <t ; i++)
	{
		time=0.000000,time1=0.0000000,time2=0.00000000,rate=2.00000000;
		inf>>c;
		inf>>f;
		inf>>x;
		while(1)
		{
			time1 = x/rate;
			time2 = c/rate + x/(rate+f);
			if (time2<time1)
			{
				time = time + c/rate;
				rate=rate+f;
			}
			else
			{
				time = time + x/rate;
				break;
			}
		}
		//cout<<time;
		outf<<fixed << setprecision(7) <<"Case #"<<(i+1)<<": "<<time<<"\n";
	}
	return 0;
}