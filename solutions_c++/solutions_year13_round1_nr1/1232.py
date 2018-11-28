#include <cstdio>

int main()
{
	freopen("p1.in", "r", stdin);
	freopen("p1.out", "w", stdout);

	int T;
	scanf("%d", &T);

	for (int _t = 1; _t <= T; _t++) {
		int r, t;
		scanf("%d %d", &r, &t);

		int csr = r; // radius
		int solution = 0;
		double inkleft = t;
		while (true) {
			double nextarea = (csr+1)*(csr+1) - (csr)*(csr);
			if (nextarea <= inkleft) {
				inkleft -= nextarea;
				solution++;
				csr += 2;
				continue;
			} else {
				break;
			}
		}

		printf("Case #%d: %d\n", _t, solution);
	}

	return 0;
}