#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

#define EPS 1e-9

int main()
{
#ifndef ONLINE_JUDGE
	freopen("B-large.in", "r", stdin);
	//freopen("t2.txt", "r", stdin);
	freopen("t3.txt", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		double c, f, x;
		cin >> c >> f >> x;
		double s = 2.0, v = 0, t = 0;
		while (x/s > c/s+x/(s+f))
		{
			t += c/s;
			s += f;
		}
		t += x/s;
		printf("Case #%d: %.7f\n", i+1, t);
	}
    return 0;
}
