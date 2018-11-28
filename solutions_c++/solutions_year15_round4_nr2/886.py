#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <utility>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <math.h>
#include <string>
#include <string.h>
#include <vector>
#include <set>
#include <list>
#include <sstream>
#include <time.h>
#include <stdlib.h>
#include <ctype.h>
#include <iomanip>

#define print(Z,a,b) for (int __z = a; __z < b; __z ++) cout << Z[__z] << " ";
#define scan(Z,a,b) for (int __z = a; __z < b; __z ++) cin >> Z[__z];
#define bit(_z) (1ll << (_z))
#define rep(__z,__Z) for(int __z = 0; __z < __Z ; __z++ )
#define all(__z) __z.begin(),__z.end()

#define par pair<int, int>
#define p1 first
#define p2 second

const double eps = 1e-7;

using namespace std;

int n;
double X, V;
double Xs[1000], Vs[1000];

double dabs(double a)
{
	return max(a, -a);
}

int main()
{
	int t;
	cin >> t;
	int caze = 0;
	while (t --)
	{
		caze ++;

		cin >> n;
		cin >> V >> X;
		for (int i = 0; i < n; i ++)
		{
			cin >> Vs[i] >> Xs[i];
		}

		if (n == 2 and Xs[0] == Xs[1])
		{
			Vs[0] += Vs[1];
			n = 1;
		}
		if (n == 1)
		{
			if (Xs[0] != X)
				cout << "Case #" << caze << ": IMPOSSIBLE" << endl;
			else
			{
 				std::cout.setf( std::ios::fixed, std:: ios::floatfield );
				 std::cout.precision(8);
				cout << "Case #" << caze << ": " << V / Vs[0] << endl;
				//print("Case #%d: %.7lf\n", caze, V / Vs[0]);
			}
		} else if (n == 2)
		{
			double v0t = (V * (Xs[1] - X)) / (Xs[1] - Xs[0]);
			double v1t = (V * (Xs[0] - X)) / (Xs[0] - Xs[1]);

			if (X > max(Xs[0], Xs[1]) or X < min(Xs[0], Xs[1]))
				cout << "Case #" << caze << ": IMPOSSIBLE" << endl;
			else
			{
				//print("Case #%d: %.7lf\n", caze, max(v0t / Vs[0], v1t / Vs[1]));
 				std::cout.setf( std::ios::fixed, std:: ios::floatfield );
				std::cout.precision(8);
				cout << "Case #" << caze << ": " << max(v0t / Vs[0], v1t / Vs[1]) << endl;
			}
		}
	}
		
	return 0;
}


