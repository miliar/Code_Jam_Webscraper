#if 1

#include <math.h>
#include <iostream>
#include <deque>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <string>
#include <ctime>
#include <vector>
using namespace std;
typedef long double LD; 
typedef long long LL; 

#define PROBLEM "B-large"

double solve (double c, double f, double x)
{
	double cps = 2, t = 0;
	while (1)
	{
		if (x / cps > c / cps + x / (f +cps))
		{
			t += c / cps;
			cps += f;
		}
		else
		{
			t += x / cps;
			return t;
		}
	}

	return -1;
}

void main()
{
	freopen(PROBLEM ".in","r",stdin); freopen(PROBLEM ".out","w",stdout);
	//freopen("input.txt","r",stdin); //freopen("output.txt","w",stdout);
	time_t START = clock();

	int n; 
	cin >> n;
	double c, f, x;

	for (int t = 1; t <= n; ++t)
	{
		cin >> c >> f >> x;
		cout << "Case #" << t << ": ";
		printf("%.7f\n", solve(c, f, x));
	}

	time_t FINISH = clock(); 
	cerr << "Time = " << double(FINISH - START) / CLOCKS_PER_SEC << endl;
	return;
}
#endif