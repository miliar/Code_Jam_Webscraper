#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cstdio>
using namespace std;

int main() {
	int t;
	cin>>t;
	for (int l = 1; l <= t; ++l) {
		double c, f, x, ans, tmp = 0;
		cin>>c>>f>>x;
		ans = x/2.;
		int n = (int)x+1;
		for (int i = 0; i < n; ++i) {
			tmp += c/(i*f+2.);
			ans = min(ans, tmp+x/(2.+(i+1)*f));
		}
		printf("Case #%d: %.7lf\n",l, ans);
	}
}