#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;



int main() {
	int tc,n;
	cin >> tc;
	for (int T = 1; T <= tc; T++) {
		cin >> n;
		if (n == 0) {
			printf("Case #%d: INSOMNIA\n", T);
		} else {
			bool d[10];
			int c = 0;
			memset(d, false, sizeof d);
			int s = n;
			while (c != 10) {
				int tmp = s;
				while (tmp != 0) {
					if (!d[tmp%10]) {
						d[tmp%10] = true;
						c++;
					}
					tmp /= 10;
				}
				s += n;
			}
			printf("Case #%d: %d\n", T, s-n);
		}
	}
}