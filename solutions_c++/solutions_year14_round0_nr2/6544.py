#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;

int main()
{
	int n;
	cin >> n;
	for(int t = 1;t<=n;t++)
	{
		double tm = 0;
		double c,f,x;
		cin >> c >> f >> x;
		double rate = 2.0;

		while((x/rate) > (c/rate)+(x/(rate+f)))
		{
			tm += c/rate;
			rate+= f;
		}
		tm += (x/rate);
		printf("Case #%d: %.7lf\n",t,tm);
	}
}