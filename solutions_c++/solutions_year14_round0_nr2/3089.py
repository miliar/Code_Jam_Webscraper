#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <queue>
#include <algorithm>
using namespace std;

int t;
double c, f, x;
double t1, t2, s = 2, now, ans, tx;

int main () {
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	scanf("%d", &t);
	int cases = 0;
	while(t--) {
		ans = 0;
		s = 2;
		now = 0;
		scanf("%lf%lf%lf", &c, &f, &x);
		while (1) {
			t1 = (x - now) / s;
			if (now > c) {
				t2 = (x - (now - c)) / s;
				tx = 0;
			} else {
				t2 = (c - now) / s + x / (s + f);
				tx = (c - now) / s;
			}
			if (t1 < t2) {
				ans += t1;
				break;
			} else {
				ans += tx;
				now = 0;
				s += f;
			}
		}
		printf("Case #%d: ", ++cases);
		printf("%.7lf\n", ans);
	}
	return 0;
}
