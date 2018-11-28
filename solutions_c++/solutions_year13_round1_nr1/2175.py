#include <iostream>
#include <cmath>

using namespace std;


int main()
{
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		long long r, l;
		cin >> r;
		cin >> l;

//		cout << "r:" << r << endl;
//		cout << "l:" << l << endl;
		long long unsigned count = 0;
		long long b = -(2 * r - 1);
		long double tvar = (long double)b * (long double)b + 8 * l;
		long double tsqrt = sqrt(tvar);
		
//		cout << "b:" << b << endl;
//		cout << "tvar:" << tvar << endl;
//		cout << "tsqrt:" << tsqrt << endl;
		count =  (b + (long long)(floor(tsqrt))) / 4;

		cout << "Case #" << (i + 1) << ": " << count << endl;
	}
}
