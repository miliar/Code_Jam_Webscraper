#include <iostream>
#include <algorithm>
#include <iomanip>
using namespace std;

double C,F,X;
double f(double rate);

int main()

{


int T;
cin>>T;

for(int i=0; i<T; i++)
{
	cin>>C>>F>>X;
	cout<<"Case #"<<i+1<<": "<<fixed<<setprecision(7)<<f(2.0)<<endl;
}


return 0;
}

double f(double rate)
{
	double wait = C/rate;
	
	double t = X/rate;

	if (t < wait + X/(rate+F)) return t;

	return min(wait + f(rate + F) , t);

}