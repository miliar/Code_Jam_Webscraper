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
	int i, n, m, t, k = 1;
	cin >> t;
	while ( t --) {
		double c, f, x, tot = 0, r = 2.0, m;
		cin >> c >> f >> x;
		while ( true ) {
			if ( c/r+x/(r+f) > x/r) {
				tot = tot + x/r;
				break;
			}
			tot = tot + (c/r);
			r = r+f;
		}
		printf ("Case #%d: %.7lf\n",k, tot);
		k ++;
	}
	return 0;
}