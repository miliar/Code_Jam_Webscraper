#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <cmath>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
using namespace std;
FILE *stream;
double c, f, x;
double check(int cf)
{
	double res = 0;
	if (cf == 0)
		return (x / 2);
	double cur = 2;
	for (int i = 0; i < cf; ++i)
	{
		res += c / cur;
		cur += f;
	}
	res += x / cur;
	return res;
}
int main()
{
	freopen_s(&stream,"B-large.in","r",stdin);
	freopen_s(&stream,"output.txt","w",stdout);
	int t;
	cin >> t;
	for (int z = 1; z <= t;++z)
	{
		
		cin >> c >> f >> x;
		double curs = 2;
		double res = x / 2;
		int l = 0, r = 1e6;
		for (int gg = 0; gg <= 1000;++gg)
		{
			int m1 = l + (r - l) / 3,m2=l+2*(r-l)/3;
			if (check(m1) < check(m2))
				r = m2;
			else
				l = m1;
		}
		for (int i = l; i <= r; ++i)
		{
			res = min(check(i), res);
		}
		cout << "Case #" << z << ": ";
		printf("%.7lf\n",res);
	}
	return 0;
}