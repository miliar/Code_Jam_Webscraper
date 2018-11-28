#include <cstdio>
#include <cstring>

using namespace std;

int main() {
	int T, c, r, i, x, ct[20], n, res;
	scanf("%d", &T);
	c = 1;
	while (T--) {
		memset(ct, 0, sizeof ct);
		scanf("%d", &r);
		r--;
		for (i=0; i<16; i++) {
			scanf("%d", &x);
			if (i/4 == r) ct[x]++;
		}
		scanf("%d", &r);
		r--;
		for (i=0; i<16; i++) {
			scanf("%d", &x);
			if (i/4 == r) ct[x]++;
		}
		n = 0;
		for (i=1; i<=16; i++) {
			if (ct[i] == 2) {
				n++;
				if (n > 1) break;
				res = i;
			}
		}
		if (n == 1) printf("Case #%d: %d\n", c++, res);
		else if (n == 0) printf("Case #%d: Volunteer cheated!\n", c++);
		else printf("Case #%d: Bad magician!\n", c++);
	}
	return 0;
}

