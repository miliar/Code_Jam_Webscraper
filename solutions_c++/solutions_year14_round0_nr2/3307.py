#include <iostream>
#include <cmath>
#include <cfloat>

using namespace std;

int get_n(long double c, long double f, long double x);

int main()
{
	cout.precision(7);
	cout << std::fixed;
    int t;
    cin >> t;
    for (int cn = 1; cn <= t; ++cn)
	{
		long double f, c, x;
		cin >> c >> f >> x;
		long double time = 0.0;
		long double speed = 2.0;
		int n = get_n(c, f, x);
		for (int i = 0; i < n; ++i)
		{
			time += c/speed;
			speed += f;
		}
		time += x/speed;
		// output
		cout << "Case #" << cn << ": " << time << "\n";
    }

    return 0;
}

int get_n(long double c, long double f, long double x)
{
	int n = 0;
	long double gamma = (x*f-2.0*c)/c/f-1.0;
	long double igamma = floor(gamma);
	if (igamma < 0)
		return 0;
	else
		n = (int)igamma;
	if (fabs(igamma-gamma) > LDBL_EPSILON)
		++n;
	return n;
}

