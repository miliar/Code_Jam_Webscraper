#include <cstdio>
#include <algorithm>
using namespace std;

int T, x, r, c;

int main() {
	freopen("D-large.in", "r", stdin);
	freopen("d1.out", "w", stdout);
	scanf("%d", &T);
	for (int k = 1; k <= T; k++) {
		scanf("%d%d%d", &x, &r, &c);
		if (r * c % x != 0 || x >= 7) printf("Case #%d: RICHARD\n", k);
		else {
			if (x == 1 || x == 2) printf("Case #%d: GABRIEL\n", k);
			else {
				if (x == 3) {
					if (min(r, c) <= 1) printf("Case #%d: RICHARD\n", k);
					else printf("Case #%d: GABRIEL\n", k);
				}
				if (x == 4) {
					if (min(r, c) <= 2) printf("Case #%d: RICHARD\n", k);
					else printf("Case #%d: GABRIEL\n", k);
				}else if (x == 5) {
					if (min(r, c) > 3) printf("Case #%d: GABRIEL\n", k);
					else if (min(r, c) < 3) printf("Case #%d: RICHARD\n", k);
					else {
						if (max(r, c) >= 6) printf("Case #%d: GABRIEL\n", k);
						else printf("Case #%d: RICHARD\n", k);
					}
				}else if (x == 6) {
					if (min(r, c) > 3) printf("Case #%d: GABRIEL\n", k);
					else if (min(r, c) <= 3) printf("Case #%d: RICHARD\n", k);
				}
			}
		}
	}
}
