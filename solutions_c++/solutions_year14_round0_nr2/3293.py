#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
using namespace std;
int main () {
	freopen ("C:\\Users\\shreshtha24\\Desktop\\ans.txt", "w", stdout);
	int i, n, m, t, kkk = 1;
	cin >> t;
	for ( kkk = 1; kkk <= t; kkk ++) {
		double count, fff, x, res = 0, rrr = 2.0;
		cin >> count >> fff >> x;
		while ( true ) {
			if ( count/rrr+x/(rrr+fff) > x/rrr) {
				res = res + x/rrr;
				break;
			}
			res = res + (count/rrr);
			rrr = rrr+fff;
		}
		printf ("Case #%d: %.7lf\n",kkk, res);
	}
	return 0;
}