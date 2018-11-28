#include<stdio.h>
#include<iostream>
#include<string.h>
#include<iomanip>
using namespace std;
double findcookie(double c,double f,double x,double rate);
int main()
{
int t;
cin>>t;
double c,f,x,res;
	for(int y=1;y<=t;y++)
	{
		cin>>c>>f>>x;
		res=findcookie(c,f,x,2.0);
		cout.fixed;
		cout<<fixed;
		cout<<setprecision(7);
		cout<<"Case #"<<y<<": "<<res<<endl;
	}
}
double findcookie(double c,double f,double x,double rate)
{
	double a=0;
	if(x<0.0000001)
	{
		return 0;
	}
	else{
		if((x/rate)<((x/(rate+f))+(c/rate)))
		{
		//cout<<"\n"<<x/rate<<"\n";
			a=(x/rate)+findcookie(c,f,0,rate);
		}
		else
		{
		//cout<<"\n"<<c/rate<<"\n";
			a=(c/rate)+findcookie(c,f,x,rate+f);
		}
	}
		return a;
}
