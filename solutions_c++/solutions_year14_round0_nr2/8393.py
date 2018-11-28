#include <iostream>
#include <queue>
#include <vector>
#include <cstdio>
#include <algorithm>
using namespace std;

int main()
{
	ios_base::sync_with_stdio(0);
	int prz;
	cin >> prz;
	for(int lic = 0; lic < prz; ++lic)
	{
		double t = 0.0;
		double speed = 2.0;
		double c, f, x;
		cin >> c >> f >> x;

		double t1;
		double t2;

		while(1)
		{
			t1 = c / f;
			t2 = (x - c) / speed;
			if(t2 < t1)
			{
				t += x / speed;
				break;
			}
			else
			{
				t += c / speed;
				speed += f;
			}
		}

		cout << "Case #" << lic + 1 << ": ";

		cout.precision(7);
		cout << fixed;
		cout << t << '\n';
	}
	return 0;
}