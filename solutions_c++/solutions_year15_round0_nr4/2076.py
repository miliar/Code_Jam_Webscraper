#include <cstdio>
#include <cmath>

using namespace std;

int main() {
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; ++i) {
		int x, r, c;
		scanf("%d%d%d", &x, &r, &c);
		int res = 0;
		switch(x) {
			case 1:
				res = 0;
				break;
			case 2:
				res = (r * c) % 2;
				break;
			case 3:
				if((int)fmin(r, c) >= 2 && (r * c) % 3 == 0) {
					res = 0;
				} else {
					res = 1;
				}
				break;
			case 4:
				if((int)fmin(r, c) >= 3 && (int)fmax(r, c) == 4) {
					res = 0;
				} else {
					res = 1;
				}
				break;
		}
		printf("Case #%d: %s\n", i, (res == 1) ? "RICHARD" : "GABRIEL");
	}
	return 0;
}