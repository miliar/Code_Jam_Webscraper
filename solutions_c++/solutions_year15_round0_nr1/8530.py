#include<stdio.h>
using namespace std;
char arr[10009];
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("q1.out", "w", stdout);
	int t, i, j, k, n, m, l, p = 1;
	scanf("%d", &t);
	while (t--) {
		scanf("%d", &n);
		scanf("%s", arr);
		m = 0;
		l = arr[0] - 48;
		for (i = 1; i <= n; i++) {
			if (arr[i] == '0') {
				continue;
			} else if (l >= i) {
				l = l + arr[i] - 48;
			} else {
				m = m + (i - l);
				l = i;
				l = l + arr[i] - 48;
			}
		}
		printf("Case #%d: %d\n", p++, m);
	}
	return 0;
}
