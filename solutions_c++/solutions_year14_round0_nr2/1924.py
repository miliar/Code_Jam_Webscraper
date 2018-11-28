#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <cmath>

using namespace std;


int main()
{
	int i, j, n, m, test, cnt_test, cnt;
	double x, c, f, time = 0, v = 2.0;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> cnt_test;
	cout.precision(20);
	cout << fixed;
	for(test = 1; test <= cnt_test; test++)
	{
		cin >> c >> f >> x;
		v = 2.0;
		time = 0;
		while(x / v > c / v + (x / (v + f)))
		{
			time += c / v;
			v += f;
		}
		cout <<"Case #" << test  << ": " << time + x / v << '\n';
	}
	return 0;
}