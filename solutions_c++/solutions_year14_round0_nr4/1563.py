#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string.h>
#include <string>
using namespace std;

const int maxn = 1000 + 10;
double a[maxn], b[maxn];
int n;

int main()
{
	freopen("D-large.in", "r", stdin);
	freopen("d_large.out", "w", stdout);
	int TextN, TT = 0;
	scanf("%d", &TextN);
	while (TextN--) {
		scanf("%d", &n);
		for (int i = 1; i <= n; i++) scanf("%lf", a + i);
		for (int j = 1; j <= n; j++) scanf("%lf", b + j);
		sort(a+1, a+1+n);
		sort(b+1, b+1+n);

		int k = 1;
		for (int i = 1; i <= n; i++)
			if (b[i] > a[k]) k++;
		
		int ans = 0;
		int p = 1, q = 1;
		while (p <= n && q <= n) {
			if (a[p] < b[q]) {
				++ans; p++;
			} else {
				p++, q++;
			}
		}

		printf("Case #%d: %d %d\n", ++TT, n - ans, n - k + 1);
	}
	return 0;
}