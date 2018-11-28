
#include <iostream>
#include<stdio.h>
using namespace std;

int main() {
	// your code goes here
	double t, t1, c, f, x, r, l, tt;
	cin >> t;
	for (t1 = 1; t >= t1; t1++)
	{
		r = 2.0; tt = 0.0;
		cin >> c >> f >> x;
		l = x;
		while (1)
		{
			if (l<c)
				break;
			l -= c;
			tt += c / r;
			if (l / r >= (l + c) / (r + f))
			{
				r += f;
				l += c;
			}
		}
		tt += l / r;
		printf("Case #%.0lf: %.7lf\n", t1, tt);
	}
	return 0;
}