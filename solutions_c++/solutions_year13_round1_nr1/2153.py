#include <iostream>
#include <math.h>

using namespace std;

int main()
{
	int tests = 0;
	cin >> tests;

	for(int n=1; n<=tests; n++)
	{
		long double r, t;
		cin >> r >> t;
		long long result = (1-2*r + sqrt(4*r*(r-1) + 1 + 8*t))/4.;
		cout << "Case #" << n << ": " << result << endl;
	}
	return 0;
}
