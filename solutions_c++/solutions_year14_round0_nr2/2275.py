#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>

using namespace std;

#define FOR(i,a,b) for(int i = a ; i < b ; i++)

void solvePr2() {
	int T;
	cin >> T;
	for(int tc = 1 ; tc <= T ; tc++) {
		double c, f, x;
		double rate = 2;
		cin >> c >> f >> x;
		double t = 0;
		double cookieCount = 0;
		while(cookieCount < x) {
			double t1 = x / rate;
			double t2 = c / rate + x / (rate + f);
			if(t1 < t2) {
				t = t + x / rate;
				cookieCount = x;
				break;
			} else {
				t = t + c / rate;
				rate = rate + f;
			}
		}
		printf("Case #%d: %.6lf\n", tc, t);
	}
}

int main() {
	freopen("C:/Users/deepd/Downloads/in.txt", "r", stdin);
	freopen("C:/Users/deepd/Downloads/out.txt", "w", stdout);
	solvePr2();
	return 0;
}
