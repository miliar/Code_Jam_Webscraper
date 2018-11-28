#include <bits/stdc++.h>
using namespace std;
double c,f,x;
int main() {
	int tests; cin >> tests;
	for (int t = 1; t <= tests; ++t) {
		cin >> c >> f >> x;
		double pfxTime = 0, sol = 1e9, prod = 2;
		for (int fc = 0; fc <= 110000; ++fc) {
			sol = min(sol, pfxTime + (x/prod) );
			pfxTime += c / prod;
			prod += f;
		}
		printf("Case #%d: %.10lf\n",t, sol);
	}
}
