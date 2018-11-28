# include <iostream>
# include <cstdio>

using namespace std;

double c, f, x, ans;

double now, h, timea, k;

double eps = 0.0000001;

int main ()
{
	int i, t, te;
	cin >> t;
	for (te = 1; te <= t; te ++)
	{
		cin >> c >> f >> x;
		now = 0.0;
		timea = 0.0;
		h = 2.0;
		while (1)
		{
			///cout << c << " " << h << " " << x << " " << now << " " << time << endl;
			k = (c - now) / h;
			if ((x - now) / h + timea > (x / (h + f)) + k + timea + eps)
			{
				now = 0.0;
				h += f;
				timea += k;
			}
			else
			{
				timea += (x - now) / h;
				break;
			}				
		}
		printf ("Case #%d: %.7lf\n", te, timea);
	}
	return 0;
}
