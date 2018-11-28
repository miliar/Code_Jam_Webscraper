#include <iostream>
#include <algorithm>
#include <string>
#include <utility>
#include <cstdio>
#include <vector>
#include <cmath>
#include <ctime>
#include <queue>
#include <map>

typedef long long LL;

using namespace std;

int main ()
{
	cout.precision (10);
    freopen ("input.txt", "r", stdin);
    freopen ("output.txt", "w", stdout);
    int t;
    scanf ("%d", &t);
    bool stop;
    double c, f, x, time, income;
    for (int i = 0;i < t;i++)
    {
		scanf ("%lf%lf%lf", &c, &f, &x);
		printf ("Case #%d: ", i + 1);
		stop = false;
		time = 0.0;
		income = 2.0;
		while (stop != true)
		{
			if (x * f <= c * (income + f))
			{
				time += x / income;
				stop = true;
			}
			else
			{
				time += c / income;
				income += f;
			}
		}
		printf ("%.7lf\n", time);
	}
    return 0;
}
