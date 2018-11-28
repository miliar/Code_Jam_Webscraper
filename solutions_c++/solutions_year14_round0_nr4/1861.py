#include <cstdio>
#include <string.h>
#include <cstring>
#include <algorithm>
using namespace std;
double eps = 1e-12;

double a[2000], b[2000];
int n, m, testnum;

int main() {
	freopen("D-large.in.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &testnum);
	int l1, l2, r1, r2, ans1, ans2;
	for (int tt = 1; tt <= testnum; tt++) {
		scanf("%d", &n);
		for (int i = 1; i <= n; i++) 
			scanf("%lf", &a[i]);
		for (int i = 1; i <= n; i++) 
			scanf("%lf", &b[i]);
		sort(a + 1, a + n + 1);
		sort(b + 1, b + n + 1);
		l1 = 1; r1 = n;
		l2 = 1; r2 = n;
		ans1 = 0; ans2 = 0;
		for (int i = 1; i <= n; i++) {
			if (a[l1] > b[l2]) { ans1++; l1++; l2++;} else {l1++;r2--;}
		}
		l1 = 1; r1 = n;
		l2 = 1; r2 = n;
		for (int i = 1; i <= n; i++) {
			if (a[r1] < b[r2]) {ans2++; r1--;r2--;} else {r1--;}
		}
		printf("Case #%d: %d %d\n", tt, ans1, n - ans2);
	}
	return 0;
}