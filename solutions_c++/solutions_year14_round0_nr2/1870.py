/*
 * Author    : ben
 */
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <functional>
#include <numeric>
#include <cctype>
using namespace std;

double work() {
	double C, F, X, f = 2, tfarm = 0;
	scanf("%lf%lf%lf", &C, &F, &X);
	int farm = 1;
	double ans = tfarm + X / f, newans;
	while(true) {
		tfarm += C / f;
		f += F;
		newans = tfarm + X / f;
		if(newans < ans) {
			ans = newans;
		} else {
			break;
		}
	}
	return ans;
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++) {
		printf("Case #%d: %.7lf\n", t, work());
	}
	return 0;
}


