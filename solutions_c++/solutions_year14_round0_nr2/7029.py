#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

int T;
double C,F,X;

int main()
{
	cin >> T;
	for (int i=0;i<T;i++)
	{
		cin >> C >> F >> X;
		double rate=2;
		double best_time=X/rate;
		double current=0;
		while (1)
		{
			current=current+C/rate;
			rate+=F;
			double expected=current+X/rate;
			if (expected<best_time)
				best_time=expected;
			else break;
		}
		cout << "Case #" << i+1 << ": ";
		printf("%.7lf\n",best_time);
	}
	return 0;
}