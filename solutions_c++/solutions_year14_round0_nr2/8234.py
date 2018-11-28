/*
 * Bsmall.cpp
 *
 *  Created on: Apr 12, 2014
 *      Author: kerollosasaad
 */
#include<bits/stdc++.h>
using namespace std;

int main() {

	freopen("B-large.in", "r", stdin);
	freopen("Blarge.out", "w", stdout);

	int tc, counter = 0;
	cin >> tc;
	while (tc--) {
		bool flag = 1;
		double c, f, x, cookies = 2, tmp1, tmp2, ret = 0;
		cin >> c >> f >> x;
		while (flag) {
			tmp1 = (c / cookies) + (x / (cookies + f));
			tmp2 = x / cookies;
			(tmp1 < tmp2) ? ret += c / cookies : (ret += x / cookies, flag = 0);
			cookies += f;
		}
		printf("Case #%d: %.7f\n", ++counter, ret);
	}
	return 0;
}

