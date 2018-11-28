#include <cstdio>

void process(int n) {
	bool mark[12];
	int nmark = 0;
	for (int i = 0; i<= 9; i++) {
		mark[i] = false;
	}
	long long m = n;
	while (nmark != 10) {
		long long temp = m;

		while (temp > 0) {
			if (!mark[temp%10]) {
				mark[temp%10] = true;
				nmark++;
			}
			temp = temp / 10;
		}
		if (nmark == 10) {
			break;
		} else {
			m += n;
		}
	}
	printf("%lld\n", m);
}

int main() {
	
	int cases;

	scanf("%d", &cases);

	for (int i = 1; i <= cases; i++) {
		printf("Case #%d: ", i);
		int n;
		scanf("%d", &n);
		if (n == 0) {
			printf("INSOMNIA\n");
		} else {
			process(n);
		}
	}

	return 0;
}