#include <iostream>
#include <cstdio>

using namespace std;

int main() {
	int t, n;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> n;
		if (n == 0) {
			printf("Case #%d: INSOMNIA\n", i+1);
			continue;
		}
		int d[10] = {0};
		for (int j = 1; ; j++) {
			int cc = n*j;
			while (cc > 0) {
				d[cc%10] = 1;
				cc /= 10;
			}
			int s = 0;
			for (int k = 0; k < 10; k++) {
				s += d[k];
			}
			if (s == 10) {
				printf("Case #%d: %d\n", i+1, n*j);
				break;
			}
		}
	}
	return 0;
}