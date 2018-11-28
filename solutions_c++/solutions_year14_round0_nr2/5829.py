#include <iomanip>
#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
	int t;
	double time = 0, time1 = 0, time2 = 0, f, c, x, r;
	cin >> t;
	for(int i = 1;i <= t;++i)
	{
		cin >> c >> f >> x;
		r = 2;
		time = x / r;
		time2 = c / r;
		r += f;
		time1 = time2 + x / r;
		while(time1 < time)
		{
			time = time1;
			time2 += c / r;
			r += f;
			time1 = time2 + x / r;
		}
		printf("Case #%d: %.7lf\n", i, time);
	}
	return 0;
}