#include<iostream>
#include<vector>
#include<iomanip>
#include<utility>
#include<algorithm>
using namespace std;

double complete_here(double r,double x)
{
	return x/(r);
}

double go_for_next(double r,double f,double c,double x)
{
	double t=0;
	t+=c/r;
	r+=f;
	return t+x/r;
}

int main()
{
	//freopen("outB.txt","w",stdout);
	int cases;
	double c,f,x,t,rate,present_c;
	
	cin>>cases;
	int ct=1;
	while(cases--)
	{
		cin>>c>>f>>x;
		rate=2;
		t=0;
		while(1)
		{
			if(complete_here(rate,x) > go_for_next(rate,f,c,x))
			{
				t += c/rate; 
				rate += f;
			}
			else
			{
				t+=x/rate;
				break;
			}	
		}
		cout<<fixed;
	    cout<<setprecision(7);
		cout<<"Case #"<<ct<<": "<<t<<endl;
		ct++;
	}
		
	return 0;
}


