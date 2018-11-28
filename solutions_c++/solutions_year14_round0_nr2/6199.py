#include<iostream>
#include<cstdio>
#include<iomanip>

using namespace std;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T;
	double C,F,X;
	cin>>T;
	for(int i=1; i<=T; i++)
	{
		cin>>C>>F>>X;
		double rate = 2.0;
		double cost = (X/rate);
		cout<<fixed;
		if(X<C)
			cout<<"\nCase #"<<i<<": "<<setprecision(7)<<cost;
		else
		{
			rate += F;
			double newCost = (C/2.0) + (X/rate);
			while(newCost<cost){
				cost = newCost;
				newCost -= (X/rate);
				newCost += (C/rate) + (X/(rate+F));
				rate += F;
			}
			cout<<"\nCase #"<<i<<": "<<setprecision(7)<<cost;
		}
	}
}