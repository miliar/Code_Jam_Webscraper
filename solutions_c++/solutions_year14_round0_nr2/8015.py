/*************************************************************************
    > File Name: b.cpp
    > Author: lax
    > Mail: xingkungao@gmail.com
    > Created Time: Sat 12 Apr 2014 09:53:18 PM CST
 ************************************************************************/

#include <iostream>
#include <cstdio>
using namespace std;
int T;
double e = 0.000001;
double c,f,x;
double v;
double cook;
double t, t1, t2;
int main() { 
	int kase = 0;
	scanf("%d", &T);
	while (kase++ < T) {
		cook = 0;
		t = 0;
		v = 2;
		scanf("%lf%lf%lf", &c, &f, &x);
		if (x <= c) {
			printf("Case #%d: %.7lf\n", kase,  x / v);
			continue;
		}
		while (1) {
			//if (cook == x + e || cook == x - e) {
			if (cook == x) {
				printf("Case #%d: %.7lf\n", kase, t);
				break;
			}
			if ( cook > x )break;
			t1 = (x - cook) / v;
			t2 = (c - cook) / v + x / (v + f);
			if (t1 < t2) {
				t += t1;
				cook = x;
			}
			else {
				t += (c-cook) / v;
				cook = 0;
				v += f;
			}
		}
	}
}
		/*while (cook < x) {
			t1 = (c-cook)/v;
			if (cook >= c) { // could buy
				t2 = (x-cook+c)/(v + f);
				if (t1 < t2) {
					t += t1;
					cook  = c;
				}
				else {
					t += t2;
					v += f;
					cook = x - c;
				}
			}
			else {
				t += t1;
			}
		}
		*/

