#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

int t;
int n;
double v, x;

double r1, c1;
double r2, c2;

bool sama(double a, double b) {
	return fabs(a-b) < 0.000000001;
}

void solve(int z) {
	cin >> n;
	cin >> v >> x;
	cout << "Case #" << z << ": ";
	if (n == 1) {
		cin >> r1 >> c1;
		if (sama(x,c1)) printf("%.9lf\n", v/r1);
		else printf("IMPOSSIBLE\n");
	} else {
		cin >> r1 >> c1;
		cin >> r2 >> c2;
		if (c1 > c2) {swap(r1,r2); swap(c1,c2);}
		if (x < c1 || x > c2) {
			printf("IMPOSSIBLE\n");
			return;
		}
		if (sama(x,c1) && sama(x,c2)) {
			printf("%.9lf\n", v/(r1+r2));
			return;
		}
		double p = 0;
		for (double b = v; b >= 0.00000000000001; b /= 2) {
			while (true) {
				if (p+b > v) break;
				double up = p+b;
				double uz = (up*c1+(v-up)*c2)/v;
				if (uz > x) p = up;
				else break;
			}
		}
		double ut = max(p/r1,(v-p)/r2);
		printf("%.9lf\n", ut);
	}
}

int main() {
	cin >> t;
	for (int i = 1; i <= t; i++) solve(i);
}
