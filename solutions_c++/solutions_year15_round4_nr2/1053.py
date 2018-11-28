#include <iostream>
#include <istream>
#include <stdio.h>
#include <string>
#include <vector> 
#include <fstream>
#include <queue>
#include <algorithm>
#define INF 2147483647
#define BIG 1000000007

using namespace std; 



int main ()
{
    freopen ("B-small-attempt3.in", "r", stdin);
	freopen ("B.out", "w", stdout); 
 	int tt; 
 	cin >> tt; 
 	for (int cases = 1; cases <= tt; cases++)
 	{
 		cout << "Case #" << cases << ": ";
 		int n;
		double vf, x, v, t, v1, t1;
 		cin >> n >> vf >> x;
 		if (n == 1)
 		{
 			cin >> v >> t;
 			if (t != x)
				cout << "IMPOSSIBLE\n";
			else
				printf ("%.9f\n", vf/v);
			continue;
		}
		cin >> v >> t >> v1 >> t1;
		if (t < t1)
		{
			double tmp1 = v, tmp2 = t;
			v = v1; t = t1; v1 = tmp1; t1 = tmp2;
		}
		else if (t == t1)
		{
			v += v1;
			if (t != x)
				cout << "IMPOSSIBLE\n";
			else
				printf ("%.9f\n", vf/v);
			continue;
		}
		//printf ("%f %f %f %f %f %f ", vf, x, v, t, v1, t1);a
		double ans = vf*(x-t1)/(t-t1);
		if (ans < 0 || (t > x && t1 > x) || (t < x && t1 < x))
			cout << "IMPOSSIBLE";
		else if (ans/v > (vf-ans)/v1)
			printf ("%.9f", ans/v);
		else
			printf ("%.9f", (vf-ans)/v1);
		cout << "\n";
	}
}
