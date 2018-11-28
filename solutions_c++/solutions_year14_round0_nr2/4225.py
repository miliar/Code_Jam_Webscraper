#include <bits/stdc++.h>
using namespace std;

#define fr(a,b,c) for (int a = b; a < c; ++a)

int main() {
	int t, caso = 1;
	for (cin >> t; caso <= t; ++caso) {
		printf("Case #%d: ", caso);
		
		double c,f,x;
		cin >> c >> f >> x;
		double rate = 2;
		double t = 0;
		
		while (true) {
			double nf = c/rate;
			if (x/rate <= x/(rate+f) + nf) break;
			rate += f;
			t += nf;
		}
		t += x/rate;
		printf("%.7lf\n", t);
	}
	return 0;
}
