#include <iostream>
#include <fstream>
#include <iomanip>
#include <stdio.h>

int main()
{
	std::ifstream file("B-large.in");
	std::ofstream file2("output.txt");
	int t;
	double c=0,f=0,x=0;
	file>>t;
	for(int i=1;i<=t;i++)
	{
		file>>c;
		file>>f;
		file>>x;
		double time=0;
		double n=2.0;
		int flag=0;
		while(!flag)
		{
			if((c/n + x/(n+f))< x/n)
			{
				time+= c/n;
				n+=f;
			}
			else
			{
				time+=x/n;
				flag++;
			}
		}
		file2<<std::fixed;
		file2<<"Case #"<<i<<": "<<std::setprecision(7)<<time<<"\n";
	}

}
