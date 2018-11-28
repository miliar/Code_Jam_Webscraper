#define _CRT_SECURE_NO_WARNINGS
#include <vector>
#include <list>
#include<string.h>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include<string>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>

#define rep(i,n) for (int i =0; i<n ; i++)
#define lp(j,n) for(int j=1;j<=n;j++)

using namespace std;


long double solve(long double c, long double f, long double x) {
	long double s = 2 + f, ac = c / 2, ax = x / 2;

	while (1) {
		long double cc = ac + c / s;
		long double xx = ac + x / s;

		if (xx > ax)
			return ax;
		ac = cc;
		ax = xx;
		s += f;
	}
}

int main() {
	freopen("in.in", "r", stdin);
	freopen("out1.in", "w", stdout);
	int t;
	cin >> t;
	lp(i, t){
		long double c, f, x;
		cin >> c >> f >>  x;
		printf("Case #%d: %.7llf\n", i, solve(c, f, x));
	}



	return 0;
}