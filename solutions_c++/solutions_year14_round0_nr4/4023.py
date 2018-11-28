// Problem D. Deceitful War
#include <cstdio>
#include <algorithm>

using namespace std;

int main(int argc, char *argv[])
{
	int nc, ci;
	static double a[1024], b[1024];

	scanf("%d", &nc);
	for (ci = 1; ci <= nc; ci++) {
		int n;
		scanf("%d", &n);
		for (int i = 0; i < n; i++) scanf("%lf\n", &a[i]);
		for (int i = 0; i < n; i++) scanf("%lf\n", &b[i]);
		sort(a, a + n);
		sort(b, b + n);
		int ans1 = n, ans2 = n;

		for (int i = 0, j = 0; i < n && j < n; i++, j++)
			for ( ; j < n; j++)
				if (b[j] > a[i]) {
					ans2--;
					break;
				}

		for (int i = 0, j = 0; i < n && j < n; i++, j++) {
			for ( ; a[i] < b[j] && i < n; i++) ans1--;
		}

		printf("Case #%d: %d %d\n", ci, ans1, ans2);
	}

	return 0;
}
