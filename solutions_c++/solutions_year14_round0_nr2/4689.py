#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <queue>
#include <iostream>
#include <cstdlib>

using namespace std;

const double eps = 1e-8;

char cmp_d(const double x, const double y)
{
	if (x - y > -eps && x - y < eps) return 0;
	else if (x - y < -eps) return -1;
	else return 1;
}

double C, F, X;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t, T;
	int i, j;
	double rt;
	double sp;
	double t_used;
	scanf("%d", &T);
	for (t = 1; t <= T; t++)
	{
		scanf("%lf%lf%lf", &C, &F, &X);
		t_used = 0;
		sp = 2;
		rt = X / sp;
		while (1)
		{
			t_used += C / sp;
			sp += F;
			if (cmp_d(rt, t_used + X / sp) < 0) break;
			else
			{
				rt = t_used + X / sp;
			}
		}
		printf("Case #%d: %0.7f\n", t, rt);
	}
	
	return 0;
}