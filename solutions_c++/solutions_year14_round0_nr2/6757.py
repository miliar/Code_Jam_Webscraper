#include<iostream>
#include<iomanip>
#pragma comment(linker, "/STACK:200000000")
using namespace std;

long double getTime(long double C, long double F, long double X, long double rate=2.0)
{
	long double timeToBuyFarm, timeToReachX;
	timeToReachX  = X / rate;
	timeToBuyFarm = C / rate + X / (F+rate);
	if(timeToBuyFarm < timeToReachX)
		return C/rate + getTime(C, F, X, (F+rate));
	else
		return X/rate;
}

int main()
{
	int t;
	cin >> t;
	for(int k=0; k<t; k++)
	{
		long double C, F, X;
		cin >> C >> F >> X;
		cout << "Case #" << k+1 << ": ";
		cout << fixed << setprecision(7) << getTime(C, F, X) << endl;
	}
	return 0;
}
