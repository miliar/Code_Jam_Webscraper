#include <cstdio>
#include <math.h>
#include <iostream>
#include <vector>
#include <string>
#include <bitset>
#include <cassert>
#include <tuple>
#include <map>
#include <algorithm>
#include <set>
#include <iomanip>

using namespace std;

int main(int argc, char *argv[])
{
	int T;
	cin >> T;

	for (int i = 1; i <= T; i++)
	{
		double C, F, X;
		cin >> C;
		cin >> F;
		cin >> X;

		double m = 2.0;
		double t = 0.0;
		while (true)
		{
			double tf = C/m;
			double breakeven = (m+F) * tf / F;

			double tx = X/m;

			if (tx > breakeven)
			{
				m = m+F;
				t += tf;
			}
			else if (tx <= breakeven)
			{

				t += tx;
				break;
			}
		}

		cout << "Case #" << i << ": ";

		cout << setprecision(7) << setiosflags(ios::fixed) << t;
		cout << resetiosflags(ios::floatfield);

		cout << endl;
	}
}
