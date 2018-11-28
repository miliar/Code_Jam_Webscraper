// B-Small.cpp : main project file.

//#include "stdafx.h"
#include <stdio.h>
#include <vector>
using namespace std;

vector<double> v;
int main()
{
	/*freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);*/
	int t;
	scanf("%d", &t);
	double C, F, X, cur;
	for (int z = 1; z <= t; z++)
	{
		v.clear();
		scanf("%lf %lf %lf", &C, &F, &X);
		cur = 0.0;
		int i = 0;
		while (1)
		{
			v.push_back(cur + X / (2.0 + F * i));
			if (i > 0 && v[i] > v[i - 1])
			{
				printf("Case #%d: %.7lf\n", z, v[i - 1]);
				break;
			}
			cur = cur + C / (2.0 + F * i++);
		}
	}
	return 0;
}
