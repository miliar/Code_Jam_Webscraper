#include <cstdio>

char str[1024];
int main() {
	int n, cnt, sum, t;
	int s_max;
	t = 1;
	scanf("%d", &n);
	while (n--) {
		scanf("%d %s", &s_max, str);
		cnt = 0;
		sum = str[0] - '0';
		for (int i = 1; i <= s_max; ++i) {
			int num = str[i] - '0';
			if (num == 0)
				continue;
			if (sum < i) {
				cnt += i - sum;
				sum = i;
			}
			sum += num;
		}
		printf("Case #%d: %d\n", t++, cnt);
	}
}