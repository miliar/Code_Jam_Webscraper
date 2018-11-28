/*
*	Copyright (C) Lyq root@lyq.me
*	File Name     : p2.cpp
*	Creation Time : 2014/04/12 13:39:02
*	Environment   : Ubuntu 12.04-64bit
*/
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

int main()
{
	freopen("input", "r", stdin);
	freopen("output", "w",stdout);

	int test;
	double C, F, X, d, ans, calc;
	int n;
	cin>>test;

	for (int tt = 1; tt <= test; tt++)
	{
		cin>>C>>F>>X;
		n = 0; d = 2; ans = 0;
		while (true)
		{
			calc = C*d + C*F - X*F;
			if (calc < 0)
			{
				n++;
				ans += C / d;
				d += F;
			}else break;
		}
		ans += X / d;
		//cout<<n;
		printf("Case #%d: %.7lf\n", tt, ans);
	}

	return 0;
}
