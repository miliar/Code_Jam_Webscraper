#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	long long eps = 1e-7, ep = 1e-6;
	int t, y = 1;
	cin >> t;
	double c, f, x;
	double cap = 2;
	while (t--) {
		cap = 2;
		double sec = 0;
		cin >> c >> f >> x;
		while (true) {
			double s1 = x / cap;
			double s2 = (c / cap) + (x / (cap + f));
			if (s1 < s2) {
				sec += s1;
				break;
			} else {
				sec += (c / cap);
				cap += f;
			}
			sec += ep;
		}
		sec += eps;
		printf("Case #%d: %.7lf\n", y, sec);
		y++;
	}
	return 0;
}
