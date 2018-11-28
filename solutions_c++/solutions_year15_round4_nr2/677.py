#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cstring>
#include <cstdio>
using namespace std;

double r[105];
double c[105];
double vv[105];
double tt[105];

int main()
{
	int ttt;
	
	cin >> ttt;
	
	for (int t = 1; t <= ttt; ++t)
	{
		cout << "Case #" << t << ": ";
		int n;
		double v, x;
		
		cin >> n >> v >> x;
		for (int i = 0; i < n; ++i)
			cin >> r[i] >> c[i];
		if (n == 1)
		{
			if (c[0] == x)
				printf("%.8lf\n", v / r[0]);
			else
				cout << "IMPOSSIBLE" << endl;
		}
		else if (n == 2)
		{
			if (((c[0] > x) && (c[1] > x)) || ((c[0] < x) && (c[1] < x)))
				cout << "IMPOSSIBLE" << endl;
			else if ((c[0] == x) || (c[1] == x))
			{
				double tv = 0;
				if (c[0] == x)
					tv += r[0];
				if (c[1] == x)
					tv += r[1];
				printf("%.8lf\n", v / tv);
			}
			else
			{
				vv[0] = v * (x - c[1]) / (c[0] - c[1]);
				tt[0] = vv[0] / r[0];
				vv[1] = v * (x - c[0]) / (c[1] - c[0]);
				tt[1] = vv[1] / r[1];
				printf("%.8lf\n", max(tt[0], tt[1]));
			}
		}
	}

	return 0;
}
