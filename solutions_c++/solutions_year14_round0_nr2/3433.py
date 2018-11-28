#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
using namespace std;
int main () {
	freopen ("C:\\Users\\shreshtha24\\Desktop\\ans2.txt", "w", stdout);
	int i, n, m, test, kkk = 1;
	cin >> test;
	for ( kkk = 0; kkk < test; kkk ++) {
		double cnt, f_val, x_val, answer = 0, rate = 2.0, q;
		scanf ("%lf %lf %lf", &cnt, &f_val, &x_val);
		while ( true ) {
			if ( cnt/rate+x_val/(rate+f_val) > x_val/rate) {
				q = x_val/rate;
				answer = answer + q;
				break;
			}
			answer = answer + (cnt/rate);
			rate = rate+f_val;
		}
		printf ("Case #%d: %.7lf\n",(kkk+1), answer);
	}
	return 0;
}