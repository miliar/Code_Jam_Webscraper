#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{

	freopen("input.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int t;
	cin >> t;
	for (size_t tsc = 1; tsc <= t; tsc++) {

		double c, f, x;
		cin >> c >> f >> x;
		double inc = 2;
		long double ans = 0;
		
		while (1) {
			double a = ans + (x / inc);
			double b = ans + (c / inc) + (x / (inc + f));
			if (a <= b) {
				ans += x / inc;
				break;
			}
			
			ans += c / inc;
			inc += f;
		}

		printf("Case #%d: %0.8lf\n", tsc, ans);
	}
}