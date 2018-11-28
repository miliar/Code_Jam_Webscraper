// K1
// :)

#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <queue>
#include <bitset>
#include <string>
#include <cmath>
#include <iomanip>
#include <set>
#include <map>

#define EPS 1e-8
#define PI 3.141592653589793
#define X first
#define Y second
#define FX(x) fixed << setprecision((x))

using namespace std;

typedef pair<int, int> point;
typedef set<int>::iterator ITR;
const int MAXN = 2e5 + 123;

double r[100];
double c[100];

int main()
{
	int t;
	cin >> t;
	for (int test = 0; test < t; ++test)
	{
		c[1] = c[2] = 9999999;
		r[1] = r[2] = 9999999;

		int n;
		double v, x;
		cin >> n >> v >> x;
		for (int i = 1; i <= n; ++i)
			cin >> r[i] >> c[i];
		double t1, t2;
		cout << "Case #" << test+1 << ": ";
		
		if(n == 1)
		{
			if(x != c[1])
			{
				cout << "IMPOSSIBLE" << endl;
				continue;
			}
			cout << FX(6) << v / r[1] << endl;
			continue;

		}

		if(min(c[1], c[2]) > x || max(c[1], c[2])  < x)
		{
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		
		if(c[2] == c[1])
		{
			cout << FX(6) << v / (r[1] + r[2]) << endl;
			continue;
		}

		t2 =  (v * x - v * c[1]) / (r[2] * (c[2] - c[1]));
		t1 = (v - r[2] * t2) / r[1];
		// cerr << t1 << " " << t2 << endl;
		cout << FX(6) << max(t1, t2) << endl;
	}

	return 0;
}