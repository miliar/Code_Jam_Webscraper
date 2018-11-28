#include<iostream>
#include<cstring>
#include<cstdlib>
#include<cmath>

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int count, n;
	double c, f, x;
	double t;

	double tmp1;
	double m;
	double tmp2;
	double tmp3;

	cin >> count;
	for (n = 0; n < count; n++)
	{
		cin >> c;
		cin >> f;
		cin >> x;
		t = x / 2;
		for (m = 1, tmp2 = 0;; m++)
		{
			tmp2 += (c / (2 + (m - 1) * f));
			tmp3 = (x / (2 + m * f));
			tmp1 = tmp2 + tmp3;
			if (tmp1 < t)
				t = tmp1;
			else
				break;
		}
		printf("Case #%d: %.7lf\n", n + 1, t);
	}
	return 0;
}