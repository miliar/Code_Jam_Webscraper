#include <iostream>
#include <stdio.h>
#include <limits.h>
#include <string.h>
#include <math.h>

using namespace std;

const double eps = 1e-8;
int mat[5][5];
int num[20];

int main (void)
{
	freopen("D:\\B-small-attempt0.in", "r", stdin);
	freopen("D:\\Bout.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	int ca = 0;
	while(t--)
	{
		double c, f, x;
		scanf("%lf %lf %lf", &c, &f, &x);
		if(c >= x - eps)
		{
			printf("Case #%d: %.7lf\n", ++ca, x / 2.0);
			continue;
		}
		double now = 2.0;
		double ans = x / now;
		double res = 0.0;
		while(1)
		{
			res += (c / now);
			now += f;
			double nowans = res + (x / now);
			if(nowans > ans - eps)
				break;
			else
				ans = nowans;
		}
		printf("Case #%d: %.7lf", ++ca, ans);
		printf("\n");
	}
	return 0;
}