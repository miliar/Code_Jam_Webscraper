#include <iostream>
#include <iomanip>

using namespace std;

const long double initf = 2;
long double costf(long double rate,long double cost)
{
	return cost/rate;
}

void calc(long double test, long double cost, long double f, long double x)
{
	long double rate = initf;
	long double time = 0;
	long double temp = 0;
	while( x/(rate) > x/(rate+f) + costf(rate,cost))
	{
		temp =  costf(rate,cost);
		time = temp + time;
		rate = rate +f;
	}
	temp = x/rate;
	time = temp + time ;
	
	cout << "Case #" << setprecision(0) << test << ": " << setprecision(7)<< time << endl;
	
	return;
}

int main()
{
	cout << fixed << setprecision(7);
	long double Cost = 0, F =0, X= 0;
	int tests = 0;
	cin >> tests;
	for(int i = 0; i < tests ; i++)
	{
		cin >> Cost;
		cin >> F;
		cin >> X;
		calc(i+1, Cost, F, X);
		
	}
	
	return 0;
}
