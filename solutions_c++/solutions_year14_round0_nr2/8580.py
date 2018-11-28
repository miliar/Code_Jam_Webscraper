#include<iostream>
using namespace std;
#include<float.h>
#include <iomanip> 

double X, C, F;

double t[1000005];
double rate[1000005];
void preCompute(int farms)
{
	
	rate[0] = 2.0;
	for(int i = 1; i <= farms; ++i)
	{
		t[i] = t[i - 1] + (C / rate[i - 1]);
		rate[i] = rate[i - 1] + F;
	}
}

double f(int farms)
{
	double tmp = t[farms];

	double rem = X / rate[farms];

	return tmp + rem;
}

int main()
{

	freopen("B-large.in", "rt", stdin);
	freopen("large2.txt", "wt", stdout);
	int t;
	cin >> t;
	double ans;
	for(int i = 1; i <= t; ++i)
	{
		cin >> C >> F >> X;
		ans  = DBL_MAX;
		preCompute(100000);
		for(int farms = 0; farms <= 100000; ++farms)
		{
		//	cout << f(farms) <<  endl;;
			ans = min(ans, f(farms));
		}
		cout << "Case #" << i << ": " << fixed << std::setprecision(7) << ans << endl;
	}
	return 0;
}
