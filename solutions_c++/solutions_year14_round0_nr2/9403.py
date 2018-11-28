#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <iostream>
#include <math.h>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>

#define EPS 1e-7

using namespace std;

int main()
{
	//cin.sync_with_stdio(0);
	#ifndef ONLINE_JUDGE
		freopen("input.txt", "rt", stdin);
		freopen("output.txt", "wt", stdout);
	#endif
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i)
	{
		double c, f, x, ans = 0.0, speed = 2.0;
		scanf("%lf %lf %lf", &c, &f, &x);
		if (x < c + EPS)
			ans = x/speed;
		else
		{
			while (true)
			{
				ans += c/speed;
				if ((x - c)/speed < x/(speed + f) + EPS)
				{
					ans += (x - c)/speed;
					break;
				}
				else
				{
					speed += f;
				}
			}
		}
		printf("Case #%d: %.8lf\n", i, ans);
	}
    return 0;
}