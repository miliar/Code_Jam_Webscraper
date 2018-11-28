#include<iostream>
#include<vector>
#include<cstdio>

using namespace std;

typedef long long ll;

int main () {

	int casos;
	cin >> casos;
	for(int t=1; t<=casos ; t++) {
	
		double c, f, x;
		cin >> c >> f >> x;
		
		double acm = 0.;
		double mn = 1E10;
		double nf = 0;

		for(int i=0 ; i<100000; i++) {
			double total = acm + x/(2 + nf * f);
			mn = min(mn, total);

			acm += c / (2 + nf * f);
			nf += 1.;
		}

		printf("Case #%d: %.7lf\n", t, mn);	
	}

	return 0;
}
