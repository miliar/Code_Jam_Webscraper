#include <stdio.h>

bool check(int cnt[10])
{
	for (int i=0; i<=9; i++) {
		if (cnt[i] == 0) { return false; }
	}
	return true;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);

	int _n;
	scanf("%d", &_n);

	for (int _t=1; _t<=_n; _t++) {
		int n, ret, cnt[10] = {0};
		scanf("%d", &n);
		if (n == 0) {
			printf("Case #%d: INSOMNIA\n", _t);
			continue;
		}
		for (int i=1;; i++) {
			int m = n*i;
			while (m > 0) {
				cnt[m%10] = 1;
				m /= 10;
			}
			if (check(cnt)) {
				ret = n*i;
				break;
			}
		}

		printf("Case #%d: %d\n", _t, ret);
	}
}
