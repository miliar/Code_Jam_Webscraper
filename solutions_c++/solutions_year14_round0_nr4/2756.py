#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

const int N = 1005;
int t, n, i, j, ans1, ans2;
double a1[N], a2[N];

int main() {
	int cas = 0;
	scanf("%d", &t);
	while (t--) {
		ans1 = ans2 = 0;
		scanf("%d", &n);
		for (i = 0; i < n; i++)
			scanf("%lf", &a1[i]);
		for (i = 0; i < n; i++)
			scanf("%lf", &a2[i]);
		sort(a1, a1 + n);
		sort(a2, a2 + n);
		i = 0; j = 0;
		while (i != n && j != n) {
			if (a1[i] > a2[j])
				j++;
			else {
				i++; j++;
			}
		}
		ans2 = j - i;
		int s = 0, e = n - 1;
		j = n - 1;
		while (s <= e) {
			if (a1[e] < a2[j]) {
				s++; j--;
			}
			else {
				e--; j--;
				ans1++;
			}
		}
		printf("Case #%d: %d %d\n", ++cas, ans1, ans2);
	}
	return 0;
}
