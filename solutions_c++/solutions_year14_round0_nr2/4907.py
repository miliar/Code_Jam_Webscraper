#include <iostream>
#include <iomanip>
using namespace std;

long double mintime(int n, long double ptime, long double price, long double add_rate, long double final)
{
	long double time = 0.0;
	long double rate = 2.0;
	for(int i = 0; i<n; i++)
	{
		time = time+(price/rate);
		rate = rate+add_rate;
	}
	time = time+(final/rate);
	if(time < ptime || n==0)
	{
		return mintime(n+1, time, price, add_rate, final);
	}
	else
		return ptime;
}

int main()
{
	int ntest;
	cin>>ntest;
	for(int i = 0; i<ntest; i++)
	{
		long double p,a,f,time;
		cin>>p>>a>>f;
		time = mintime(0,0,p,a,f);
		cout.precision(7);
		cout.setf( ios::fixed, ios::floatfield );
		cout<<"Case #"<<i+1<<": "<<time<<endl;
	}
}
