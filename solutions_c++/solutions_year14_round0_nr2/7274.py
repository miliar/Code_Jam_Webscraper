#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
#include <map>
#include <cmath>
#include <stdio.h>
#include <fstream>
#include <iomanip>

using namespace std;

double getBest(int n, double c, double f, double x)
{

	double rate = 2;
	double time = 0.0;

	for (int i = 0; i < n - 1; i++)
	{
		time += (c / rate);
		rate += f;
	}

	time += (x / rate);

	return time;
}

int main()
{
   
	ifstream cin("B-large.in");
	ofstream cout("output.txt");

	int t;
	cin >> t;

	
	for (int i = 1; i <= t; i++)
	{
		
		double c, f, x;
		cin >> c >> f >> x;
		
		int lo = 0;
		int hi = 1000000;
		int m = 1;

		while (lo < hi)
		{

			m = (lo + hi) / 2;
			double cur = getBest(m, c, f, x);
			double next = getBest(m + 1, c, f, x);
			// 50 40 45 30 15 18 20 50 100
			if (cur < next)
			{
				hi = m;
			}
			else
			{
				lo = m + 1;
			}

		}

		cout.precision(7);
		cout << "Case #" << i << ": " << fixed << setprecision(7) << getBest(hi, c, f, x) << endl;
		
		

	}


}