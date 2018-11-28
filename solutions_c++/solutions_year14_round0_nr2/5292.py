#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

int main(void)
{
	int T;
	cin >> T;
	for (int C = 1; C <= T; C++)
	{
		double c, f, x;
		cin >> c >> f >> x;
		double rate = 2.0;
		double count = 0.0;
		double ans = x / rate;
		double cnt = max(0.0, ceil(((f*x-c*f-2*c)/(c*f)))-1);
		for (int i = cnt; i >= 0; i--)
			count += c / (f*i+rate);
		rate += f * (cnt + 1);
		for (int i = 0; i < 3; i++)
		{
			ans = min(ans, count + x / rate);
			count += c / rate;
			rate += f;
		}
		printf("Case #%i: %.9f\n",C,ans);
	}
	return 0;
}
