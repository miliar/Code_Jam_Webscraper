#include <cstdio>

char s[100];
int get(int x) {
	int ret = 0;
	sprintf(s, "%d", x);
	for (int i = 0; s[i]; i++)
		ret |= 1 << (s[i] - '0');
	return ret;
}

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		int n;
		scanf("%d", &n);
		if (n == 0) {
			printf("Case #%d: INSOMNIA\n", i+1);
		} else {
			int sum = n, mask = get(n);
			while (mask != 1023) {
				sum += n;
				mask |= get(sum);
			}
			printf("Case #%d: %d\n", i+1, sum);
		}
	}
}
