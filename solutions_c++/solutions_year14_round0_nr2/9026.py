#include <iostream>
#include <fstream>
#include <cstdio>
#include <climits>
#include <cmath>
#include <algorithm>

using namespace std;

typedef long long ll;

double getf(ll k, double C, double F, double X)
{
	double sum = 0.0;
	for(ll i = 0; i < k; i++)
		sum += C/(2.0 + i*F);
	sum += X/(2.0 + k*F);
	return sum;
}

int main()
{
	int t;
	double c,f,x;
	freopen("cc.in", "r", stdin);
	freopen("cc.out", "w", stdout);
	cout.precision(16);
	cin >> t;
	for(int ti = 1; ti <= t; ti++)
	{
		cin >> c >> f >> x;
		double tmp1 = getf(floor(x/c - 2.0/f),c, f, x), tmp2 = getf(ceil(x/c - 2.0/f),c, f, x);
		double tmp = min(tmp1, tmp2);
		cout << "Case #" << ti << ": ";
		if(tmp < 0)
			cout << min(0.5*x, max(tmp1, tmp2)) << "\n";
		else
			cout << min(0.5*x, tmp) << "\n";
	}	
	return 0;
}