//============================================================================
// Name        : cf.cpp
// Author      : HX
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <set>
#include <stack>
#include <vector>

using namespace std;
#define  N   211
#define  eps 1e-8
#define  pi  acos(-1.0)
#define  inf 0XFFFFFFFll
#define  mod 1000000007ll
#define  LL  long long


int main() {
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T; cin >> T;
	for (int t=1; t<=T; t++) {
		double C, F, X;
		cin >> C >> F >> X;
		cout << "Case #" << t << ": ";
		double ans = -1;
		double r = 2.0, s = 0.0;
		for (int c=0; c<=10000000; c++) {
			double need = s + X / r;
			if (ans < 0)
				ans = need;
			else
				ans = min(need, ans);
			if (s > ans)
				break;
			s += C / r;
			r += F;
		}
		cout << fixed << setprecision(7) << ans << endl;
	}
	return 0;
}
