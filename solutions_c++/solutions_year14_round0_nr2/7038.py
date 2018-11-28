#define _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include<stdio.h>
#include <iomanip>

using namespace std;

int main()
{
	freopen("2.in", "r", stdin);
	freopen("2.out", "w", stdout);
	int test;
	cin >> test;
	for (int t = 0; t < test; t++)
	{
		double c, f, x;
		cin >> c >> f >> x;
		double min = x/2, save = 0.0, time;
		int count = 0, flag = 0;
		for (int n = 1; n <= 100000; n++)
		{
			//if (flag)
				//count++;
			save += c / (2 + f * (n - 1));
			time = save + (x / (2 + f * n));
			if (time < min)
			{
				min = time;
				//flag = 1;
				//count = 0;
			}
			//if (count > 5)
				//break;
		}
		cout << "Case #" << (t + 1) << ": ";
		if (min < 10.0)
			cout << std::setprecision(8) << min << endl;
		else if (min >= 10.0 && min <100.0)
			cout << std::setprecision(9) << min << endl;
		else if (min >= 100.0 && min <1000.0)
			cout << std::setprecision(10) << min << endl;
		else if (min >= 1000.0 && min <10000.0)
			cout << std::setprecision(11) << min << endl;
		else if (min >= 10000.0 && min <100000.0)
			cout << std::setprecision(12) << min << endl;
		else if (min >= 100000.0 && min <1000000.0)
			cout << std::setprecision(13) << min << endl;
	}
	return 0;
}
