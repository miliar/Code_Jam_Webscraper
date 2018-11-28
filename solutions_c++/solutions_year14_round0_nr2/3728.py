#include<iostream>
#include <fstream>
#include<iomanip>
#include<conio.h>
using namespace std;
int main()
{
	ifstream inp;
	ofstream out;
	inp.open("input.in");
		if(!inp)
	{
		return 100;
	}
	out.open("output.txt");
	if(!out)
	{
		return 100;
	}
	int cases;
	inp>>cases;
	double c,f,x;
	double time;
	int flag;
	double rate;
	for(int z=1;z<=cases;z++)
	{
		inp>>c;
		inp>>f;
		inp>>x;
		time =0;
		flag=0;
		rate=2;
		double t1=0,t2=0,t3=0;
		while(1)
		{
			t1=c/rate;
			t2=x/rate;
			t3=x/(rate+f);
			if((t1+t3)<t2)
			{
				time=time+t1;
				rate=rate+f;	
			}
			else
			{
				time=time+t2;
				break;
			}
			
		}
		out<<fixed;
		out<<setprecision(7);
		out<<"case #"<<z<<": "<<time<<"\n";
		cout<<fixed;
		cout<<setprecision(7);
		cout<<"case #"<<z<<": "<<time<<"\n";
	}
	inp.close();
	out.close();
	return 0;
	
}

