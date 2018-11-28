#include <iostream>
#include <cstdio>
#include <math.h>
#include <iomanip>

using namespace std;

int main()
{
	int T;
	cin >> T;
	int case_id = 1;

	while (T--) {
		double C, F, X;
		cin >> C >> F >> X;
		double result = 0;
		result = X / 2.0;	// init it as a1.
		double a = C / 2.0 + X / (2.0 + F);
		double b;

		for (int i = 2; ; i++) {
			b = a + C / double(F * i - F + 2) + X / double(F * i + 2) - X / double(F * i - F + 2);
			//cout << b << endl;
			if (a < b) {
				break;
			}

			a = b;
		}
		if (result > a)
			result = a;
		
		cout << "Case #" << case_id++ << ": " << setprecision(11) << result << endl;
	}

}