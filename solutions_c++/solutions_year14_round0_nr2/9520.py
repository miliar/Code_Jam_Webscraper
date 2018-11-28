#include <iostream>
#include <cstdio>
#include <iomanip>
#include <stdio.h>
#include <fstream>

using namespace std;

double durum(double f, double c, double x, int k, double current, int dontbuy);

int main()
{
	double c,f,x,current;
	int adet,i=1;
	ifstream r("small.in");
	ofstream w("output");

r >> adet;
while(i<=adet)
{	
	
	r >> c >> f >> x;
	w << "Case #" << i << ": " << fixed << setprecision(7) << durum(f,c,x,0,current,0) << endl;
	
	i++;
}
	return 0;
}

double durum(double f, double c, double x, int k, double current, int dontbuy)
{	
	
	bool comp =  (x-c)/(f*k+2) >= x/(f*(k+1)+2);
	if(dontbuy)
	{
		return (x-c)/(f*k+2);
	}
	else if(comp && current>=c)
	{
		return durum(f,c,x,k+1,current-c,0);
	}
	else if(!comp && current>=c)
	{
		return durum(f,c,x,k,current,1);
	}
	else if(current<c && !dontbuy)
	{
		return (c-current)/(f*k+2)+durum(f,c,x,k,c,0);
	}
}
