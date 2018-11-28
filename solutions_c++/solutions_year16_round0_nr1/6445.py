#include <stdio.h>

int t = 0, cnt = 0;
long long n = 0;
long long m = 0;
bool fin = false;
bool visited[10];
long long dynamic[1000010];

void get_digit(int digit) {
	if (digit < 10) {
		if (!visited[digit]) {
			visited[digit] = true;
			cnt++;
		}
		return;
	} else {
		get_digit(digit / 10);
		if (!visited[digit % 10]) {
			visited[digit % 10] = true;
			cnt++;
		}
		return;
	}
}

int main() {
	scanf("%d", &t);
	for (int j = 1; j <= t; j++) {
		scanf("%lld", &n);
		if (n == 0) {
			printf("Case #%d: INSOMNIA\n", j);
			continue;
		} else if (dynamic[n] == 0) {
			for (int i = 0; i < 10; i++) visited[i] = false;
			fin = false;
			cnt = 0;
			m = 0;
			while (cnt < 10) {
				m += n;
				get_digit(m);
			}
			dynamic[n] = m;
			printf("Case #%d: %lld\n", j, m);
		} else {
			printf("Case #%d: %lld\n", j, dynamic[n]);
		}
	}
	return 0;
}