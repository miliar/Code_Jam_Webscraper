#include<iostream>
#include<fstream>
#include<stdio.h>
using namespace std;

void main()
{
	fstream fs,os;
	fs.open("cookie2.in",ios::in);
	os.open("sol2.txt",ios::out);
	int t,val=1;
	double c,f,x,rate=2.0000000,time=0.0000000;
	fs>>t;

	while(t>0)
	{

	fs>>c>>f>>x;

	while(((c/rate)+(x/(rate+f)))<(x/rate))
	{
		time=time+(c/rate);
		rate=rate+f;
	}

	time=time+x/rate;
	os.precision(7);
	os.setf(ios::fixed);
	os.setf(ios::showpoint);
	os<<"Case #"<<val<<": "<<time<<"\n";
	val++;
	rate=2;
	time=0;
	t--;
	}

	fs.close();
	os.close();

}



