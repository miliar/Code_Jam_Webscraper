#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <cstring>

using namespace std;

int main () {
	
	freopen ("input.txt", "r", stdin);
 	freopen ("output.txt", "w", stdout);

 	int t,p = 1;
 	cin >> t;
 	while (t--) {
 		double C, F, X;
 		cin >> C >> F >> X;
 		double res = X / 2.;
 		double prev = X / 2.;
 		double s = 0;
 		int cnt = 0;
 		while (cnt++ < 500000) {
 			double cur = prev - (X / (2. + F * s)) + (C / (2. + F * s)) + (X / (2. + F * (s + 1.)));
// 			printf ("%.3f\n", cur);
 			s++;
 			res = min (res, cur);
 			prev = cur;
 		}
 		printf ("Case #%d: %.7f\n", p++, res);
// 		 puts ("------");
 	}
	
	return 0;
}
