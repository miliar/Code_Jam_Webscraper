#include <bits/stdc++.h>
using namespace std;

double c, f, x;

double minTime(double rate)
{
	if((rate - 2.0) * c > x * f)
	{
		return x;
	}
	double t1 = x / rate;
	double t2 = c / rate + minTime(rate + f);
	if(t1 < t2)
	{
		return t1;
	}
	else
	{
		return t2;
	}
}

int main()
{
	int t, T;
	cin >> T;
	for(t = 1; t <= T; ++t)
	{
		cin >> c >> f >> x;
		printf("Case #%d: %.8lf\n", t, minTime(2.0));
	}
	return 0;
}
