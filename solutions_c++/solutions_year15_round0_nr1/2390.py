#include <cstdio>
const int nmax = 1000 + 18;

int n, ans, sum;
char a[nmax];

int main()
{
	int T;
	scanf("%d", &T);
	for (int cases = 1; cases <= T; ++cases) {
		scanf("%d%s", &n, a);
		sum = ans = 0;
		for (int i = 0; i <= n; ++i) {
			int now = a[i] - '0';
			if (sum < i) {
				ans += i - sum;
				sum = i;
			}
			sum += now;
		}
		printf("Case #%d: %d\n", cases, ans);
	}
	return 0;
}
