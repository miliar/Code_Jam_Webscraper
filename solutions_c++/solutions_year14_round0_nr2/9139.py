//============================================================================
// Name        : codejam.cpp
// Author      : huangxs139
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <cctype>
#include <cmath>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <stack>
using namespace std;

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	double c, f, x;
	double s;
	double ans;
	int t, cas = 0;
	scanf("%d", &t);
	while (t--) {
		scanf("%lf%lf%lf", &c, &f, &x);
		ans = 0;
		s = 2.0;
		while (x/s > c/s+x/(s+f)) {
			ans += c/s;
			s += f;
		}
		ans += x/s;
		printf("Case #%d: %.7f\n", ++cas, ans);
	}
	return 0;
}
